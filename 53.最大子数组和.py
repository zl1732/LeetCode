#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30201
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    """
    首先思考如何定义 dp
    1. nums[0..i] 中的「最大的子数组和」为 dp[i]。
        假设我们知道了 dp[i-1]，如何推导出 dp[i] 呢？
        答：不行的，因为子数组一定是连续的，按照我们当前 dp 数组定义，并不能保证 nums[0..i] 中的最大子数组与 nums[i+1] 是相邻的，也就没办法从 dp[i] 推导出 dp[i+1]。
           无法得到合适的状态转移方程
    
    2. 以 nums[i] 为结尾的「最大子数组和」为 dp[i]。
        状态转移关系：
        dp[i] 有两种「选择」，要么与前面的相邻子数组连接，形成一个和更大的子数组；要么不与前面的子数组连接，自成一派，自己作为一个子数组。
        # 要么自成一派，要么和前面的子数组合并
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        然后for loop一遍
    """
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        # 定义：dp[i] 记录以 nums[i] 为结尾的「最大子数组和」
        dp = [0] * n
        # base case
        # 第一个元素前面没有子数组
        dp[0] = nums[0]
        # 状态转移方程
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # 得到 nums 的最大子数组
        res = float('-inf')
        for i in range(n):
            res = max(res, dp[i])
        return res
    
    def maxSubArray(self, nums):
        n = len(nums)
        if n==0:
            return 0
        dp = [0] * n
        # base case
        '''
        这里写错了：以第 0 个元素结尾的最大子数组和”，它就只能是 nums[0]，不是 0。
        '''
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
        #return max(dp)
        # 手写max
        res = float('inf')
        for i in range(n):
            res = max(res, dp[i])
        return res
        
# 优化1
def maxSubArray(self, nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = nums[0]
    res = dp[0]  # 初始化最大值

    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        res = max(res, dp[i])  # 同时更新最大子数组和

    return res

# 优化2 o(1) 空间
def maxSubArray(self, nums):
    if not nums:
        return 0

    cur = res = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        res = max(res, cur)
    return res



# 单调队列
from collections import deque

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        # 单调队列维护最小前缀和
        q = deque()
        q.append(0)
        res = float('-inf')

        for i in range(1, n + 1):
            # 当前区间和 = preSum[i] - preSum[q[0]]
            res = max(res, preSum[i] - preSum[q[0]])

            # 保持队列递增（前缀和小的留着）
            while q and preSum[q[-1]] >= preSum[i]:
                q.pop()
            q.append(i)

        return res



# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

