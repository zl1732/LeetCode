#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30201
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """

    1. 创建虚拟头结点dummy; p 是一个“游走指针”，用于逐步构建新链表
    2. 直接拼接已有节点，无需创建新节点：p.next = p2，而不是 ListNode(p2.val)
    3. 处理剩余部分，最多只会有一个链表还未合并完,所以不用 if p1 is not None and not p2
    4. 返回结果时，p已在最末尾，需要返回dummy
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建虚拟头结点，方便统一操作
        dummy = ListNode(-1)
        p = dummy  # p 是一个“游走指针”，用于逐步构建新链表
        p1 = l1
        p2 = l2

        while p1 is not None and p2 is not None:
            # 比较 p1 和 p2 两个指针的值
            if p1.val > p2.val:
                p.next = p2  # ✅ 直接拼接已有节点，无需创建新节点：p.next = p2，而不是 ListNode(p2.val)
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next  # p 指针向后移动，构建链表

        # 处理剩余部分，最多只会有一个链表还未合并完
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2

        return dummy.next  # ✅ 返回 dummy.next，跳过虚拟头节点，得到真正的合并链表头部

            

# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

