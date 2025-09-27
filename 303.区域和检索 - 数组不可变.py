#
# @lc app=leetcode.cn id=303 lang=python3
# @lcpr version=30203
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums) + 1
        self.preSum = [0]*n
        for i in range(1, n):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        """
        # 注意这里 right 要 +1，因为前缀和是 [0..n]
        """
        return self.preSum[right+1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end



#
# @lcpr case=start
# ["NumArray", "sumRange", "sumRange", "sumRange"]\n[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]\n
# @lcpr case=end

#

