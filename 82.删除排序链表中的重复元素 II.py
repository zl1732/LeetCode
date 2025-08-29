#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30201
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        注意：
            需要取值操作 p1.val 且为游走指针 即需要 p = p.next
            一定要检测p、p.next等非空！！！
        例：
            if p1 is not None and p1.val == p2.val:
                p1 = p1.next
        """
        dummy = ListNode(-1)
        dummy.next = head
        p2 = dummy
        p1 = head

        """
        LC83 答案
        """
        # while p1 is not None:
        #     # 如果当前节点是重复段的起点
        #     if p1 and p1.val == p2.val: # 先两个一块走，再检测
        #         dup_val = p1.val
        #         # 跳过所有这个值的节点
        #         while p1 and p1.val == dup_val:
        #             p1 = p1.next
        #         # 删除整个重复段
        #         p2.next = p1
        #     else:
        #         # 当前值是唯一的，保留
        #         p2 = p2.next
        #         p1 = p1.next
 
        # return dummy.next

        """
        本题 答案
        """
        while p1:
            # 如果当前节点是重复段的起点
            """
            例如这里p1.val == p1.next.val，用了 p1.next.val
            所以必须if p1.next is not None
            """
            if p1.next and p1.val == p1.next.val: # p1先往前多走一步
                dup_val = p1.val
                # 跳过所有这个值的节点
                while p1 and p1.val == dup_val:
                    p1 = p1.next
                # 删除整个重复段
                p2.next = p1
            else:
                # 当前值是唯一的，保留
                p2 = p2.next
                p1 = p1.next

        return dummy.next

"""
关键区别：
LC83: if p1 and p1.val == p2.val:
判断当前节点和前一个是否重复 + 	✅ 每组重复保留一个
LC82: if p1.next and p1.val == p1.next.val:
判断是否“进入重复段” + 全部删除重复节点

"""

# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

