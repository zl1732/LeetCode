#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30203
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1,2,1,3,5,6,4]
        如果mid比左边大，上坡
        如果mid比左边小，下坡
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
        return left

"""
1. 为什么比较mid mid-1会卡住：
    这里比较的是 mid 与 mid+1，永远不会越界，因为：
    循环条件是 left < right
    所以 mid < right
    自然 mid+1 <= right ✅

    这就是这题选择 “右邻居比较” 的数学保证。

🕳️ 坑 2：left, right = 0, len(nums) 导致单元素越界
    如果你写成：
    left, right = 0, len(nums)

    再加上同样的比较：
    nums[mid] > nums[mid+1]

    💥 问题：mid+1 可能会越界。
    举个例子：
    nums = [1]
    初始化：
    left = 0, right = 1
    mid = 0 + (1-0)//2 = 0
    访问 nums[mid+1] = nums[1] ❌越界
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            
            # 获取左右邻居值，越界时视作 -∞
            left_val = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right_val = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            
            # 判断是否为峰
            if nums[mid] > left_val and nums[mid] > right_val:
                return mid
            elif nums[mid] < right_val:   # 上坡，往右
                left = mid + 1
            else:                         # 下坡，往左
                right = mid - 1

"""
while left < right → 收敛型二分（无需判断峰，最优模板）
逼近区间

while left <= right → 搜索型二分（要判断峰条件）
目标是找 target 的确切位置；

| 逻辑类型 | 典型题目                  | 循环条件                  | 思想          | 终止返回               |
| ---- | --------------------- | --------------------- | ----------- | ------------------ |
| 搜索型  | 34.在排序数组中查找元素的第一个位置   | `while left <= right` | 找一个确切满足条件的点 | 在循环内判断并 return     |
| 收敛型  | 162.寻找峰值 / 852.山脉数组峰顶 | `while left < right`  | 区间收敛，单调收缩   | 循环结束时返回 left/right |

"""

# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

