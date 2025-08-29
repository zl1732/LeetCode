#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30201
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    你给的这个代码有个严重的逻辑错误：它修改了原始链表结构，这在面试或实际中是绝对不能接受的
    面试已经挂了宝贝儿
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 != p2:
            # A is shorter
            if not p1.next:
                """
                # ❗️篡改原始链表结构
                这会让原本没有交点的两个链表“被你强行制造了交点”，
                导致你之后的判断 while p1 != p2 变得毫无意义。

                链表A: 1 -> 2 -> 3
                链表B: 4 -> 5 -> 6
                
                两者本身并无交点。
                你这么写：
                    p1 走完了 1->2->3，到 3 时 p1.next = None，你就让它：
                
                3.next = headB（即 4）
                所以链表A 变成了：
                1 -> 2 -> 3
                          ↓
                          4 -> 5 -> 6
                
                在本题中：
                ❗️会形成环，然后p1,p2在环上互相追逐
                    headA: 1  →  2 - None
                                ↗
                    headB: 3 → 5 
                
                1. p1:1  p2:3
                2. p1:2  p2:5   
                3. p1:2.next = headB(3)  p2:2
                    headA: 1  →  2 - None
                               ↙   ↖
                    headB:   3   →   5 
                4. p1:3  p2:2
                5. p1:5  p2:3(2.next = 3（之前被改了）)
                6. p1:2  p2:5
                ...

                """
                p1.next = headB # ❗️篡改链表A，让它尾部接上链表B
            # B is shorter
            if not p2.next:
                p2.next = headA

            # move forward
            p1 = p1.next
            p2 = p2.next
        return p1
            
    """
    错错错：
    ❗️❗️游走指针.next = 原始链表的头❗️❗️
    
    无论是 p1 还是 p2，作为游走指针，它们只能自己“跳转”位置，
    绝不能通过 p1.next = ... 或 p2.next = ... 去“修路”改原链表结构。

    ✅ 正确指针行为是：
    指针自己跳，比如：
    if p1:
        p1 = p1.next
    else:
        p1 = headB

    这是说：“我自己换轨道走”，没有动任何链表。

| 写法               | 是否安全？| 是否修改结构？      |
| ----------------- | -----   | ------------ |
| `p1 = headB`      | ✅ 安全  | ❌ 没有改结构      |
| `p2 = p2.next`    | ✅ 安全  | ❌ 没有改结构      |
| `p1.next = headB` | ❌ 错误  | ✅ **篡改链表结构** |
| `p2.next = headA` | ❌ 错误  | ✅ **篡改链表结构** |

    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA

        # while p1 != p2:
        #     p1 = p1.next if p1 else headB
        #     p2 = p2.next if p2 else headA
        return p1

# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

