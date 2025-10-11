#
# @lc app=leetcode.cn id=852 lang=python3
# @lcpr version=30203
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] > nums[mid+1]:  #>= 左平峰
                right = mid
            elif nums[mid] < nums[mid+1]:#<= 右平峰
                left = mid+1
        return left
    

# @lc code=end



#
# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,10,5,2]\n
# @lcpr case=end

#

