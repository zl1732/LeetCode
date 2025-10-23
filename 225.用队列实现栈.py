#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30203
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    """
    用一个队列a记录，top_element记录栈顶
    [1,2,3,4]
    push: 贴到最后
    pop: 用deque模拟，注意只能popleft，把队头都pop到队尾
    """
    from collections import deque
    def __init__(self):
        self.a = deque()
        self.top_element = None
        
    def push(self, x: int) -> None:
        self.a.append(x)
        self.top_element = x

    def pop(self) -> int:
        size = len(self.a)
        # 保留队尾两个元素，先记录倒数第二个为新栈顶，然后pop最后一个
        # 如果只保留一个，pop之后会丢失新的栈顶
        for i in range(size-2):
            self.a.append(self.a.popleft())
        # 记录新栈顶
        self.top_element = self.a.popleft()
        self.a.append(self.top_element)
        # pop 栈顶
        return self.a.popleft()
        
    def top(self) -> int:
        return self.top_element
        
    def empty(self) -> bool:
        return not self.a
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyStack", "push", "push", "top", "pop", "empty"]\n[[], [1], [2], [], [], []]\n
# @lcpr case=end

#

