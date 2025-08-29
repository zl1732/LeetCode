#
# @lc app=leetcode.cn id=516 lang=python3
# @lcpr version=30201
#
# [516] 最长回文子序列
#

# @lc code=start
# 反着
"""
为什么「反着遍历」——也就是 从右往左找子串起点 i，从左往右找终点 j（i 从大到小，j 从小到大） 是有效的。
如果你“从前往后找 i”，你会想用 dp[i+1][j] 的值
但此时 dp[i+1][j] 还没有计算出来！

起始点i 从最后往前
结尾点j 从i+1往后到n
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp 数组全部初始化为 0
        dp = [[0] * n for _ in range(n)]
        # base case
        """
        注意到n
        """
        for i in range(n):
            dp[i][i] = 1
        # 反着遍历保证正确的状态转移
        """
        注意是到-1！！！才能走到0
        """
        for i in range(n - 1, -1, -1):
            """
            从i+1开始
            """
            for j in range(i + 1, n):
                # 状态转移方程
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    """
                    不能+1， 只是重新找！！
                    """
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 整个 s 的最长回文子串长度
        return dp[0][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n-1):
            dp[i][i] = 1
        
        for i in range(n-1, 0, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    """
                    如果是for j in range(i, n):
                    dp[i+1][j-1] 这里报错 
                    i,j = 4, 4
                    i+1, j-1 = 5, 3
                    dp[5][3] 超了

                    解决办法1： 让j 从 i+1开始
                    解决办法2: 加判断条件j > i、i！=j
                    """
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j]) + 1
        return dp[0][n-1]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if i!=j:
        #             if s[i] == s[j]:
        #                 dp[i][j] = dp[i+1][j-1] + 2
        #             else:
        #                 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


# # 斜着
# def longestPalindromeSubseq(s: str) -> int:
#     n = len(s)
#     dp = [[0] * n for _ in range(n)]

#     # 初始化对角线：单个字符是回文，长度为 1
#     for i in range(n):
#         dp[i][i] = 1

#     # 斜着填表：遍历子串长度
#     for length in range(2, n + 1):  # 子串长度从2到n
#         for i in range(n - length + 1):
#             j = i + length - 1  # 右端点
#             if s[i] == s[j]:
#                 dp[i][j] = dp[i + 1][j - 1] + 2
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

#     return dp[0][n - 1]




# from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        self.memo = [[-1]* n for _ in range(n)]
        return self.dp(s, 0, len(s) - 1)

    def dp(self, s, i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if s[i] == s[j]:
            self.memo[i][j] = self.dp(s, i + 1, j - 1) + 2
            return self.memo[i][j]
        else:
            self.memo[i][j] = max(self.dp(s, i + 1, j), self.dp(s, i, j - 1))
            return self.memo[i][j]

        



# @lc code=end



#
# @lcpr case=start
# "bbbab"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

