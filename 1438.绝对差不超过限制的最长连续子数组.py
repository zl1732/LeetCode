#
# @lc app=leetcode.cn id=1438 lang=python3
# @lcpr version=30203
#
# [1438] 绝对差不超过限制的最长连续子数组
#

# @lc code=start
class MonotonicQueue:
    def __init__(self):
        # 常规队列，存储所有元素
        self.q = collections.deque()
        # 元素降序排列的单调队列，头部是最大值
        self.maxq = collections.deque()
        # 元素升序排列的单调队列，头部是最小值
        self.minq = collections.deque()

    def push(self, elem: int):
        # 维护常规队列，直接在队尾插入元素
        self.q.append(elem)

        # 维护 maxq，将小于 elem 的元素全部删除
        while self.maxq and self.maxq[-1] < elem:
            self.maxq.pop()
        self.maxq.append(elem)

        # 维护 minq，将大于 elem 的元素全部删除
        while self.minq and self.minq[-1] > elem:
            self.minq.pop()
        self.minq.append(elem)

    def max(self) -> int:
        # maxq 的头部是最大元素
        return self.maxq[0]

    def min(self) -> int:
        # minq 的头部是最大元素
        return self.minq[0]

    def pop(self) -> int:
        # 从标准队列头部弹出需要删除的元素
        deleteVal = self.q.popleft()

        # 由于 push 的时候会删除元素，deleteVal 可能已经被删掉了
        if deleteVal == self.maxq[0]:
            self.maxq.popleft()
        if deleteVal == self.minq[0]:
            self.minq.popleft()
        return deleteVal

    def size(self) -> int:
        # 标准队列的大小即是当前队列的大小
        return len(self.q)

    def isEmpty(self) -> bool:
        return not self.q
    

class Solution:
    """
    本题可用滑动窗口 + 双端队列
    右移窗口: 最大绝对差 <= limit, 记录最大值，最小值，
    缩小窗口: 最大绝对值 > limit, 从minq一个一个删除
    判断最大长度: 缩小窗口之后，计算max
    """
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = MonotonicQueue()
        left = right = 0
        n = len(nums)
        res = 0
        while right < n:
            window.push(nums[right])
            right += 1
            while left < right and window.max() - window.min() > limit:
                window.pop()
                left += 1
            # 这里不是 right - left + 1 因为right在前面已经+1
            res = max(res, right - left)
        return res

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = MonotonicQueue()
        left = right = 0
        n = len(nums)
        window_size = 0
        res = 0
        while right < n:
            window.push(nums[right])
            right += 1
            window_size += 1
            while window.max() - window.min() > limit:
                window.pop()
                left += 1
                window_size -= 1
            # 这里不是 right - left + 1 因为right在前面已经+1
            res = max(res, window_size)
        return res
                
# @lc code=end



#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

