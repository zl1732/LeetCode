#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30201
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-2)
        dummy.next = head
        p2 = dummy
        p1 = head

        while p1 is not None:
            # 如果当前节点是重复段的起点
            if p1 and p1.val == p2.val:
                dup_val = p1.val
                # 跳过所有这个值的节点
                """
                需要.val，一定要检测p1 not none
                """
                while p1 and p1.val == dup_val:
                    p1 = p1.next
                # 删除整个重复段
                p2.next = p1
            else:
                # 当前值是唯一的，保留
                p2 = p2.next
                p1 = p1.next
 
        return dummy.next
    
# labuladong
# 对比LC26题的解法写的
# 唯一的区别是把数组赋值操作变成操作指针而已
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow, fast = head, head
        while fast is not None:
            if fast.val != slow.val:
                # nums[slow] = nums[fast];
                slow.next = fast
                # slow++;
                slow = slow.next
            # fast++
            fast = fast.next
        # 断开与后面重复元素的连接
        slow.next = None
        return head



# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

