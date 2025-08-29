#
# @lc app=leetcode.cn id=518 lang=python3
# @lcpr version=30202
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.res = 0
        self.coins = coins
        self.memo_fail = set()  # 只记录失败位置
        self.dfs(amount, 0, 0)
        return self.res

    def dfs(self, amount: str, i: int, start: int) -> bool:
        if i == amount:
            self.res += 1
            return True
        """
        memo_fail 只用 i 作为 key，剪枝过严
        你把所有从某个已失败的金额 i 开始的路径都剪掉，但实际上同一个 i 在不同的 start 下可能有不同的出路。
        需要把 (i, start) 一起作为剪枝的 key，才能更精确地记“从金额 i 且剩余币种索引 ≥ start 时是失败的”。
        
        为什么140可以这么剪枝
            ✅ 140 题中：
            同一个位置 i，只要记住是否能从 i 出发成功划分整个字符串就够了。
            所以只需用 i 做 key 存 memo[i] = False 就能剪枝。

            特性：
            对于位置 i：
                如果从 i 出发，所有子字符串都不能被分词，那从 i 开始的路径永远失败；
                不管是谁调用 dp(i)，结果都一样。
            所以 memo[i] 只需要依赖 i，是“无额外状态”的。

            关键：对于同一个位置 i，无论是哪个递归路径走到 i，它后面的所有结果都是一样的。

        
        为什么518不能这样剪枝
            ❌ 518 题中：
            同一个金额 curr，如果当前可选币种起点 start 不一样，结果也可能不一样。
            所以不能只用 curr 剪枝，而是必须记住 (curr, start)。

            关键：LeetCode 518 中，是否能凑出金额 i，不仅取决于金额 i，还取决于你允许使用哪些硬币（也就是 start 位置）
            
            ✅ 更直观的例子
            coins = [1, 2, 5]，amount = 5：
            如果你从 curr=3 出发：
                当 start=0，你可以选 1，再选 1，合法。
                当 start=2，只能用 5，就超额了。
            所以你不能只用 curr=3 剪枝！

        | 问题                | 是否能只用一个 index 作为剪枝 key？ | 解释            |
        | ------------------ | -----------------------------   | ------------- |
        | 140 Word Break II  | ✅ 可以只用 `i`                   | 状态只依赖当前位置     |
        | 518 Coin Change II | ❌ 需要 `(curr, start)`          | 状态依赖金额和剩余币种范围 |

        ✅ 所以剪枝成立的充要条件是：
        子问题的结果只和 i 有关，不依赖前面路径的其他选择。
        """
        # if i in self.memo_fail:
        #     return False

        success = False
        for start in range(start, len(self.coins)):
            coin = self.coins[start]
            if i + coin <= amount:
                """
                start + 1❎
                这样就把下次搜索的 start 往后移了一位，禁止重复使用当前币种。
                """
                if self.dfs(amount, i + coin, start):  # 尽管成功，也继续尝试其它组合
                    success = True

        if not success:
            self.memo_fail.add(i)  # 剪枝：这个位置起步的路径全失败

        return success
    
"""
依然通过不了时间限制，这个题不是用回溯解法
14/30 cases passed (N/A)
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.res = 0
        self.coins = coins
        self.memo_fail = set()  # 记录失败的 (i, start) 状态
        self.dfs(amount, 0, 0)
        return self.res

    def dfs(self, amount: int, i: int, start: int) -> bool:
        if i == amount:
            self.res += 1
            return True
        # 改为2元组
        if (i, start) in self.memo_fail or i > amount:
            return False

        success = False
        for idx in range(start, len(self.coins)):
            coin = self.coins[idx]
            if i + coin <= amount:
                # 允许重复使用当前 coin，所以仍然传 idx
                if self.dfs(amount, i + coin, idx):
                    success = True

        if not success:
            self.memo_fail.add((i, start))  # 精确剪枝：当前状态无解

        return success

"""
GPT答案 29/30 cases passed (N/A)
区别一：返回值结构 vs 全局计数器结构
✅ 我的写法：
一旦 dfs(3, 0) 算出返回值 3，就可以直接缓存复用，所有遇到 (3, 0) 的分支都直接拿结果，不会再递归下去。

❌ 你的写法：
你虽然也用了 memo_fail，但剪枝逻辑是：
    只要某个路径没有任何一种成功方式，你才会记录失败；
    一旦有一种成功路径，你还会继续尝试所有其它可能；
    所以即使 (i, start) 你走过一次成功路径了，下次你还会重新再走一遍，无法复用计数结果。

✅ 区别二：剪枝粒度不一样
我的写法用 memo[(remain, start)] = ways 来剪枝，是无论调用者是谁，直接复用计数结果；
你的写法用 self.memo_fail.add((i, start))，只能剪掉“必然失败的路径”，但不能剪掉“虽然成功但没必要再走的路径”。


"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(remain: int, start: int) -> int:
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            if (remain, start) in memo:
                return memo[(remain, start)]

            ways = 0
            for i in range(start, len(coins)):
                ways += dfs(remain - coins[i], i)  # 可重复使用当前币种

            memo[(remain, start)] = ways
            return ways

        return dfs(amount, 0)



"""
使用完全背包思路：

dp[i][j] = 使用前 i 个硬币，凑出金额 j 的组合数
注意事项：
    i 从 0 到 n，表示前 i 个硬币（第 i 个是 coins[i-1]）
    j 从 0 到 amount，表示金额

✅ 状态转移方程讲解（关键）
dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
我自己理解： dp[i-1][j]的意思是不用新的（第i个）硬币，继续用前面的硬币拼出j的这部分解法
           dp[i][j - coins[i-1]] 加了新的硬币i，但是j - coins[i-1]的意思：新硬币面值coins[i-1]
           即 dp[i][目标总额 - 新硬币面值]，即 dp[i-1][目标总额 - 新硬币面值] ❌❌ 这是错的 ❌❌

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
✅ 正确理解 dp[i][j - coins[i-1]] 是：
    允许在构造 [0, j - coins[i-1]] 这个金额的过程中使用 coins[i-1]”
    dp[i][j - coins[i-1]] 是允许 coins[i-1] 在整个构造过程中重复出现的
    它可能已经用了这个硬币，现在又再用一枚来构造 j

❌ 而 dp[i-1][j - coins[i-1]] 的含义是：
    在[0, j - coins[i-1]], 没用 coins[i-1]，直到这次才用一次
    所以这是 0-1 背包的行为：只允许 coins[i-1] 出现一次（当前这次）


✅ 你总结得非常好，我把你的原话稍作润色，供你保存：
    原来我误以为 dp[i][j - coins[i-1]] 是“我刚刚加了一个 coins[i-1]”，
    但其实它更重要的含义是：“我在构造 j - coins[i-1] 的过程中就可以多次使用 coins[i-1]，而不是只在最后加一次”。
    所以 dp[i][j - coins[i-1]] 是允许 coins[i-1] 出现在整个构造过程中任意位置的；
    而 dp[i-1][j - coins[i-1]] 才是那种“前面完全不准用 coins[i-1]，直到这次才用一次”的行为，这才是 0-1 背包的含义。


🧠 一个直觉图示：
以 coins = [1, 2]，amount = 4 为例：
    dp[1][4] 表示：用前 1 个硬币（也就是只用 1 元）凑出 4：
        可以：1+1+1+1，所以 dp[1][4] = 1
    dp[2][4] 表示：用前 2 个硬币（1 元和 2 元）凑出 4：
        不用 2 元 → dp[1][4] = 1
        用 2 元 → dp[2][2] = 2（2+2 或 1+1+2）
→ 所以 dp[2][4] = dp[1][4] + dp[2][2] = 1 + 2 = 3


dp[1][6] = dp[0][6] + dp[1][4]
        = 0 + dp[1][4]
              ↳ = dp[0][4] + dp[1][2]
                     ↳ = dp[0][2] + dp[1][0]
                            ↳ = dp[0][0] = 1

你从 dp[1][0] 一路“递推”过来，每次都是加一个 2，其实就等于你在考虑加1个、2个、3个硬币！

✅ 所以只需要加一次的原因：
    每个子状态会“滚动地”把前面的情况一层层推过来，等效于穷举了所有用 n 个当前硬币的情况！

你在更新 dp[i][j] 的时候，加了 dp[i][j - coin]，而这个 dp[i][j - coin] 本身已经包括：
    用了 1 个 coin 的组合
    用了 2 个 coin 的组合
    用了更多 coin 的组合…

"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) # n个硬币
        dp = [[0] * (amount+1) for _ in range(n+1)]

        # base case
        # amount=0 都有一种方法
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                # coin amount current
                cur_coin = coins[i-1]
                # 超重,只能不放
                if cur_coin > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 完全背包，不用硬币+用硬币
                    dp[i][j] = dp[i-1][j] + dp[i][j-cur_coin]
        return dp[n][amount]

    # 压缩数组
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case：凑出 0 的方法只有 1 种（啥都不取）

        for i in range(1, n + 1):  # 遍历硬币种类
            coin = coins[i - 1]
            for j in range(1, amount + 1):  # 金额从 coin 到 amount（正序）
                if coin > i:
                    continue
                else:
                    dp[j] = dp[j] + dp[j - coin]  # 完全背包：可以重复选，所以仍然是 dp[j] += ...

        return dp[amount]

  
    # 压缩数组
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

# @lc code=end



#
# @lcpr case=start
# 5\n[1, 2, 5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#

