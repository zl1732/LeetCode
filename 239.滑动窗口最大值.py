#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30203
#
# [239] 滑动窗口最大值
#

# @lc code=start
"""
用一个双端队列，维护单调性
"""
from collections import deque
class MonoQueue:
    def __init__(self):
        self.queue = deque()
    
    # 5 4 3 2
    def push(self, num):
        while self.queue and num > self.queue[-1]:
            self.queue.pop()
        self.queue.append(num)
    
    def max(self):
        return self.queue[0]
    
    # pop 输入特定值，判断是不是max值
    def pop(self, num):
        if num == self.max():
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = MonoQueue()
        res = []
        for i in range(n):
            num = nums[i]
            if i < k-1:
                # window.append(num)
                window.push(num)
            else:
                # 更新窗口
                # window.append(num)
                window.push(num)
                # 最大值
                # max_val = max(window)
                max_val = window.max()
                res.append(max_val)
                """ 这里应该pop 最前面的值，而不是max_val"""
                # window.pop(max_val)
                window.pop(nums[i-k+1])
        return res

# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

