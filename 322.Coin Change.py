#
# @lc app=leetcode id=322 lang=python3
# @lcpr version=30201
#
# [322] Coin Change
#

"""
# 自顶向下递归的动态规划
def dp(状态1, 状态2, ...):
    for 选择 in 所有可能的选择:
        # 此时的状态已经因为做了选择而改变
        result = 求最值(result, dp(状态1, 状态2, ...))
    return result

# 伪码框架(顶向下)
def coinChange(coins: List[int], amount: int) -> int:
    # 题目要求的最终结果是 dp(amount)
    return dp(coins, amount)

# 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
def dp(coins: List[int], n: int) -> int:
    # 做选择，选择需要硬币最少的那个结果
    # 初始化res为正无穷
    res = float('inf')
    for coin in coins:
        res = min(res, sub_problem + 1)
    return res
    
    """
# @lc code=start
class Solution:
    """
    top down without memo
    """
    def coinChange1(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)
    
    def dp1(self, coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        # 要求最少
        res = float('inf')
        # 不同选择
        for coin in coins:
            # 计算子问题结果
            subProblem = self.dp(coins, amount-coin)
            # 子问题无解
            if subProblem == -1:
                continue
            res = min(res, subProblem+1)
        return res if res !=float('inf') else -1

    """
    ✅ 问题解释：
        你把 memo = {} 写在了 dp 函数的 内部，这意味着 每次递归调用 dp() 
        都会创建一个新的空 memo 字典，所有的记忆都无法保存！
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        """
        memo不能写在递归函数里
        """
        memo = {}
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        ## search 
        if amount in memo:
            return memo[amount]
        # 要求最少
        res = float('inf')
        # 不同选择
        for coin in coins:
            # 计算子问题结果
            subProblem = self.dp(coins, amount-coin)
            ## ensure not -1
            # 子问题无解
            if subProblem == -1:
                continue
            res = min(res, subProblem+1)
        memo[amount] = res if res !=float('inf') else -1
        return memo[amount]



    def coinChange(self, coins: List[int], amount: int) -> int:
        # 必须用全局变量
        self.memo = {}
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        ## search 
        if amount in self.memo:
            return self.memo[amount]
        # 要求最少
        res = float('inf')
        # 不同选择
        for coin in coins:
            # 计算子问题结果
            subProblem = self.dp(coins, amount-coin)
            ## ensure not -1
            # 子问题无解
            if subProblem == -1:
                continue
            res = min(res, subProblem+1)
        self.memo[amount] = res if res !=float('inf') else -1
        return self.memo[amount]


"""
动态规划，下往上
🔹 dp[2]：
用 1：2 - 1 = 1，dp[1] + 1 = 1 + 1 = 2
用 2：2 - 2 = 0，dp[0] + 1 = 0 + 1 = 1 ✅ 更优
用 5 不行

🔹 dp[3]：
1 → dp[2]+1 = 1+1 = 2
2 → dp[1]+1 = 1+1 = 2
5 不行

🔹 dp[4]：
1 → dp[3]+1 = 2+1 = 3
2 → dp[2]+1 = 1+1 = 2 ✅
5 不行

🔹 dp[5]：
1 → dp[4]+1 = 2+1 = 3
2 → dp[3]+1 = 2+1 = 3
5 → dp[0]+1 = 0+1 = 1 ✅

# 自底向上迭代的动态规划
# 初始化 base case
dp[0][0][...] = base case
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins: 
                # 子问题无解，跳过
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin]) 
        return -1 if dp[amount] == amount + 1 else dp[amount]




# @lc code=end



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

