#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30203
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    """
    for 0 <= i < len(s):
        找到以 s[i] 为中心的回文串
        找到以 s[i] 和 s[i+1] 为中心的回文串
        更新答案
    # 判断回文子串

    def isPalindrome(s: str) -> bool:
        # 一左一右两个指针相向而行
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    """
    def longestPalindrome(self, s: str) -> str:
        res = []
        #for i in range(len(s)-1):  # ❌，会少最后一位的情况，应该交由下面的函数判断
        for i in range(len(s)):
            # 奇数
            s1 = self.palindrome(s, i, i)
            # 偶数
            s2 = self.palindrome(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

        
    # def palindrome(self, s, i, j):
    #     while i>=0 and j< len(s):
    #         if s[i] != s[j]:
    #             break
    #         i-= 1
    #         j+=1
    #     return s[i+1:j]
    
    """
    学会吧判断写进 while 里面
    """
    def palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

        
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

