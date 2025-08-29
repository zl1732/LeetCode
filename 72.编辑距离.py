#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30201
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        # i，j 初始化指向最后一个索引
        return self.dp(s1, m - 1, s2, n - 1)

    # 定义：返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        # base case
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if s1[i] == s2[j]:
            # 啥都不做
            return self.dp(s1, i - 1, s2, j - 1)

        return min(
            # 插入
            self.dp(s1, i, s2, j - 1) + 1,
            # 删除
            self.dp(s1, i - 1, s2, j) + 1,
            # 替换
            self.dp(s1, i - 1, s2, j - 1) + 1
        )


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        self.memo = [[-1]*n for _ in range(m)]
        return self.dp(s1, m-1, s2, n-1)
    
    def dp(self, s1, i, s2, j):
        if i == -1:
            return j+1
        if j == -1:
            return i+1
        # 查memo
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if s1[i] == s2[j]:
            # 没有操作
            self.memo[i][j] = self.dp(s1, i-1, s2, j-1)
            return self.memo[i][j]
        
        self.memo[i][j] = min(
            # 替换
            self.dp(s1, i-1, s2, j-1)+1,
            # 插入
            self.dp(s1, i, s2, j-1)+1,
            # 删除
            self.dp(s1, i-1, s2, j)+1
        )
        return self.memo[i][j]
    

# 自底向上
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        # 储存着整个 s1 和 s2 的最小编辑距离
        return dp[m][n]

    def min(self, a: int, b: int, c: int) -> int:
        return min(a, min(b, c))
# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

