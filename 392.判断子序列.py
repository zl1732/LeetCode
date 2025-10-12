#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30203
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i, j = 0,0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
        return len(s) == i
    
    def isSubsequence(self, s: str, t: str) -> bool:
        # if not s:
        #     return True
        # if not t:
        #     return False
        i, j = 0,0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return len(s) == i
# @lc code=end



#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#

