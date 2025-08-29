#
# @lc app=leetcode.cn id=1312 lang=python3
# @lcpr version=30202
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution:
    """
    解法1，思路类似516
    1. 如果 s[i] == s[j],直接s[i+1] s[j-1]
    2. 如果 s[i] != s[j],看s[i] s[j+1]、s[i+1] s[j] 然后加一个插入
    
    解法2，直接借用516
    len(s)-516
    """
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # base case，单个字母本身已经是回文串
        for i in range(n):
            dp[i][i] = 0
        # 还是i从后往前，j从i往后到末尾
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 无需插入
                if s[i] == s[j]:
                    # 只要涉及+-1，特别注意边界，查for的起止点
                    dp[i][j] = dp[i+1][j-1]
                else:
                    # 需要插入一位，对上s[i]或者s[j]
                    dp[i][j] = 1+ min(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


# 递归方法
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        self.memo = [[-1]* n for _ in range(n)]
        return self.dp(s, 0, len(s) - 1)

    def dp(self, s, i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if s[i] == s[j]:
            self.memo[i][j] = self.dp(s, i + 1, j - 1)
            return self.memo[i][j]
        else:
            self.memo[i][j] = 1 + min(self.dp(s, i + 1, j), self.dp(s, i, j - 1))
            return self.memo[i][j]



# @lc code=end



#
# @lcpr case=start
# "zzazz"\n
# @lcpr case=end

# @lcpr case=start
# "mbadm"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

#

