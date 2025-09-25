#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30203
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 找到最短字符
        min_l = float("inf")
        min_s = ""
        for str in strs:
            l = len(str)
            if l < min_l:
                min_l = l
                min_s = str

        # 遍历比较
        res = ""
        k = 0
        while k < min_l:
            char = min_s[k]
            for str in strs:
                if str[k] != char:
                    return res
            res += char
            k += 1
        return res


    """
    优化
    1. 增加base case
    2. 直接找到最短字符串
    3. Python 里频繁 res += char 会不断生成新字符串，时间复杂度退化。更好的方式是用 list 累积，再用 ''.join。
        每次执行 res += ch，都会新建一个 新的字符串对象
        总的拷贝量：1 + 2 + ... + n = O(n^2)。

        list.append(ch) 是摊还 O(1) 操作，不涉及整体拷贝。
        最终 ''.join(res) 会一次性申请一块连续内存，总体是O(N)

    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_s = min(strs, key=len)  # 直接找最短串
        prefix = []

        for i, ch in enumerate(min_s):
            for s in strs:
                if s[i] != ch:
                    return ''.join(prefix)
            prefix.append(ch)

        return ''.join(prefix)
            


# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

