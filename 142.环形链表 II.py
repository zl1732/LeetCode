#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30201
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    错误在于相遇的点不是环的起点
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return p1
        return None
    """
    链表非环部分长度为 a
    环起点到相遇点的距离为 b
    相遇时慢指针总共走了 a + b，快指针走了 2(a + b)
    快指针多走了一圈环长 r，即：2(a + b) = a + b + r => a = r - b
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            # 相遇了
            if p1 == p2:
                p3 = head
                """
                1. 建议以后不要写while 1：
                while p3 != p1:
                    p3 = p3.next
                    p1 = p1.next
                return p1  # 或 p3，环的起点

                2. 应该先判断，然后再移动p1, p3。可能初始就是起点
                    if p1 == p3:
                        return p1
                    p3 = p3.next
                    p1 = p1.next
                """
                while 1:
                    p3 = p3.next
                    p1 = p1.next
                    if p1 == p3:
                        return p1
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            # 相遇了
            if p1 == p2:
                p3 = head
                while p1 != p3:
                    p3 = p3.next
                    p1 = p1.next
                return p1
        return None

    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            # 相遇了
            if p1 == p2:
                break
        
        # 判断有无环
        """
        if p1.next is None or p1 is None:
        ⚠️ 这两者是不同的！
        上面这个会先判断短p1.next 但是如果p1已经是None，就报错了！！！
        if p1 is None or p1.next is None:
        
        if p1 or p1.next:
        这个判断逻辑是“只要 p1 或 p1.next 有值就进入”，和你想判断“是否是空”正好相反**。
        """
        if p1.next is None or p1 is None:
        # if p1 or p1.next:
            return None
        
        # 找环起点
        p3 = head
        while p1 != p3:
            p1 = p1.next
            p3 = p3.next
        return p1
    

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            # 相遇了
            if p1 == p2:
                break
        
        # 判断有无环
        if p1 is None or p1.next is None:
        # if not p1 or not p1.next:
            return None
        
        # 找环起点
        p3 = head
        while p1 != p3:
            p1 = p1.next
            p3 = p3.next
        return p1
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

