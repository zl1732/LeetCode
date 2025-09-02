#
# @lc app=leetcode id=509 lang=python3
# @lcpr version=30201
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    # base top down, brutal force
    def fib(self, n: int) -> int:
        # base
        if n==0 or n==1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # top down with memory
    # 相当于 0,1的情况不走memo，直接走函数输出0,1
    def fib(self, n: int) -> int:
        memo = {}
        # base
        if n==0 or n==1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]

    # bottom top with memory 其实是迭代
    def fib(self, n: int) -> int:
        # base
        if n==0 or n==1:
            return n
        # dp table 注意命名
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    # labuladong
    def fib(self, n: int) -> int:
        memo = [-1] * (n+1)
        return self.dp(memo, n)
    def dp(self, memo, n):
        if n==0 or n==1:
            return n
        if memo[n] !=-1:
            return memo[n]
        memo[n] = self.dp(memo, n-1) + self.dp(memo, n-2)
        return memo[n]

    # 直接写memo
    def fib(self, n: int) -> int:
        memo = {0:0,1:1}

        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

