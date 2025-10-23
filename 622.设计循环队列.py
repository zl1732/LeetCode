#
# @lc app=leetcode.cn id=622 lang=python3
# @lcpr version=30203
#
# [622] 设计循环队列
#

# @lc code=start
from collections import deque
# 底层用数组实现队列
class ArrayQueue:
    INIT_CAPACITY = 2

    def __init__(self, init_cap=INIT_CAPACITY):
        self.size = 0
        self.data = [None] * init_cap
        self.first = 0
        self.last = 0

    def enqueue(self, e):
        # 拓容
        if self.size == len(self.data):
            self.resize(self.size * 2)
        self.data[self.last] = e
        self.last += 1
        if self.last == len(self.data):
            self.last = 0
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue underflow')
        # 缩容
        if self.size == len(self.data) // 4:
            self.resize(len(self.data) // 2)

        old_val = self.data[self.first]
        self.data[self.first] = None
        self.first += 1
        if self.first == len(self.data):
            self.first = 0

        self.size -= 1
        return old_val

    def resize(self, new_cap):
        temp = [None] * new_cap

        # first ----- last
        # --- last    first ---

        for i in range(self.size):
            temp[i] = self.data[(self.first + i) % len(self.data)]

        self.first = 0
        self.last = self.size
        self.data = temp

    # 查
    def peek_first(self):
        if self.is_empty():
            raise Exception('Queue underflow')
        return self.data[self.first]

    def peek_last(self):
        if self.is_empty():
            raise Exception('Queue underflow')
        if self.last == 0:
            return self.data[len(self.data) - 1]
        return self.data[self.last - 1]

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0



class ArrayQueue:
    """Circular queue where 'last' points to the LAST valid element."""

    INIT_CAPACITY = 4

    def __init__(self, init_capacity=INIT_CAPACITY):
        self.data = [None] * init_capacity
        self.first = 0       # 指向队首元素
        self.last = -1       # 指向最后一个有效元素（初始为空）
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    # ---- 入队 ----
    def enqueue(self, e):
        if self.size == len(self.data):
            self._resize(len(self.data) * 2)

        # 注意：先移动指针，再写入元素
        self.last = (self.last + 1) % len(self.data)
        self.data[self.last] = e
        self.size += 1

    # ---- 出队 ----
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")

        old_val = self.data[self.first]
        self.data[self.first] = None
        self.first = (self.first + 1) % len(self.data)
        self.size -= 1

        # ---- 缩容 ----
        if 0 < self.size == len(self.data) // 4:
            self._resize(len(self.data) // 2)

        # ---- 当队列被清空时的可选重置 ----
        # 这一段不是为了“功能正确性”，而是为了让状态语义更干净。
        # 理论上，即使删除这三行，程序也能完全正确运行：
        #   - 因为 enqueue() 会在旧的 last 基础上 +1 再写入；
        #   - 所有出队、peek 操作都会先检查 is_empty()；
        #   - 所以不会有实际越界或逻辑错误。
        #
        # 但从“语义纯洁性”角度看，如果队列为空，
        # 我们希望保持 “last 指向最后一个有效元素” 这一不变式。
        # 此时 size=0 时已无有效元素，若不重置，last 仍指向旧位置（语义不一致）。
        # 因此这里选择在清空时复位 first/last：
        if self.size == 0:
            self.first = 0
            self.last = -1

        return old_val

    # ---- 辅助操作 ----
    def peek_first(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self.data[self.first]

    def peek_last(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self.data[self.last]

    # ---- 扩缩容 ----
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[(self.first + i) % len(self.data)]

        self.data = temp
        self.first = 0
        self.last = self.size - 1  # 注意这里，last 永远指向最后一个有效元素

    def __repr__(self):
        return f"ArrayQueue(data={self.data}, first={self.first}, last={self.last}, size={self.size})"




class MyCircularQueue:

    def __init__(self, k):
        self.q = ArrayQueue(k)
        self.max_cap = k

    def enQueue(self, value):
        if self.q.size == self.max_cap:
            return False
        self.q.enqueue(value)
        return True

    def deQueue(self):
        if self.q.is_empty():
            return False
        self.q.dequeue()
        return True
    
    def Front(self):
        if self.q.is_empty():
            return -1
        return self.q.peek_first()

    def Rear(self):
        if self.q.is_empty():
            return -1
        return self.q.peek_last()

    def isEmpty(self):
        return self.q.is_empty()

    def isFull(self):
        return self.q.size == self.max_cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end



