#
# @lc app=leetcode.cn id=LCR 184 lang=python3
# @lcpr version=30203
#
# [LCR 184] 设计自助结算系统
#

# @lc code=start
class Checkout:
    from collections import deque
    def __init__(self):
        self.maxq = deque()
        self.nums = deque()

    def get_max(self) -> int:
        return -1 if not self.maxq else self.maxq[0]
        

    def add(self, value: int) -> None:
        while self.maxq and value > self.maxq[-1]:
            self.maxq.pop()
        self.maxq.append(value)

        # 原始序列
        self.nums.append(value)
        

    def remove(self) -> int:
        if not self.nums:
            return -1
        else:
            val = self.nums.popleft()
            """
            get_max() 调用时最好不要再递归调用自身；
            """
            # if val == self.get_max():
            if val == self.maxq[0]:
                self.maxq.popleft()
        return val


        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
# @lc code=end



#
# @lcpr case=start
# ["Checkout","add","add","get_max","remove","get_max"]\n[[],[4],[7],[],[],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["Checkout","remove","get_max"]\n[[],[],[]]\n
# @lcpr case=end

#

