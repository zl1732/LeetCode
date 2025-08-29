#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30202
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        
        # dp[i][j] 表示前 i 个数能否组成和为 j 的方案数
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        # base case：不选任何数，组成 0 的方案数为 1（空集）
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]  # 不选 nums[i-1]
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选 nums[i-1]
        
        return dp[n][target] > 0
    

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = [0] * (target + 1)
    dp[0] = 1  # 空集凑出 0 的方法有一种

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]
    
    return dp[target] > 0


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # 和为奇数时，不可能划分成两个和相等的集合
        if total_sum % 2 != 0:
            return False
        n = len(nums)
        target = total_sum // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # base case
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足，不能装入第 i 个物品
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或不装入背包
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        
        return dp[n][target]
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

