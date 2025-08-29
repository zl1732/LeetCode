#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30201
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    """
    1. 固定使用dummy为虚拟节点的头部, dummy = ListNode(-1)
    2. use p as the moving pointer
    3. if two list given, use p1 and p2
    写错了❌
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        p = head
        while not head:
            if head.val < x:
                p1.next = p
                # ❌错误1：缺少p1 = p1.next
            else:
                p2.next = p
                # ❌错误1：缺少p2 = p2.next
            # ❌错误2：
            # 不能直接让 p 指针前进，会断开原链表中的每个节点的 next 指针
            p = p.next
        
        p1.next = dummy2.next
        return dummy1.next

class Solution:
    """
    标准答案：
    1. p1, p2 = dummy1, dummy2  参考写法

    2. 这三行代码的作用是：
        为了安全地将当前节点 p 从原链表中拆出来，
        并防止后续错误引用或链表成环。

        temp = p.next
        # 保存当前节点的下一个节点，防止断链后找不到它。

        p.next = None
        # 把当前节点从原链表中“剪下来”，让它成为一个独立节点，
        # 这样它可以被安全地加入新链表，不会带出原链表的尾部。
        🔍 为什么要让节点成为“独立节点”？
            ✅ 因为你正在重新组织链表结构 —— 把原链表“分裂”成两个新链表：
            原始链表： 3 → 5 → 2 → 6 → null
            x = 4
            目标结构：
                小链表：3 → 2
                大链表：5 → 6
                
            🧨 如果不让节点“独立”会发生什么？
            if p.val < x:
                p1.next = p
                p1 = p1.next # 没有断开 p.next!
            你刚把 p = [3 → 5 → 2 → 6] 接到小链表末尾，但它还拖着原链表的尾巴！
            那么你的小链表现在变成：
            dummy1 → 3 → 5 → 2 → 6 → ...
            你是不是只想把 3 加进去？但你不“剪断”（p.next = None），就会错误地连上整个尾巴。
            
            🔗 “成为独立节点”的意义是让节点不再引用原链表后续部分
            [3] → null ✅
            [3] → [5] → [2] → [6]  ❌
            这样你才能安全地说：“我只把这个 [3] 放进小链表。”
            否则你会意外地把整条链拖进去！

        p = temp
        # 移动指针，继续处理下一个节点。


        可以这样写比较逻辑清晰：
            temp = p.next
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            p.next = None
            p = temp

    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        # p1, p2 指针负责生成结果链表
        p1, p2 = dummy1, dummy2
        # p 负责遍历原链表，类似合并两个有序链表的逻辑
        # 这里是将一个链表分解成两个链表
        p = head
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让 p 指针前进，
            # 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp
        # 连接两个链表
        p1.next = dummy2.next

        return dummy1.next




# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

