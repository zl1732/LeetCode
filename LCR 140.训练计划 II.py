#
# @lc app=leetcode.cn id=LCR 140 lang=python3
# @lcpr version=30201
#
# [LCR 140] 训练计划 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan1(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        """
        two pointer, 还是先走cnt步，后面再走
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy

        for i in range(cnt+1):
            p1 = p1.next
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2.next


    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        """
        two pointer, 还是先走cnt步，后面再走
        """
        p1 = p2 = head

        for i in range(cnt):
            p1 = p1.next
        
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2
    
"""
💡💡💡
Leetcode 19 要删除倒数第 n 个节点，所以你需要找前一个节点（p2）来跳过它；
Leetcode LCR 140（训练计划）是找倒数第 n 个节点本身，直接返回 p2 即可，不需要管它的前一个是谁。

| 点                   | Leetcode 19                    | LCR 140            |
| -----------------   | -----------------------------   | ------------------ |
| 操作目标              | 删除倒数第 n 个节点               | 返回倒数第 n 个节点        |
| 是否要访问前驱         | ✅ 需要 `p2.next = p2.next.next`| ❌ 不需要              |
| p1 走 n 步后为 None 时| 要特殊处理（说明删的是第一个节点）   | 不处理，直接返回 `head` 即可 |
| dummy node          | ✅ 推荐使用                      | ❌ 不需要              |

"""
# @lc code=end



#
# @lcpr case=start
# [2,4,7,8]\n1\n
# @lcpr case=end

#

