#
# @lc app=leetcode.cn id=581 lang=python3
# @lcpr version=30203
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        pass


# @lc code=end


class Solution_Stack:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = float('inf'), float('-inf')

        # ✅ 从左往右：单调递增栈（找 left）
        incr_stk = []
        for i in range(n):
            while incr_stk and nums[incr_stk[-1]] > nums[i]:
                # 当前值比栈顶小 → 打破单调递增
                left = min(left, incr_stk.pop())
            incr_stk.append(i)

        # ✅ 从右往左：单调递减栈（找 right）
        decr_stk = []
        for i in range(n - 1, -1, -1):
            while decr_stk and nums[decr_stk[-1]] < nums[i]:
                # 当前值比栈顶大 → 打破单调递减
                right = max(right, decr_stk.pop())
            decr_stk.append(i)

        return 0 if left == float('inf') else right - left + 1

class Solution_ImplicitStack:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1

        # ✅ 从右往左：隐式单调递增栈 → 找 left
        min_so_far = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > min_so_far:
                left = i  # 当前值比右边最小值大 → 破坏递增
            min_so_far = min(min_so_far, nums[i])

        # ✅ 从左往右：隐式单调递减栈 → 找 right
        max_so_far = float('-inf')
        for i in range(n):
            if nums[i] < max_so_far:
                right = i  # 当前值比左边最大值小 → 破坏递减
            max_so_far = max(max_so_far, nums[i])

        return 0 if right == -1 else right - left + 1


class Solution_Scanline:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1

        # 从左往右找 right（破坏递增）
        max_so_far = float('-inf')
        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_so_far:
                right = i

        # 从右往左找 left（破坏递减）
        min_so_far = float('inf')
        for i in range(n - 1, -1, -1):
            min_so_far = min(min_so_far, nums[i])
            if nums[i] > min_so_far:
                left = i

        return 0 if right == -1 else right - left + 1


# 显式单调栈（正序）找 left：从左→右维护单调递增栈

left = +inf; stk=[]
for i in range(n):
    while stk and nums[stk[-1]] > nums[i]:
        left = min(left, stk.pop())
    stk.append(i)


# 隐式反序栈（min_so_far，反序）找 left：从右→左维护“右侧最小值”

left = n; min_so_far = +inf
for i in range(n-1, -1, -1):
    if nums[i] > min_so_far: left = i
    min_so_far = min(min_so_far, nums[i])

#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

