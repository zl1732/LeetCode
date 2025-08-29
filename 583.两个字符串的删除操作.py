#
# @lc app=leetcode.cn id=583 lang=python3
# @lcpr version=30201
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(word1, m-1, word2, n-1)
    
    def dp(self, s1, i, s2, j):
        # base case 删除
        if i == -1:
            return j+1
        if j == -1:
            return i+1
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i-1, s2, j-1)
            return self.memo[i][j]
        # either del s1, or del s2
        """
        最少次数！！！！！！min
        """
        self.memo[i][j] = 1 + min(
            self.dp(s1, i-1, s2, j),
            self.dp(s1, i, s2, j-1)
        )
        return self.memo[i][j]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        lcs = self.longestCommonSubsequence(word1, word2)
        return m-lcs+n-lcs

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # base case
        ##
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[i][j]
                    


# @lc code=end



#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"etco"\n
# @lcpr case=end

#

