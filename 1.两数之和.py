#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30203
#
# [1] 两数之和
#

# @lc code=start
"""
| 问题         | 总数           | 时间复杂度  |
| ---------- | ------------ | ------ |
| 所有子集       | 2^n          | O(2^n) |
| 全排列        | n!           | O(n!)  |
| 固定长度的 k 元组 | C(n,k) ≈ n^k | O(n^k) |

"""

class Solution:
    """
    标准普通写法
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i,num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []
        
    """
    双指针
    """
    
def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 先对数组排序
        nums.sort()
        res = []
        lo, hi = 0, len(nums)-1
        while lo<hi:
            sum = nums[lo] + nums[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                res.append([lo, hi])
                lo += 1
                hi -= 1
        return res


# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

