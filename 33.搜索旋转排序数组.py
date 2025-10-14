#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30203
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums)
    #     while left < right:
    #         mid = left + (right -left) //2
    #         print(left, right, mid, target)
    #         # 如果target在mid左边,
    #         if nums[left] < target <= nums[mid]:
    #             right = mid
    #         # 如果target在左半边,
    #         elif nums[mid] < target <= nums[right]:
    #             left = mid + 1
    #         elif nums[mid] > nums[left]:
    #             left = mid + 1
    #         elif nums[mid] <= nums[right]:
    #             right = mid
    #         # print(left, right, mid, target)
    #     if right == len(nums):
    #         return -1
    #     return right if nums[right] == target else -1
    
    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right: # 右闭区间
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 左半边有序
            if nums[left] <= nums[mid]:
                # target 在左半边
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半边有序
            # elif nums[mid] <= nums[right]: 无重复可以这样
            else: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 右开区间
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 左半边有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid  # 因为右开，所以直接取 mid，不减 1
                else:
                    left = mid + 1

            # 右半边有序
            else:
                if nums[mid] < target <= nums[right - 1]:  # 注意这里必须用 right-1
                    left = mid + 1
                else:
                    right = mid
        return -1
    



    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            # 先检测是不是target
            if nums[mid] ==  target:
                return mid
            
            # 检测左侧有序还是右侧有序
            if nums[mid] >= nums[left]: # 左侧有序
                # target 位置检测
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    """
                    elif target > nums[mid] 这样写不完整！！
                    左半边 [4,7] 有序；target=0 < nums[left]=4 → 两个分支都不满足
                    """
                #elif target > nums[mid]:
                else:
                    left = mid + 1
            
            elif nums[mid] <= nums[right]:
            # else:
                # target 位置检测
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                    





# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

