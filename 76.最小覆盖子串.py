#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30201
#
# [76] 最小覆盖子串
#

# @lc code=start
"""
非常关键：
                    # # 写法1：
                    # # 注意这里是先检测，再删除d， 所以是==
                    # if window[d] == need[d]:
                    #     valid -= 1
                    # window[d] -= 1
                    
                    # 写法2：
                    # 注意这里是先删除d，再检测 所以是<
                    # 不用再window.get(c, 0) - 1 
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1

为什么在本题中可以使用写法2，但是在567中不可以：
                    因为while的条件不一样！


| 题号             | 缩窗进入条件                                                      | 会被移出的字符当时一定已经“达标”吗？                                                   |
| --------------   | -----------------------------------------------------           | --------------------------------------------------------------------- |
| **76 最小覆盖子串**| `while valid == required:`<br>（只有当 **所有字符都已满足** 时才收缩）| **是的**。因为 `valid == required` 表示此刻每个 `ch` 都满足 `window[ch] ≥ need[ch]` |
| **567 字符串的排列**| `while right-left ≥ len(s1):`<br>（只要窗口达到固定长度就收缩）     | **不一定**。窗口可能还没完全满足 `need`                                             |

                    在 76 中，这个假设永远成立
                    因为只有 valid == required 时才会进入收缩：
                    → 每一种字符当时必满足  window[ch] ≥ need[ch]
                    所以被删字符 肯定“原本达标”，删 1 个后才可能低于需量，valid -= 1 正好把它从“已满足”改为“未满足”——逻辑完全正确。

                    在 567 中，这个假设就可能被破坏
                    窗口达到固定长度就开始收缩，此时 很多字符仍可能不足量 (window[ch] < need[ch])。


结论： “先判 == need[ch] 再减” 是最稳妥、通用的一版——

| 做法                                                                       | 适用范围                                                                       | 为何更 robust                                  |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------- |
| **先判再减**<br>`if window[ch] == need[ch]: valid -= 1`<br>`window[ch] -= 1` | ✔️ 所有滑窗题（固定长度 or 可变长度、是否已满足都行）                                             | 删除前若**刚好达标**才扣 `valid`，不管删前是欠缺、达标、超标，逻辑都正确。 |
| **先减再判 `< need`**                                                        | 仅当收缩循环在 `valid == required` 条件下触发（LeetCode 76、Minimum Window Substring 这类） | 假设“被删字符原本必达标”。若此前就欠缺，会误扣 `valid`。           |

"""
class Solution:
    """
    ❌ 存在的问题：
    1. contain() 每次都要遍历 tgt，复杂度是 O(m)，
    当放在一个循环里，就会导致整体 O(n * m)，不满足线性时间要求。
    
    这其实是个假的滑动窗口
    注意滑动窗口里不能再用别的循环判断
    """
    def minWindow(self, s: str, t: str) -> str:
        def contain(window, tgt):
            for k in tgt.keys():
                if tgt[k] > window.get(k,0):
                    return False
            return True
            
        left = right = 0
        best_left = best_right = 0
        # 生成目标查表
        best_length= 10000
        tgt = {}
        for c in t:
            tgt[c] = tgt.get(c, 0) + 1

        window = {}
        while right < len(s):
            c = s[right]
            window[c] = window.get(c,0) + 1
            right += 1

            while left < right and contain(window, tgt):
                if right-left < best_length:
                    best_left = left
                    best_right = right
                    best_length = right-left
                d = s[left]
                window[d] -= 1
                left += 1


        if best_length == float('inf'):
            return ""
        return s[best_left:best_right]


    """
    ❎ 错误分析：
    🧠 想法引导 1: “window 是否 **包含了所有需要的字符（数量也满足）”？"
    🧩 那我们能不能“记住”哪些字符已经满足了，只要有 3 个字符满足需求，就说明 window 满足了？
    ✍️ 加一个变量，比如叫 valid，记录当前满足了多少个字符的需求？
    👉 问题 1：
    什么时候可以让 valid += 1？
    """
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        valid = 0
        best_left = best_right = 0
        best_length= float('inf')

        # 生成目标查表
        tgt = {}
        for c in t:
            tgt[c] = tgt.get(c, 0) + 1
        valid_t = len(tgt.keys())

        window = {}
        while right < len(s):
            c = s[right]
            window[c] = window.get(c,0) + 1
            right += 1
            # 判断 valid 是否满足，注意这里是右移，所以只会单调增
            if c in tgt and window[c] == tgt[c]:
                valid += 1

            while left < right and valid == valid_t:
                if right-left < best_length:
                    best_left = left
                    best_right = right
                    best_length = right-left
                
                d = s[left]
                window[d] -= 1
                left += 1

                # 更新 valid
                """
                if d in tgt and window[d] == tgt[d]:注意不是==
                你是在 window[d] 刚好等于 tgt[d] 的时候 valid -= 1，但实际上 这个时候字符还刚好满足需求，我们还不应该减！
                
                上面先执行了window[d] -= 1
                所以这里应该是 <
                """
                if d in tgt and window[d] < tgt[d]:
                    valid -= 1

        if best_length == float('inf'):
            return ""
        return s[best_left:best_right]


    """
    优化：
    0. 使用float('inf')
    1. 只在 c in need 时才更新 window？
        * 避免记录无关字符，减少哈希表的空间膨胀、提高判断效率。
    2. 使用 Counter(t) 构建字典
    3. 命名	best_left, best_length -> start, min_len
    """

    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        required = len(need)
        valid = 0

        start = 0
        min_len = float('inf')
        
        window = {}
        left = right = 0

        while right < len(s):
            c = s[right]
            # 这里没更新window，因为要先检测字母是否在need里
            right += 1

            # window不记除了need以外的字母
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
        
            while valid == required:
                # 先检测是否为更好的答案
                if right - left < min_len:
                    """
                    start = [left, right]
                    📚 社区惯例	✅ LeetCode 解法主流	⚠️ 不常见，不建议
                    """
                    start = left
                    min_len = right - left

                d = s[left]
                # 一样，检测是否在need里
                left += 1
                
                if d in need:
                    # # 写法1：
                    # # 注意这里是先检测，再删除d， 所以是==
                    # if window[d] == need[d]:
                    #     valid -= 1
                    # window[d] -= 1
                    
                    # 写法2：
                    # 注意这里是先删除d，再检测 所以是<
                    # 不用再window.get(c, 0) - 1 
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
                    
        return s[start:start + min_len] if min_len != float('inf') else ""

    # 自己写
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        required = len(need)
        valid = 0

        start = 0
        min_len = float('inf')
        
        window = {}
        left = right = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
        
            while valid == required:
                if right - left < min_len:
                    start = left
                    min_len = right - left

                d = s[left]
                left += 1
                
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
                    
        return s[start:start + min_len] if min_len != float('inf') else ""



# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

