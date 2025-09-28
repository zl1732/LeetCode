#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30203
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    """
    方法1： 跳过第一个元素
    这里可以从if nums[fast] == nums[slow]起手，因为跳过了第一个元素
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        count = 1  # 第一个数已经放进去了
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                if count < 2:  # 允许最多两个
                    slow += 1
                    nums[slow] = nums[fast]
                    count += 1
                # 否则超过 2 个，直接跳过
            else:
                # 遇到新数
                slow += 1
                nums[slow] = nums[fast]
                count = 1  # 新数重新计数
        return slow + 1



"""
微妙差别：
方法一就像「慢指针 slow 是一个筛子口，我每次要问：fast 这个球能不能进？」
逻辑：
    slow 始终指向结果数组的最后一个元素。
    拿当前 fast 位置的数和 slow 对比：
    一样 → 说明是重复数。
    不一样 → 说明遇到新数。
    指针关系：比较的是 结果数组末尾 和 当前扫描位置。

方法二就像「我盯着原数组看，和前一个比，不一样就是新球，相同就数次数」
逻辑：
    直接比较 原数组里相邻两个数。
    如果不一样 → 说明是新数；
    如果一样 → 就看次数 count。
    指针关系：比较的是 原数组相邻元素。
    优势：实现直观，不需要依赖 slow 来判断新旧，只看当前和前一个。
"""


class Solution:
    """
    方法2： 不跳过第一个元素
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        count = 0  # 当前数字计数，从0开始
    
        for fast in range(len(nums)):
            if fast == 0:
                nums[slow] = nums[fast]
                slow += 1
                count = 1
                continue

            # fast-1：比较的是 原数组里相邻两个元素。
            # slow-1：比较的是 结果数组最后一个元素。
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
                count = 1
                continue

            if count < 2:
                nums[slow] = nums[fast]
                slow += 1
                count += 1
                continue

            # 情况 4: 重复元素且已经 >= 2 次，直接跳过
            # 什么都不做
        return slow
    

class Solution:
    """
    方法3： 不跳过第一个元素

    为什么先写 if nums[fast] != nums[slow]:
        
    因为一开始 slow = fast = 0：

        第一次循环时，nums[fast] == nums[slow] → 不会进第一个 if。
        但 slow < fast 也不成立（0 < 0 为假），所以第二个分支也不会走。
        接着 fast += 1，count += 1，下一次循环才真正开始处理。
        也就是说：第一个元素天然保留，不用写任何逻辑。
    """
    # ✅
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        slow = fast = 0
        count = 0
        while fast < len(nums):
            if nums[fast]!=nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count += 1 # 先“临时的加一”；在循环结尾，再根据 new != old 来判断是否遇到新数，然后重置 count = 0。
            else: # 相等
                if slow < fast and count < 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    count += 1
            old = nums[fast]
            fast += 1
            new = nums[fast]
            if fast < len(nums) and new != old:
                count = 0
        return slow + 1           

    #❌❌❌❌❌❌❌
    def removeDuplicates(self, nums):
        if len(nums) ==0:
            return 0
        slow = fast = 0
        count =0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count = 1 # 👉 初始 fast=0, slow=0, count=0 时，第一个元素还没被正确计数，到第二个相等元素时，count 其实落后一拍，导致第 3 个相同元素还能再被放进去
            else:
                if slow < fast and count<2:
                    slow += 1
                    nums[slow] = nums[fast]
                    count+= 1
            fast += 1
        return slow + 1







class Solution2:
    """
    因为数组有序，所以可以这样
    [1,2,3,3] [1,1,2,3] [1,1,1,2]
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        k = 2  # 前两个可以直接保留
        for i in range(2, n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

