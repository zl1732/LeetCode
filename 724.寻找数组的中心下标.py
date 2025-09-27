#
# @lc app=leetcode.cn id=724 lang=python3
# @lcpr version=30203
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)+1
        preSum = [0] * n
        for i in range(1, n):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        """注意这里的逻辑"""
        for i in range(n-1):
            left = preSum[i]
            right = preSum[-1] - preSum[i+1]
            if left == right:
                return i
        return -1
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1, 7, 3, 6, 5, 6]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, -1]\n
# @lcpr case=end

#

