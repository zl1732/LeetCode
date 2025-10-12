#
# @lc app=leetcode.cn id=LCR 172 lang=python3
# @lcpr version=30203
#
# [LCR 172] 统计目标成绩的出现次数
#

# @lc code=start
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        left = self.searchLeft(scores, target)
        right = self.searchRight(scores, target)
        if left ==-1 or right == -1:
            return 0
        return right-left + 1
    
    def searchLeft(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left >= len(nums):
            return -1
        return left if nums[left] == target else -1
    
    def searchRight(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                left = mid + 1 # 只改了这一句
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right < 0:
            return -1
        return right if nums[right] == target else -1

# @lc code=end



#
# @lcpr case=start
# [2, 2, 3, 4, 4, 4, 5, 6, 6, 8]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 5, 7, 9]\n6\n
# @lcpr case=end

#

