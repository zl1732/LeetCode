#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30203
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s)-1
        while lo< hi:
            """isalnum:如果是 字母 (a–z, A–Z) 或 数字 (0–9)，返回 True"""
            while lo< hi and not s[lo].isalnum():
                lo += 1
            while lo< hi and not s[hi].isalnum():
                hi -= 1
            """注意转换大小写"""
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
        
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

