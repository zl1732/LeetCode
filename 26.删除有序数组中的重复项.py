#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30201
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    """
    用了83题的思路，不是最好的解
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return []

        n = len(nums)
        slow = 0
        fast = 1

        while fast < n:
            if nums[slow] == nums[fast]:
                dup_val = nums[fast]
                # 跳过整个重复段
                while fast < n and nums[fast] == dup_val:
                    fast += 1
                if fast < n:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1

        return slow + 1




# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

