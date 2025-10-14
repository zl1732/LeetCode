#
# @lc app=leetcode.cn id=528 lang=python3
# @lcpr version=30203
#
# [528] 按权重随机选择
#

# @lc code=start
class Solution:
    """
    前缀和 + 随机数 + 左边界/右边界
    """
    def __init__(self, w: List[int]):
        # 构建前缀和
        n = len(w)
        self.preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.preSum[i] = self.preSum[i-1] + w[i-1]


    def pickIndex(self) -> int:
        # 左边界，则总找到大于等于target,（0,2]
        # 右边界，则总找到小于等于target, [0,2)
 
        import random
        # target = random.randint(1, self.preSum[-1])
        # return self.left_bound(self.preSum, target) - 1
        target = random.randint(0, self.preSum[-1]-1)
        return self.right_bound(self.preSum, target)

    
    def left_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def right_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end



#
# @lcpr case=start
# ["Solution","pickIndex"]\n[[[1]],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]\n[[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#

