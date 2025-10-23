#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30203
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    """
    用两个栈，一个正常的，一个记录到每个为止的最小值
    4 2 6 1 9
    4 2 2 1 1
    """
    def __init__(self):
        self.st =[]
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        # 更新min_st
        """
        第一次push时会出错 self.min_st[-1]
        """
        # new_min = min(val, self.min_st[-1])
        if not self.min_st:
            self.min_st.append(val)
        else:
            new_min = min(val, self.min_st[-1])
            self.min_st.append(new_min)

    def pop(self) -> None:
        self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]
    
    def getMin(self) -> int:
        return self.min_st[-1]
        


    """
    优化，第二个栈只在出现更小的值时才记录
    4 2 6 1 9
    4 2 1
    pop 的时候先和最小值比较，如果是最小值，才更新min_st
    4 2 6 1 (9)
    4 2 1

    4 2 6 (1)
    4 2 (1)

    4 2 6
    4 2
    """
    def __init__(self):
        self.st =[]
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st:
            self.min_st.append(val)
        else:
            """
            不能用 < 必须用 <=
                st = [4, 2, 2]
                min_st = [4, 2]

                弹出时，lastVal = 2, lastMin = 2 → min_st.pop()
            结果：
                st = [4, 2]
                min_st = [4]
                这时 getMin() 返回 4 ❌
            """
            # if val < self.min_st[-1]:
            if val <= self.min_st[-1]:
                self.min_st.append(val)

    def pop(self) -> None:
        lastVal = self.st.pop()
        lastMin = self.min_st[-1]
        if lastVal == lastMin:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]
    
    def getMin(self) -> int:
        return self.min_st[-1]
        




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

