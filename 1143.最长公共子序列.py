#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30201
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(text1,0, text2,0)
        


    def dp(self, s1, i, s2, j):
        # base case
        if i == len(s1) or j == len(s2):
            return 0
        
        # 转移方程1：相同,+1,同时往后走
        if s1[i] == s2[j]:
            return 1+self.dp(s1, i+1, s2, j+1)
        # 转移方程1：不相同,比较最大值
        else:
            """
            情况三「s1[i] 和 s2[j] 都不在 lcs 中」其实可以直接忽略。
            况三在计算 s1[i+1..] 和 s2[j+1..] 的 lcs 长度，
            这个长度肯定是小于等于情况二 s1[i..] 和 s2[j+1..] 中的 lcs 长度的，
            因为 s1[i+1..] 比 s1[i..] 短
            """
            return max(
                self.dp(s1, i, s2, j+1),
                self.dp(s1, i+1, s2, j)
                #self.dp(s1, i+1, s2, j+1)
            )
        
    def dp(self, s1, i, s2, j):
        # base case
        if i == len(s1) or j == len(s2):
            return 0
        
        if self.memo[i][j]!=-1:
            return self.memo[i][j]
        
        if s1[i] == s2[j]:
            self.memo[i][j] = 1+self.dp(s1, i+1, s2, j+1)
            # return self.memo[i][j]
        
        else:
            self.memo[i][j] = max(
                self.dp(s1, i, s2, j+1),
                self.dp(s1, i+1, s2, j))
        return self.memo[i][j]
            

"""
自底向上
"""
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case: dp[0][..] = dp[..][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # s1[i-1] 和 s2[j-1] 必然在 lcs 中
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # s1[i-1] 和 s2[j-1] 至少有一个不在 lcs 中
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # base case
        ## dp[0][j] dp[i][j] =0
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 注意是前一个 i-1, j-1
                if s1[i-1] == s2[j-1]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                # 没匹配上
                else:
                    dp[i][j] =  max(dp[i][j-1],dp[i-1][j])
        return dp[i][j]

        
            
# @lc code=end



#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

