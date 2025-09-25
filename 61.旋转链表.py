#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30203
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        思路同151
        先分两段，分别反转
        然后整体反转
        """
        if not head or not head.next or k == 0:
            return head
    
         # 1. 计算长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 2. 找到切分点（n-k 位置）
        k %= n
        cut = head
        for _ in range(n - k - 1):
            cut = cut.next

        second = cut.next
        cut.next = None   # 断开
        
        # 分别反转
        n1 = self.reverseList(head)
        n2 = self.reverseList(second)

        # 连接两段
        """不需要prev，直接用while tail.next就行"""
        # prev, cur = None, n1
        # while cur:
        #     prev = cur
        #     cur = cur.next
        # prev.next = n2

        tail = n1
        while tail.next:
            tail = tail.next
        tail.next = n2

        # 整体反转
        return self.reverseList(n1)
        
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next   # 先保存下一个节点
            curr.next = prev  # 翻转指针
            prev = curr       # prev 前进
            curr = nxt        # curr 前进
        return prev
    

class Solution1:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. 计算链表长度
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        # 2. 找到新尾巴位置 (n-k-1)
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # 3. 重新链接
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

