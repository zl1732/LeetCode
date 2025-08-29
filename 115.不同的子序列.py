#
# @lc app=leetcode.cn id=115 lang=python3
# @lcpr version=30201
#
# [115] 不同的子序列
#

"""
## 从排列问题理解， t就是盒子，s就是球
视角一，从 t 的视角穷举
我们的原问题是求 s[0..] 的所有子序列中 t[0..] 出现的次数，那么可以先看 t[0] 在 s 中的什么位置，假设 s[2], s[6] 是字符 t[0]，那么原问题转化成了在 s[3..] 和 s[7..] 的所有子序列中计算 t[1..] 出现的次数。

写成比较偏数学的形式就是状态转移方程：

// 定义：s[i..] 的子序列中 t[j..] 出现的次数为 dp(s, i, t, j)
dp(s, i, t, j) = SUM( dp(s, k + 1, t, j + 1) where k >= i and s[k] == t[j] )

（首先，你可以站在盒子的视角，每个盒子必然要选择一个球。
这样，第一个盒子可以选择 n 个球中的任意一个，然后你需要让剩下 k - 1 个盒子在 n - 1 个球中选择（这就是子问题 P(n - 1, k - 1)）：
）


视角二，从 s 的视角穷举
我们的原问题是计算 s[0..] 的所有子序列中 t[0..] 出现的次数，可以先看看 s[0] 是否能匹配 t[0]，如果不匹配，那没得说，原问题就可以转化为计算 s[1..] 的所有子序列中 t[0..] 出现的次数；

但如果 s[0] 可以匹配 t[0]，那么又有两种情况，这两种情况是累加的关系：

1、让 s[0] 匹配 t[0]，那么原问题转化为在 s[1..] 的所有子序列中计算 t[1..] 出现的次数。

2、不让 s[0] 匹配 t[0]，那么原问题转化为在 s[1..] 的所有子序列中计算 t[0..] 出现的次数。

为啥明明 s[0] 可以匹配 t[0]，还不让它俩匹配呢？主要是为了给 s[0] 之后的元素匹配的机会，比如 s = "aab", t = "ab"，就有两种匹配方式：a_b 和 _ab。

（另外，你也可以站在球的视角，因为并不是每个球都会被装进盒子，所以球的视角分两种情况：
1、第一个球可以不装进盒子，这样的话你就需要将剩下 n - 1 个球放入 k 个盒子。
2、第一个球可以装进盒子，这样的话你就需要将剩下 n - 1 个球放入 k - 1 个盒子。
结合上述两种情况，可以得到：
注意组合和前面排列的区别，因为组合不考虑顺序，所以球选择装进盒子时，只有一种选择，而不是 k 种不同选择，所以 C(n-1, k-1) 不用乘 k。）
"""


"""
✅ 什么是 @lru_cache(None)？

它是 Python 标准库 functools 中的装饰器，用于自动为递归函数加上缓存功能（记忆化）。

完整写法：

from functools import lru_cache

@lru_cache(None)  # None 表示缓存无限大
def dp(i, j):
    ...

它的作用跟你手动写 self.memo = {} 类似，但更干净优雅。
"""

class Solution:
    """
    ✅ 解法一：递归 + 记忆化（从 t 的角度出发）
    📌 思路概述（你说的视角一）：
    我们从 t[j] 出发，在 s[i:] 中找到所有等于 t[j] 的位置 k，然后从 s[k+1:] 匹配 t[j+1:]。
    """
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        n, m = len(s), len(t)

        @lru_cache(None)
        def dp(i, j):
            # t 匹配完了
            # 表示这个路径是一个合法的完整匹配，为整个方案数 +1。
            if j == m:
                return 1
            # s 匹配完了但 t 还没
            if i == n:
                return 0
            # 提前剪枝
            # # base case 2
            # if len(s) - i < len(t) - j:
            #     return 0

            res = 0
            for k in range(i, n):
                if s[k] == t[j]:
                    res += dp(k + 1, j + 1)
            return res

        return dp(0, 0)

    """
    ✅ 解法二：自顶向下（从 s 的角度穷举，带记忆化）
    📌 思路概述（你说的视角二）：
    枚举每个 s[i] 是不是要匹配当前的 t[j]：
        不匹配：dp(i+1, j)
        匹配：dp(i+1, j+1)
    """
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache
        n, m = len(s), len(t)

        @lru_cache(None)
        def dp(i, j):
            if j == m: return 1  # t 匹配完了
            if i == n: return 0  # s 匹配完了但 t 还没

            if s[i] == t[j]:
                # 两种选择：匹配 or 跳过
                return dp(i+1, j+1) + dp(i+1, j)
            else:
                # 跳过 s[i]
                return dp(i+1, j)

        return dp(0, 0)

    """
    ✅ 自底向上 dp
    和递归写法一一对应：
        如果 s[i-1] == t[j-1]，我们有两种选择：
            匹配它：dp[i-1][j-1]
            不匹配它：dp[i-1][j]
        所以：
            dp[i][j] = dp[i−1][j−1] + dp[i−1][j]
            dp[i][j] = dp[i−1][j−1] + dp[i−1][j]

        如果 s[i-1] != t[j-1]，我们只能跳过当前字符：
            dp[i][j] = dp[i−1][j]
            dp[i][j] = dp[i−1][j]
    初始化
        dp[0][0] = 1：空串匹配空串
        dp[i][0] = 1：任何前缀的 s 都能匹配空的 t（只有一种方法）
        dp[0][j > 0] = 0：空的 s 无法匹配非空的 t
    """
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1  # 空串 t 匹配方式是 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]
    
    """
    ✅ 五、空间优化到一维（滚动数组）
    因为状态只依赖于上一行，所以我们可以用一维数组，从右往左更新避免覆盖：
    """
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # 注意倒序更新
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]


# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 初始化备忘录为特殊值 -1
        self.memo = {}
        return self.dp(s, 0, t, 0)
    
    def dp(self, s, i ,t, j):
        m, n =len(s), len(t)
        # t完全匹配，方案数量+1
        if j == n:
            return 1
        # s的长度不够匹配t了/s走完了，t没完全匹配
        # 没成功，+0
        # if i == m:
        if m-i<n-j:
            return 0
        """ 查备忘录防止冗余计算 """
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = 0
        # 递归
        # 一个位置一个位置轮着找，如果第一位匹配，就往后一个一个匹配
        # 对比小球的：for循环=选出第一个球（n种），只是这里有顺序要求，n转换为for循环+判断首字符相同
        for k in range(i, len(s)):
            if s[i] == t[j]:
                # 第一个球入盒，开始找下一位，这里用到递归调用
                res += self.dp(s, i+1, t, j+1)
        self.memo[(i, j)] =res
        return res


    def dp(self, s, i ,t, j):
        m, n =len(s), len(t)
        # t完全匹配，方案数量+1
        if j == n:
            return 1
        # s的长度不够匹配t了/s走完了，t没完全匹配
        # 没成功，+0
        # if i == m:
        if m-i<n-j:
            return 0
        """ 查备忘录防止冗余计算 """
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = 0
        # 递归
        # 对应第二种方式，球的视角，第一个球（s）可入盒(t)，则找剩余，也可不入盒，则在剩余里重新找
        # 1. 入盒，p(n-1，k-1)*k 这里k即遍历s检测所有可入盒s[i] == t[j]的位置
        # 2. 不入盒，剩下 n - 1 个球放入 k 个盒子。s的位置+1
        # 注意：第一个球可入盒，在此处就是判断首字符相同
        if s[i] == t[j]:
            #             入盒                 不入盒
            res = self.dp(s, i+1, t, j+1) + self.dp(s, i+1, t, j)
        ##注意这里
        else:
            res = self.dp(s, i+1, t, j)
        self.memo[(i, j)] =res
        return res

# @lc code=end



#
# @lcpr case=start
# "rabbbit"\n"rabbit"\n
# @lcpr case=end

# @lcpr case=start
# "babgbag"\n"bag"\n
# @lcpr case=end

#

