#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30203
#
# [220] 存在重复元素 III
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        window = SortedList()
        for i, x in enumerate(nums):
            # 1️⃣ 填充阶段：先把窗口凑齐 k 个元素
            if i + 1 < k:
                window.add(x)
                continue
            
            # 2️⃣ 检查当前 x 是否满足差值条件
            pos = window.bisect_left(x)
            if pos < len(window) and window[pos] - x <= t:
                return True
            if pos > 0 and x - window[pos - 1] <= t:
                return True

            # 3️⃣ 更新窗口
            window.add(x)
            if i >= k:
                window.remove(nums[i - k])
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        window = SortedList()
        for i, x in enumerate(nums):
            """
            注意题干：
                abs(i - j) <= indexDiff
                abs(nums[i] - nums[j]) <= valueDiff

            也就是从第一个开始就可以和第二个比较，无需等到第k个再比
            所以无需预填充window！！！
            
            举例说明：
                [-5,5,5,5,5,15] 6 6
                正确答案之所以是 True，是因为索引 1 和 2 的两个 5 已经满足：
                |5 - 5| = 0 ≤ 6
                |2 - 1| = 1 ≤ 6
                但你的代码在 i=1..4 期间都 continue（只加不查），直到 i=5 才开始查，这时拿 x=15 去比，当然查不出前面 5 和 5 的那对，于是误判 False。
            """
            # if i + 1 < k:
            #     window.add(x)
            #     continue
            # 搜索第一个>= x的位置
            pos = window.bisect_left(x)
            if pos <= len(window)-1 and window[pos] - x <=t:
                return True
            if pos > 0 and x - window[pos-1] <= t:
                return True
            
            # 更新窗口
            """
            要删的应该是最早滑出窗口的那个旧元素,而不是最小值
            例如：[10, 1, 20, 2, 30] 
            window = [1, 10, 20]  ← 有序，但最旧的是 10
            
            此时如果你用 pop(0) 删掉 1，
            实际上删掉的是“最小值”而不是“最旧元素”，
            逻辑错误 ❌。

            所以，不能用 pop(0) 替代 remove(nums[i - k])，
            """
            # window.add(x)
            # if len(window) >= k:
            #     window.pop(0)
            window.add(x)
            if i >= k:
                window.remove(nums[i - k])
        return False
# @lc code=end


from bisect import bisect_left, bisect_right, insort
class Solution2:
    def containsNearbyAlmostDuplicate(nums, k, t):
        window = []
        for i, x in enumerate(nums):
            # case 1: 找到略大于等于 x 的元素，检查差值 <= t
            pos = bisect_left(window, x)
            if pos < len(window) and window[pos] - x <= t:
                return True

            # case 2: 找到略小于 x 的元素（pos-1），检查差值 <= t
            if pos > 0 and window[pos - 1] - x <= t:
                return True

            # 插入当前元素
            insort(window, x)

            # 保持窗口大小 <= k
            if i >= k:
                rm = nums[i - k]
                idx = bisect_left(window, rm)
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




#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#
