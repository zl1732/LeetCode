#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30203
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedList
        
        window = SortedList()
        for i in range(len(nums)):
            # 为了防止 i == j，所以在扩大窗口之前先判断是否有符合题意的索引对 (i, j)
            # 查找略大于 nums[i] 的那个元素
            pos = window.bisect_left(nums[i])
            if pos < len(window) and window[pos] - nums[i] <= t:
                return True
            # 查找略小于 nums[i] 的那个元素
            if pos > 0 and nums[i] - window[pos - 1] <= t:
                return True

            # 扩大窗口
            window.add(nums[i])

            if len(window) > k:
                # 缩小窗口
                window.remove(nums[i - k])

        return False


import bisect
from typing import List
class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k <= 0:
            return False

        window = []  # 保持有序，长度 ≤ k
        for i, x in enumerate(nums):
            # 找到 >= x - t 的最小下标
            pos = bisect.bisect_left(window, x - t)
            # 如果这个位置存在，且值 ≤ x + t，则满足
            if pos < len(window) and window[pos] <= x + t:
                return True

            # 插入 x
            bisect.insort(window, x)

            # 窗口超界，移除 nums[i-k]
            if i >= k:
                # 二分定位并删除
                rm = nums[i - k]
                idx = bisect.bisect_left(window, rm)
                # 这里一定能找到对应值（因为一进一出）
                window.pop(idx)

        return False
  


"""
LeetCode 220. Contains Duplicate III
------------------------------------
【解题思路】

题目要求：
判断数组中是否存在一对 (i, j)，使得：
    |i - j| <= k  且  |nums[i] - nums[j]| <= t

思路：
我们维护一个大小不超过 k 的「滑动窗口」，并保证窗口内的元素是**有序的**。
这样对于当前元素 x = nums[i]，只需要在窗口中找出与它最接近的数，
检查差值是否 ≤ t 即可。

具体做法：
1. 使用有序表（SortedList）维护最近 k 个元素；
2. 对每个 nums[i]：
   - 在有序表中用二分找到 >= nums[i] 的第一个元素，检查是否差 ≤ t；
   - 再看左边的邻居（小于 nums[i] 的最大值）是否差 ≤ t；
3. 插入 nums[i]；
4. 若窗口超过 k，则移除 nums[i - k]。

复杂度：
- 时间复杂度：O(n log k)
- 空间复杂度：O(k)
"""

"""
【SortedList vs bisect+list 库对比】

1️⃣ SortedList（来自 sortedcontainers）
   - 内部实现为分块平衡结构（chunked list）
   - 插入、删除、二分查找均为 O(log n)
   - 性能稳定，代码简洁，功能完备（支持 add/remove/bisect 等）
   - 类似于 C++ 的 std::multiset / TreeSet

2️⃣ bisect + list（Python 标准库）
   - bisect 仅提供“查找插入位置”的二分函数
   - 实际插入或删除 list 元素需要移动后续元素 → O(k)
   - 适合小规模数据（k 很小），大 k 时性能急剧下降
   - 无平衡逻辑，需要手动维护顺序和删除操作

✅ 结论：
   - 面试 / 实战推荐使用 SortedList（清晰且高效）
   - 若不能安装第三方库，再退回 bisect 手写版
"""
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#
