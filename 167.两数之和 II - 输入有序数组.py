#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30201
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while lo<hi:
            curSum = numbers[lo] + numbers[hi]
            if lo < hi and curSum < target:
                lo += 1
            elif lo < hi and curSum > target:
                hi -= 1
            else:
                return [lo+1, hi+1]

        
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

