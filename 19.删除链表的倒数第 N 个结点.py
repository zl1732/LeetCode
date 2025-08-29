#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30201
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    处理corner case有问题
    总结：
        创建的新链表都从dummy开始
        游走指针从head开始


| 使用场景                   | 是否用 dummy？          | 说明                         |
| -----------------         | -----------------     | -------------------------- |
| ✅ 需要在任意位置插入/删除    | ✔️ dummy 很有用        | dummy.next 永远指向当前“实际头”，更稳健 |              |
| ✅ 多指针交错操作，链表可能为空| ✔️ 更推荐 dummy        | 避免空指针判断混乱                  |

    """
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = head
        p2 = head

        for i in range(n):
            p1 = p1.next

        """
        p1 = head
        p2 = head
        如果这么写，需要自行加上边界处理
        因为执行完上面的之后， 可能已经在末尾，即n=长度
        """
        # 如果 p1 已经是 None，说明要删的是第一个节点
        if p1 is None:
            return head.next  # 相当于跳过第一个节点
        
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        
        # 删除
        p2.next = p2.next.next

        return dummy.next


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy

        """
        如果从dummy开始，就需要n+1
        """
        for i in range(n+1):
            p1 = p1.next

        # # 如果 p1 已经是 None，说明要删的是第一个节点
        # if p1 is None:
        #     return head.next  # 相当于跳过第一个节点
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        
        # 删除
        p2.next = p2.next.next

        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

