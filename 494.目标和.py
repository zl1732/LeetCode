#
# @lc app=leetcode.cn id=494 lang=python3
# @lcpr version=30202
#
# [494] 目标和
#

# @lc code=start
""" 1. 
| 写法                             | 是否推荐   | 原因说明                  |
| ------------------------------ | ------ | --------------------- |
| `self.result = 0` 在函数内         | ✅ 推荐   | 每次调用函数都初始化，最安全        |
| `self.result = 0` 在 `__init__` | ⚠️ 有风险 | LeetCode 可能复用实例，导致脏数据 |
| `result = 0` 在类体里              | ❌ 错误   | 是类属性，所有实例共享，污染严重      |

"""

""" 2.
    backtrack(i + 1, current_sum + nums[i])
    backtrack(i + 1, current_sum - nums[i])
与
    remain += nums[i]
    self.backtrack(nums, i + 1, remain)
    remain -= nums[i]
    remain -= nums[i]
    self.backtrack(nums, i + 1, remain)
    remain += nums[i]

是否等价？

✅ 从语义上和最终效果上是等价的
❌ 但在编程风格和维护性上有区别

方式1：表达式传参	ßß
    - 无副作用
    - 更简洁
    - 推荐用于 Python 等函数式语言
方式2：修改+撤销	
    - 更贴近“回溯模板”
    - 适合需要记录路径（如组合问题）
    - 但更容易写错，维护成本略高
"""

class Solution:
    """
    暴力穷举
    Time Limit Exceeded
    73/142 cases passed (N/A)
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.result = 0
        self.backtrack(nums, 0, 0, target)
        return self.result
    
    def backtrack(self, nums, i, cur, target):
        # 找到
        """
        ❌ i==len(nums) and cur == target:
        这只能处理刚好满足条件的情况，如果 cur != target，程序仍然会进入 for x in [1,-1] 然后越界报错。
        ✅ 正确写法：应该在最前面判断 i 是否越界

        ❌ 如果不return 还会继续走i+1, 报IndexError
        ✅ 正确写法：最后必须return
        """
        # if i==len(nums) and cur == target:
        #     self.result += 1
        #     return
        if i == len(nums):
            if cur == target:
                self.result += 1
            return  # 关键！无论是否成功都必须 return
            
        for x in [1,-1]:
            num = nums[i] * x
            cur += num
            self.backtrack(nums, i+1, cur, target)
            cur -= num
        ## 也可以用这种写法
        #self.backtrack(i + 1, current_sum + nums[i])
        #self.backtrack(i + 1, current_sum - nums[i])

    """
    分解思路（动态规划）
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        self.res = 0
        return self.backtrack(nums, 0, 0, target)
    
    def backtrack(self, nums, i, cur, target):
        if i == len(nums):
            if cur == target:
                return 1
            return 0 # 注意这里的写法
        
        if (i, cur) in self.memo:
            return self.memo
        

        """
        以下代码还有几处错误：
        1. 不应该使用self.res
            会导致 memo 记录的是总结果，而不是当前子问题的结果
            错误在于：
            保存的是 self.res（全局累计值），而不是当前这个 backtrack(...) 调用返回的结果。
        假设：
            你第一次递归回来后 self.res = 3
            然后你又去计算另一个分支 backtrack(i+1, cur)，得到 2 个解
            你现在 self.res = 5
        你这时：
        self.memo[i, cur] = self.res
        把 memo[i, cur] 设成了 5 ❌
        但正确的是：
            这个 memo[i, cur] 的值应该是 这个 backtrack() 分支本身产生了几个方案，也就是 2，而不是全局已经累加到的 5
        ✅ 正确方式：
        单独用一个局部变量 res 表示这个子问题的结果，再存入 memo：

        res = 0
        for x in [1, -1]:
            res += self.backtrack(nums, i+1, cur + x * nums[i], target)
        self.memo[i, cur] = res  # 这才是当前子问题的解法数
        return res
        🚨 🚨 🚨 🚨 🚨 🚨 
        只要是**“分解问题”的思路（即带返回值的递归函数 + 记忆化搜索 / 动态规划），
        就应该避免使用全局变量来统计结果**，而是用返回值来收集子问题的结果。
        🚨 🚨 🚨 🚨 🚨 🚨 
        """
        for x in [1,-1]:
            num = nums[i] * x
            cur += num
            """
            为什么是**“两个递归结果相加”**？
            这其实触及了一个非常关键的动态规划和递归的底层逻辑：
                当一个问题可以拆分成多个子问题时，总方案数等于所有子问题的方案数之和。
            """
            self.res += self.backtrack(nums, i+1, cur, target)
            self.memo[i, cur] = self.res
            cur -= num
        

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.backtrack(nums, 0, 0, target)
    
    def backtrack(self, nums, i, cur, target):
        if i == len(nums):
            if cur == target:
                return 1
            return 0 # 注意这里的写法
        
        if (i, cur) in self.memo:
            return self.memo[(i, cur)]
        
        """
        强烈不建议手动回溯值，建议
        """
        result = 0
        for x in [1,-1]:
            num = nums[i] * x
            cur += num
            result += self.backtrack(nums, i+1, cur, target)
            """
            注意不要写错
            self.memo[i, cur] = result 错
            self.memo[(i, cur)] = result 对
            
            另外位置不对，应该是走完当前函数再记录，放到for外面
            """
            cur -= num
        self.memo[(i, cur)] = result

        """
        注意分解思路需要return result！！
        """
        return result


    """
    GPT 标准答案
    """
    def backtrack(self, nums, i, cur, target):
        if i == len(nums):
            return 1 if cur == target else 0

        if (i, cur) in self.memo:
            return self.memo[(i, cur)]

        # 两种选择：加当前数 or 减当前数
        add = self.backtrack(nums, i + 1, cur + nums[i], target)
        subtract = self.backtrack(nums, i + 1, cur - nums[i], target)
        result = add + subtract

        # 记入备忘录
        self.memo[(i, cur)] = result
        return result

# @lc code=end



#
# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

