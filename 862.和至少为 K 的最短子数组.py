#
# @lc app=leetcode.cn id=862 lang=python3
# @lcpr version=30203
#
# [862] 和至少为 K 的最短子数组
#

# @lc code=start
class Solution:
    """
    注意这个题不能直接用原始序列 滑动窗口
    因为值有负数，所以必须用前缀和 + 双端队列 记录当前区间最小值的i
    然后移动left的时候，从队列中逐个找从小到大
    """
    def shortestSubarray(self, nums: List[int], k: int) -> int:
   
# @lc code=end





from collections import deque
class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        dq = deque()
        res = n + 1

        for j in range(n + 1):
            # 尝试从左端找能满足条件的 i
            while dq and prefix[j] - prefix[dq[0]] >= k:
                res = min(res, j - dq.popleft())

            # 保持前缀和递增
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(j)

        return res if res <= n else -1


#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

