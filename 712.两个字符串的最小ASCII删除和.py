#
# @lc app=leetcode.cn id=712 lang=python3
# @lcpr version=30201
#
# [712] 两个字符串的最小ASCII删除和
#

# @lc code=start
class Solution:
    #ord(s2[k])
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(word1, m-1, word2, n-1)
    
    def dp(self,s1, i, s2, j):
        m, n = len(s1), len(s2)
        res = 0
        # base case 删除
        if i == -1:
            for k in range(j+1):
                res += ord(s2[k])
            return res
        if j == -1:
            for k in range(i+1):
                res += ord(s1[k])
            return res
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i-1, s2, j-1)
            return self.memo[i][j]
        # either del s1, or del s2

        self.memo[i][j] = min(
            self.dp(s1, i-1, s2, j) + ord(s1[i]),
            self.dp(s1, i, s2, j-1) + ord(s2[j])
        )
        return self.memo[i][j]


"""
也可以从前往后找
"""
class Solution:
    memo = []
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(s1, 0, s2, 0)

    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        res = 0
        # base case
        if i == len(s1):
            for k in range(j, len(s2)):
                res += ord(s2[k])
            return res
        if j == len(s2):
            for k in range(i, len(s1)):
                res += ord(s1[k])
            return res

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i + 1, s2, j + 1)
        else:
            self.memo[i][j] = min(
                ord(s1[i]) + self.dp(s1, i + 1, s2, j),
                ord(s2[j]) + self.dp(s1, i, s2, j + 1)
            )
        return self.memo[i][j]
# @lc code=end



#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "delete"\n"leet"\n
# @lcpr case=end

#

