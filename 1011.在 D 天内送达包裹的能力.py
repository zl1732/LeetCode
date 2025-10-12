#
# @lc app=leetcode.cn id=1011 lang=python3
# @lcpr version=30203
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
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
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

