#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30201
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列，最小堆(PriorityQueue)
        pq = []
        # 将 k 个链表的头结点加入最小堆
        for i, head in enumerate(lists):
            if head is not None:
                """
                避免比较 ListNode 对象抛出异常
                if writen as: heapq.heappush(pq, (head.val, head))
                一开始没问题，但当你遇到 两个节点 val 一样 时，heapq 会试图比较第二个元素（即两个 ListNode）：
                # 会报错：TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
                因为 Python 中的自定义对象（如 ListNode）没有默认的 < 操作符，无法排序。
                    * val 是排序的主依据
                    * i 是 tie-breaker（打破平局的工具），它是整数，可以比较
                    * head 是我们最终要用的
                    原始链表节点
                """
                heapq.heappush(pq, (head.val, i, head))
        
        while pq:
            # 获取最小节点，接到结果链表中
            val, i, node = heapq.heappop(pq)
            p.next = node
            p = p.next
            # if node.next:
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
        return dummy.next





class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for i, head in enumerate(lists):
            if head is not None:
                to_push = (head.val, i, head)
                heapq.heappush(pq, to_push)

        while pq:
            val, i, head = heapq.heappop(pq)
            p.next = head
            if head.next is not None:
                to_push = (head.next.val, i, head.next)
                heapq.heappush(pq, to_push)
            p = p.next
        
        return dummy.next


# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

