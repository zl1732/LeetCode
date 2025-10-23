#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30203
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        
        cur = head
        for i in range(len(st)//2):
            node = st.pop()
            next = cur.next
            cur.next = node
            node.next = next
            cur = next
        
        """
        防止环
        """
        cur.next = None
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        
        cur = head
        while cur:
            node = st.pop()
            next = cur.next
            if node == next or node.next == next:
            # if node == next or node == cur:
                # print(node.val, next.val, node.next.val,cur.val)
                node.next = None
                break
            cur.next = node
            node.next = next
            cur= next
            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

