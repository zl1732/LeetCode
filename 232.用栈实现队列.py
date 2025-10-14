#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30203
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    """
    双栈，a负责入栈，b负责出站
    push: to stack a
    ❌pop: first move to stack b, make sure no element remain in a, then pop a
    ❌peek: first move to stack b, make sure no element remain in a, then return first a
    empty: no b no a

    pop 和 peek 的逻辑有误！！！

    正确解读：b只用来跟踪队头：
        b 是队头的“缓存栈”，只在它空了的时候，才需要从 a 把新的元素倒进来刷新缓存。
        所以只要 b 不空，你永远可以直接用它的顶端（pop/peek）。
    
        当 b 空了，才说明之前的“老队头们”都被弹完了；
        这时才需要把 a 里还没出队的新元素倒过去，重新生成一个“新队头序列”。
    """

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x) 

    def pop(self) -> int:
        # first move all a to b,then pop
        self.peek()
        return self.b.pop()

    def peek(self) -> int:
        # move all a to b, then return first
        """
        先检查b是否已经空了
        """
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]
        
    def empty(self) -> bool:
        return not self.a and not self.b
        



class MyQueue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # 添加元素到队尾
    def push(self, x: int) -> None:
        self.s1.append(x)

    # 删除队头元素并返回
    def pop(self) -> int:
        # 先调用 peek 保证 s2 非空
        self.peek()
        return self.s2.pop()

    # 返回队头元素
    def peek(self) -> int:
        if not self.s2:
            # 把 s1 元素压入 s2
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # 判断队列是否为空
    def empty(self) -> bool:
        return not self.s1 and not self.s2
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyQueue", "push", "push", "peek", "pop", "empty"]\n[[], [1], [2], [], [], []]\n
# @lcpr case=end

#

