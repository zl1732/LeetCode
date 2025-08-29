#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30201
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        return slow

    """
    压缩代码， 观察到fast += 1都要执行，
    且前后顺序不影响（在nums[slow] = nums[fast]之后）
    """ 
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        

    """
    # 对比26题有序数组:

    ✅ 双指针写法中的顺序区别小结：
    📌 slow += 1 在前：
                slow += 1
                nums[slow] = nums[fast]
    👉 用于 有序数组去重（如 LeetCode 26）保留一个重复值

    📌 nums[slow] = nums[fast] 在前 — 常用于 删除特定值
                nums[slow] = nums[fast]
                slow += 1
    👉 用于 排除某些值（如 LeetCode 27）删除全部

    """
    # 对比26题有序数组
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0 
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                """
                注意这里是反着的，因为要保留一个
                """
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # 数组长度为索引 + 1
        return slow + 1
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

