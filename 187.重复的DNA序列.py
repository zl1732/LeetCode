#
# @lc app=leetcode.cn id=187 lang=python3
# @lcpr version=30203
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    """
    把 AGCT 四种字符等价为 0123 四个数字，那么长度为 L = 10 的一个碱基序列其实就可以等价为一个十位数，这个数字可以唯一标识一个子串。而且窗口移动的过程，其实就是给这个数字的最低位添加数字，并删除最高位数字的过程，回顾之前的讲解，添加和删除数字的运算就是两个公式，可以在 
    O(1) 的时间完成。
    然后，我们不要在哈希集合中直接存储子串了，而是存储子串对应的十位数。因为一个十位数可以唯一标识一个子串，所以也可以起到识别重复的作用。
    
    在滑动窗口中快速计算窗口中元素的哈希值，叫做滑动哈希技巧。

    进一步，我们用一个长度为 10 的十进制数来标识一个长度为 10 的碱基字符序列，这个数字可能达到 10^10，int 存不下，这需要 long 类型存储。但你注意这个十进制数中的每一位数字只会局限于 0,1,2,3，是不是有些浪费？

    换句话说，我们需要存储的其实只是一个长度为 10 的四进制数（共包含 4^10 个数字）
    
    
    # 思路
    L = 10
    # 集合中不要存储字符串了，而是存储字符串对应的哈希值
    seen = set()

    # 滑动窗口代码框架
    window = CharWindow()
    left, right = 0, 0
    while right < len(s):
        # 扩大窗口，移入字符
        window.addRight(s[right])
        right += 1
        
        # 当子串的长度达到要求
        if right - left == L:
            # 获取当前窗口内字符串的哈希值，时间 O(1)
            windowHash = window.hashCode()
            # 根据哈希值判断是否曾经出现过相同的子串
            if windowHash in seen:
                # 当前窗口中的子串是重复出现的
                print(window.toString())
            else:
                # 当前窗口中的子串之前没有出现过，记下来
                seen.add(windowHash)

            # 缩小窗口，移出字符
            window.removeLeft()
            left += 1
    
    """



# 在数字的最低位添加数字以及如何删除数字的最高位
# R 可以改成其他数字，其他进制数
"""
// ****** 在最低位添加一个数字 ******
int number = 8264;
// number 的进制
int R = 10;
// 想在 number 的最低位添加的数字
int appendVal = 3;
// 运算，在最低位添加一位
number = R * number + appendVal;
// 此时 number = 82643

// ****** 在最高位删除一个数字 ******
int number = 8264;
// number 的进制
int R = 10;
// number 最高位的数字
int removeVal = 8;
// 此时 number 的位数
int L = 4;
// 运算，删除最高位数字
number = number - removeVal * Math.pow(R, L-1);
// 此时 number = 264

"""
"""
// ****** 在最低位添加一个数字 ******
// number 的进制
int R = 4;
// 想在 number 的最低位添加的数字
int appendVal = 0~3 中的任意数字;
// 运算，在最低位添加一位
number = R * number + appendVal;

// ****** 在最高位删除一个数字 ******
// number 的进制
int R = 4;
// number 最高位的数字
int removeVal = 0~3 中的任意数字;
// 此时 number 的位数
int L = ?;
// 运算，删除最高位数字
number = number - removeVal * R^(L-1);
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        if len(s) < L:
            return []

        code = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
        R = 4
        RL = R ** (L - 1)

        seen = set()
        res = set()
        window_hash = 0
        left = 0

        for right, ch in enumerate(s):
            window_hash = R * window_hash + code[ch]

            # 当窗口长度达到 L
            if right - left + 1 == L:
                if window_hash in seen:
                    res.add(s[left:right+1])
                else:
                    seen.add(window_hash)
                # 移出最高位
                window_hash -= code[s[left]] * RL
                left += 1

        return list(res)


    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        L = 10
        if n < L:
            return []
        
        code = {'A':0, 'C':1, 'G':2, 'T':3}
        mask = (1 << (2 * L)) - 1   # 20 位全 1
        window_hash = 0
        seen = set()       # 已见过的编码
        res = set()   # 出现至少两次的子串

        for i, ch in enumerate(s):
            """
            所以当 x 比 mask 短时，& mask 的行为就是你说的那样：
            👉 会自动在前面视作补 0，对齐后再按位与。
            """
            window_hash = ((window_hash << 2) | code[ch]) & mask
            if i >= L - 1:
                if window_hash in seen:
                    res.add(s[i - L + 1 : i + 1])
                else:
                    seen.add(window_hash)
        return list(res)

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        L = 10
        if n < L:
            return []
        code = {'A':0, 'C':1, 'G':2, 'T':3}
        mask = (1 << (2*L)) -1
        window_hash = 0
        seen = set()
        res = set()

        for i, ch in enumerate(s):
            window_hash = (window_hash<<2 | code[ch] ) & mask
            if i >= L-1:
                if window_hash in seen:
                    res.add(s[i-L+1:i+1])
                else:
                    seen.add(window_hash)
        return list(res)


# @lc code=end



#
# @lcpr case=start
# "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAAAAA"\n
# @lcpr case=end

#

