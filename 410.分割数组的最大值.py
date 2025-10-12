#
# @lc app=leetcode.cn id=410 lang=python3
# @lcpr version=30203
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.shipWithinDays(nums, k)

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left)//2
            if days < self.deliver(weights, mid):
                left = mid + 1
            else:
                right = mid
        return left


    def deliver(self, weights, x):
        days = 0
        cur = 0
        for w in weights:
            if cur + w > x:
                days += 1
                cur = w
            else:
                cur += w
        if cur:
            days += 1
        #print(weights, x, days)
        return days
    

# @lc code=end



#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,4]\n3\n
# @lcpr case=end

#

