#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30201
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    普通解法，用一个hashset
    注意：
    1. 判断节点相同应当用node对象，不能用值
    2. 不推荐使用while 1:
        无限循环，必须依赖内部逻辑手动跳出（return），容易漏写或顺序错乱；
        if p is None不安全，如果需要访问p.val，可能报错
    """
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        hs = set()
        p = head
        while 1:
            """
            if p.val in hs:
                return True
            # 错：值可能重复，不适合判断环
            应该直接使用节点对象
            """
            if p in hs:
                return True
            if p is None:
                return False
            hs.add(p)
            p = p.next

    # 更好的写法
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        hs = set()
        p = head
        while p:
            if p in hs:  # 用节点对象本身判断是否访问过
                return True
            hs.add(p)
            p = p.next
        return False

    """
    高级解法：配合快慢指针
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        """
        可以写成：
        1. p1 = p2 = head
        2. p1, p2 = head, head
        """
        while p1 and p1.next:
            """
            等同于：while fast is not None and fast.next is not None:
            """
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False
    

        
        


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

