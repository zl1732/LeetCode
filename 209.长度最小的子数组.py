#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30203
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:

    #  这个应该是找刚好等于target的解法
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        left = 0
        min_len = float('inf')
        for right, num in enumerate(nums):
            window += num
            while window > target:
                window -= nums[left]
                left += 1

            if window == target:
                min_len = min(min_len, right-left+1)


        return min_len if min_len!=float('inf') else 0
    """
    拓展：（== target）
    🔹 有负数：「前缀和 + 哈希表」
    有负数时为什么会出问题？
        如果 nums 里有负数，window 就不再单调。
        右移 right 后，window 可能变小。
        收缩 left 后，window 也可能变大。

    
    # 「前缀和 + 哈希表」
    def minSubArrayLen(nums, target):
        preSum = 0
        seen = {0: -1}  # preSum -> 最早出现的下标
        min_len = float('inf')

        for i, num in enumerate(nums):
            preSum += num
            if preSum - target in seen:  # 找到一个子数组
                min_len = min(min_len, i - seen[preSum - target])
            if preSum not in seen:       # 只存最早出现的下标
                seen[preSum] = i

        return 0 if min_len == float('inf') else min_len

    """

    # >= target
    # 正确写法
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        left = 0
        min_len = float('inf')
        for right, num in enumerate(nums):
            window += num
            while window >= target:
                window -= nums[left]
                min_len = min(min_len, right-left+1)
                left += 1
                
        return min_len if min_len!=float('inf') else 0



    # 错误写法
    """
    11 12 9993 0
    12 13 9904 0
    13 14 8819 0
    14 15 1231 0
    15 16 6309 0

    下面这个方法的问题在于：
    最后一轮 走到 15 16，left += 1执行完，
    while left < right不会再执行了，但是其实16 16这一轮才是解

    """
    def minOperations(nums, x) -> int:
        # 用 window 记sum
        window = 0
        target = sum(nums) - x
        max_len = -1
        left = right = 0 
        
        while right < len(nums):
            num = nums[right]
            right += 1
            window += num
            while left < right and window >= target:
                # print(left, right,window, target)
                if window == target:
                    max_len = max(max_len,right - left)
                # 左移动
                num = nums[left]
                window -= num
                left += 1
        return -1 if max_len == -1 else len(nums) - max_len



"""
拓展
关于如果是原始题意，即大于等于，而非大于，为什么就不好用前缀和+哈希表了、

🔹 525 题
连续子数组的和能被 k 整除吗？

形式化：
    (preSum[j] - preSum[i]) % k == 0

关键点：
- 只要余数相等即可。
- 这是一个「相等关系」问题，可以直接用哈希表解决。
- 哈希表存的是「某个余数最早出现的下标」。
- 查询复杂度 O(1)。

🔹 209 题
连续子数组的和 ≥ target，最短长度是多少？

形式化：
    preSum[r] - preSum[l] >= target

关键点：
- 这不是「等于」，而是「大于等于」。
- 我们要找的是「所有 ≤ 某个值的 preSum 中，最靠右的一个」。
- 这是一个范围查询（≤），哈希表不适合。
- 因为 preSum 单调递增（nums 全是正数），可以用二分查找。

🔑 为什么需要二分？
- 对于每个右端点 r，需要找到最右的 l，使：
    preSum[l] <= preSum[r] - target
- 这个操作正好是二分能完成的。
- 时间复杂度 O(n log n)。

🔎 举例
nums = [2,3,1,2,4,3], target = 7
preSum = [0,2,5,6,8,12,15]

当 r=5 (preSum=12)，需要 preSum[l] <= 12 - 7 = 5
候选有 [0,2,5]，最靠右的是 5 → l=2
子数组长度 = r - l = 5 - 2 = 3

👉 这个「找 ≤ 某个值的最右位置」就是二分的作用。

🔹 如果用哈希表存 preSum
- seen = {preSum: index}
- 只能检查「某个值是否存在」：比如 preSum[r] - target
- 但 209 需要的是「范围 ≤」的最优解，哈希表无能为力。

✅ 总结
- 525 题：相等条件 → 哈希表能搞定。
- 209 题：大于等于条件 → 要做范围查询 → 用二分（或单调队列）。
- 如果坚持用哈希表，只能解「== target」，而不是「≥ target」。
"""

    
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

