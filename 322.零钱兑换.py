#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30201
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        # top down
        self.memo = {}
        return self.dp(coins, amount)
    
    def dp1(self,coins, amount):
        # base case
        if amount < 0:
            return -1
        if amount ==0:
            return 0
        # 查表
        if amount in self.memo:
            return self.memo[amount]
        
        res = float('inf')
        for coin in coins:
            # sub problem
            subProblem = self.dp(coins, amount-coin)
            if subProblem == -1:
                continue
            res = min(res, subProblem+1)
        self.memo[amount] = res if res!=float('inf') else -1
        return self.memo[amount]
    
    """
    dp 数组中的值都初始化为 amount + 1:
        凑成 amount 金额的硬币数最多只可能等于 amount（全用 1 元面值的硬币），
        所以初始化为 amount + 1 就相当于初始化为正无穷，便于后续取最小值。
    
    为啥不直接初始化为 int 型的最大值 Integer.MAX_VALUE 呢？
        因为后面有 dp[i - coin] + 1，这就会导致整型溢出。
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        """
        有可能根本到不了：
        """
        #return dp[amount]
        return -1 if dp[amount] == amount + 1 else dp[amount]


# @lc code=end


"""
对比518题 求组合方式总数

🔍 为什么这个只用 memo[amount] 就够了？
因为这个问题不关心组合数、不关心路径结构，只关心：
    对于金额 amount，最少需要多少枚硬币？

✅ 所以：只要当前剩余金额 amount 一样，不管你从哪个路径来的，最优解总是一样的。

    换句话说：子问题的结果 dp(amount) 是唯一且确定的；

    所以你可以用一个 memo[amount] 来剪枝缓存。

❌ 为什么 518 不行？
因为 518 要求的是：
    有多少种“组合方式”可以组成 amount，硬币无限用，组合顺序不计重复
    如果只记录 dp[amount]，那就会重复统计一些路径

        🎯 什么是“重复统计”？
            coins = [1, 2]
            amount = 3
            所有可能的硬币组合（顺序不重要）是：
                [1,1,1]
                [1,2]
                [2,1] ← ⚠️ 这和 [1,2] 是同一种组合，不能重复计数！

        ✅ 怎么避免这种重复？
            我们需要“固定组合的选择顺序”，比如：
                永远从左到右选 coins（即：选过 coin[i] 后只能继续选 coin[i] 及之后的）
                用 start 参数限制递归从当前位置之后开始枚举
            这样 [2,1] 就不会被选出来（因为 1 在 2 的左边）

    你需要通过 start 参数控制组合不能重复（比如 [2,1] 和 [1,2] 不能重复计）
    所以必须加一个币种起点：memo[(amount, start)]
    
✅ 再对比一下 322：
coins = [1, 2]
amount = 3
你只在乎哪一个最少（比如 2 个硬币就能凑出 3
    不管 [2,1] 和 [1,2] 哪个先走，只要它用了 2 枚，都是最优；
    所以对于 amount=3，只需要 memo[3] = 最小硬币数，不关心它怎么来的，不会重复计数；

🎯 补充一个小口诀
    “求最值”类问题 → 状态只由资源量决定（如 amount）
    “求方案数”类问题 → 状态需额外控制路径合法性（如 start）
"""


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

