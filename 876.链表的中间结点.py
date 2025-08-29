#
# @lc app=leetcode.cn id=876 lang=python3
# @lcpr version=30201
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    x is None or x.next is None ✅
    x is None and x.next is None ❌
    x is not None and x.next is not None ✅
    x is not None or x.next is not None ❌
    🧠 一句话口诀：
    要访问 .next，必须先确保节点本身存在
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        # ❌
        while p1.next is not None or p1.next.next is not None:
            p1 = p1.next.next
            p2 = p2.next

        return p2.next
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        while p1.next is not None and p1.next.next is not None:
            p1 = p1.next.next
            p2 = p2.next
        return p2.next
    
    """
    1 - 2 - 3 - N
    1 - 2 - 3 - 4 - N
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

