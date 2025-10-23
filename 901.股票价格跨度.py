#
# @lc app=leetcode.cn id=901 lang=python3
# @lcpr version=30203
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner:
    """
    类似每日温度
    但是问题是：next一个一个录入的，也就要转换为 找下一个更大大于等于值的距离

    正序 找下一个大于等于
    倒序 找上一个更小 ??

    注意，要一直往前找到最远的一个最小值
    [60],[70],[60],[75]  75 -> 60 不是70
    """
    def __init__(self):
        self.prices = []
        self.st = []
        self.i = 0

    def next(self, price: int) -> int:
        # 70 60 
        days = 1
        while self.st and price >= self.prices[self.st[-1][0]]:
            # 找到最小的i
            idx, prev_days = self.st.pop()
            # days = self.i - idx + 1
            days = self.i - idx + prev_days


        # 更新 stack
        self.st.append([self.i, days])

        # 更新 i
        self.i += 1

        # 更新原始序列
        self.prices.append(price)
        return days

 
# gpt
"""
为什么不需要记录i
注意在while里面他是复返直接更新span
比如：
# 70, 60, 80
   1  1   1
到 80 时: stack = [(70, 1), (60, 1)]
分别pop, 然后span会加两次1，变成3
"""
class StockSpanner:
    def __init__(self):
        self.st = []  # [(price, span)]
        
    def next(self, price: int) -> int:
        span = 1
        # 只要栈顶价格 <= 当前价格，都可以被“合并”
        while self.st and self.st[-1][0] <= price:
            span += self.st.pop()[1]
        self.st.append((price, span))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end



#
# @lcpr case=start
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]\n[[], [100], [], [60], [70], [60], [75], [85]]\n
# @lcpr case=end

#

