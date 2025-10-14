#
# @lc app=leetcode.cn id=81 lang=python3
# @lcpr version=30203
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 83.05 % of python3 submissions (17.9 MB)
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right- left )//2
            if nums[mid] == target:
                return True
            
            # 处理重复
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # 左侧有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return False
    


    def search1(self, nums: List[int], target: int) -> bool:
        """
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 5.24 % of python3 submissions (18.2 MB)
        """
        left, right = 0, len(nums) -1
        while left <= right:
            # 另一种去重逻辑
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            mid = left + (right- left )//2
            if nums[mid] == target:
                return True

            # 左侧有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return False

"""
# 为什么需要去重：
    因为无法判断实际是否有序，可能会跳过转轴
    以为“左半有序”，
    但其实旋转点在里面。

举例说明：
    [1,0,1,1,1]
    Answer	Expected Answer
    false	true

Step 1
    left = 0, right = 4
    mid = 2
    nums[mid] = 1
    nums[left] = 1, nums[right] = 1

进入判断：
    if nums[mid] >= nums[left]:  # 1 >= 1 → True
    → 算法认为 “左半区 [0..2] 有序”。

接下来：
    if nums[left] <= target < nums[mid]:  # 1 <= 0 < 1 → False
    else:
        left = mid + 1 = 3

⚠️ 问题出现了：
    算法认为目标不在左边，
    把 left 移到了 3，
    于是把真正包含 target = 0 的那一段 [0,1] 直接丢掉了。
"""    
# @lc code=end



#
# @lcpr case=start
# [2,5,6,0,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,5,6,0,0,1,2]\n3\n
# @lcpr case=end

#

