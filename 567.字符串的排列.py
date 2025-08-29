#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30201
#
# [567] 字符串的排列
#

# @lc code=start
"""
注意这个缩窗口的条件：
while left < right and right-left >= len(s1):
右侧先前进，当窗口到达len(s1),才能开始缩
如果只有left < right，则right走一步，left就会走一步，错
"""
class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        left = right = 0

        need = Counter(s1)
        required = len(need)
        valid = 0

        # 本题不需要了
        #best = 0
        #min_len = float('inf')

        while right < len(s2):
            c = s2[right]
            right += 1
            # 只记录在s1出现的字母
            if c in need:
                # 先update window
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]: # 到达
                    valid += 1
            
            """
            这个位置不对，收缩之后才找到，不是在拓展的时候找到
            """
            # if valid == required:
            #     return True        
                                   # 📢长度不能小过s1
            while left < right and right-left == len(s1):
                # 先检测是否更好 本题不需要了
                #if right - left < min_len:
                #    min_len = right - left
                #    best = left

                # 检测是否找到
                if valid == required:
                    return True     
                  
                # 删除
                d = s2[left]
                """
                注意习惯，不是 left -= 1
                """
                left += 1
                # 判断是否在need里
                # if d in need:
                #     window[d] = window[d] - 1
                #     if window[d] < need[d]: # 到达
                #         valid -= 1
                """
                特别注意要这么写，具体见下面
                """
                if d in need:
                    if window[d] == need[d]: # 到达
                        valid -= 1
                    window[d] = window[d] - 1
                        
        return False
                    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        left = right = 0

        need = Counter(s1)
        required = len(need)
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1
            # 只记录在s1出现的字母
            if c in need:
                # 先update window
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]: # 到达
                    valid += 1
            
            while left < right and right-left == len(s1):
                # 检测是否找到
                if valid == required:
                    return True        
                # 删除
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]: # 到达
                        valid -= 1
                    window[d] = window[d] - 1
            # 不能放在这里
            # if valid == required:
            #     return True            
        return False
                    



from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
        window = {}
        left = right = 0

        need = Counter(s1)
        required = len(need)
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]: # 到达
                    print("到达的字母：",c)
                    valid += 1
            
            while right-left >= len(s1):
            # while left < right:
            # while right-left == len(s1):
                # print(s2[left:right+1],valid,required)
                # print(window)
                # print(left, "*"*20)
                print(left, right)
                if valid == required:
                    return True     
                # 删除
                d = s2[left]
                left += 1
                # if d in need:
                #     window[d] = window[d] - 1
                #     if window[d] < need[d]: # 到达
                #         print("删除的字母：",d)
                #         valid -= 1
                if d in need:
                    if window[d] == need[d]: # 到达
                        print("删除的字母：",d)
                        valid -= 1
                    window[d] = window[d] - 1
        return False

s1 = "trinitrophenylmethylnitramine"
s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"


s1 = "abc"
s2 = "aflsacdbaec"


# print(checkInclusion(s1, s2))

"""
#### 为什么这会出问题？

* 如果 **字符原本就没达标**（`window[d] < need[d]`），  
  - **正确写法**：❶ 条件不成立，不动 `valid` ✔️  
  - **错误写法**：删完之后还会满足 `window[d] < need[d]`，于是误扣 `valid` ❌  
  - ⮕ `valid` 被白白减 1

这就是你在第 5 行开始看到 **8 vs 7** 的根源：错误版把一个本来就不达标的字符又扣了一分，`valid` 从那一刻起就一直少 1。

---

### 4 · 把这个道理放在你的长用例里看一眼

```python
s1 = "trinitrophenylmethylnitramine"     # need['t'] = 4
s2 = "dinitrophenylhydrazine …"          # 第 4 位正好是 't'

❌
left = 4 valid = 7
{'i': 3, 'n': 3, 't': [3], 'r': 4, 'o': 2, 'p': 2, 'h': 3, 'e': 3, 'y': 2, 'l': 1, 'a': 1}
删除的字母： t
到达的字母： n
left = 5 valid = 7
{'i': 3, 'n': 4, 't': [2], 'r': 4, 'o': 2, 'p': 2, 'h': 3, 'e': 3, 'y': 2, 'l': 1, 'a': 1}

✅
left = 4 valid = 7
{'i': 3, 'n': 3, 't': 3, 'r': 4, 'o': 2, 'p': 2, 'h': 3, 'e': 3, 'y': 2, 'l': 1, 'a': 1}
到达的字母： n
left = 5 valid = 8
{'i': 3, 'n': 4, 't': 2, 'r': 4, 'o': 2, 'p': 2, 'h': 3, 'e': 3, 'y': 2, 'l': 1, 'a': 1}

    当 left = 4 时窗口里 't' 的计数是 3 (< 4)，它本来就没达标，所以 valid 不应该受它影响。

    正确写法 不减分，valid 还是 7。

    错误写法 先减到 2，再看见 “< need”，误以为自己刚失去 1 分，于是 valid 变 6。
    下一轮右边进来一个新字符把 valid 加 1，也只能追到 7。

从这一刻开始，两条执行路径就差 1 分；到真正命中的窗口（trinitrophenylmethylnitramine）时：
版本	valid	required	结果
正确写法	12	12	返回 True
错误写法	11	12	误判为 False
"""
# @lc code=end



#
# @lcpr case=start
# "eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "eidboaoo"\n
# @lcpr case=end

#

