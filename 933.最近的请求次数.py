#
# @lc app=leetcode.cn id=933 lang=python3
# @lcpr version=30203
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:
    """
    维护的队列前端可能单次删除多个元素，不是只删除一个
    例如：
        [642],[1849],[4921]
    前两个都要删除
    """
    from collections import deque
    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        self.window.append(t)
        while self.window[0] < t-3000:
            self.window.popleft()
        return len(self.window)
            
from queue import Queue
class RecentCounter:
    def __init__(self):
        self.q = Queue()
    def ping(self, t: int) -> int:
        self.q.put(t)
        while self.q.queue[0] < t - 3000:
            self.q.get()
        return self.q.qsize()

"""
对比deque queue 

🧱 一、collections.deque（单线程 / 算法常用）

    from collections import deque
    dq = deque()           # 创建队列

    dq.append(1)           # 从右侧入队  → [1]
    dq.append(2)           # [1, 2]
    dq.appendleft(0)       # 从左侧入队 → [0, 1, 2]

    x = dq.popleft()       # 从左侧出队  → 返回 0
    y = dq.pop()           # 从右侧出队  → 返回 2

    n = len(dq)            # 当前长度（等价于 len(list)）
    print(n)               # 1

    dq.clear()             # 清空队列

    ✅ 没有阻塞行为，速度快。


⚙️ 二、queue.Queue（线程安全 / 多线程任务队列）

    from queue import Queue
    q = Queue(maxsize=5)   # 创建队列，可设最大容量

    q.put(1)               # 入队（如果满则阻塞）
    q.put(2)

    x = q.get()            # 出队（如果空则阻塞）
    print(x)               # 1

    size = q.qsize()       # 当前队列长度
    print(size)            # 1

    q.empty()              # 判断是否为空 → True/False
    q.full()               # 判断是否已满 → True/False

    # 标记任务完成（配合多线程 task_done/join 使用）
    q.task_done()
    q.join()               # 等待队列中所有任务完成

    ✅ 默认是线程安全的。
    ✅ 内部有锁，单线程性能比 deque 慢一点。
    ✅ 用于生产者–消费者模型。

    
🧩 Multi-thread (use Queue):
    
    from queue import Queue
    import threading

    q = Queue()

    def worker():
        while True:
            item = q.get()
            print(f"Processing {item}")
            q.task_done() 📢

    threading.Thread(target=worker, daemon=True).start()

    for i in range(3):
        q.put(i)
    q.join() 📢
"""  


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end



#
# @lcpr case=start
# ["RecentCounter", "ping", "ping", "ping", "ping"]\n[[], [1], [100], [3001], [3002]]\n
# @lcpr case=end

#

