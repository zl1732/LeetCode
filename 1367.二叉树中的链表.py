#
# @lc app=leetcode.cn id=1367 lang=python3
# @lcpr version=30201
#
# [1367] 二叉树中的链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        我的思路：compare 函数输出对错
        遍历root每个点运行compare函数

     A
    / \
   B   C
  /
 D
/
1
 \
  2
   \
    3   
        ❌❌❌错误写法：
        #return self.match(root, head) or self.match(root.left, head) or self.match(root.right, head)
        match(A, head) ❌
        match(B, head) ❌
        match(C, head) ❌
        就停了！
        但是 1 在 D 的左子树里啊，而你没有继续递归深入去找！
        
        ✅✅✅正确写法：
        isSubPath(head, root)
        ↳ match(root, head)            # 当前点开始尝试
        ↳ isSubPath(head, root.left)  # 左子节点作为新起点
        ↳ isSubPath(head, root.right) # 右子节点作为新起点
        """

        #if root is None and head is not None:
        # 上面这个也能过，但是当成递归理解即可，所以用下面
        """
        ✅ 意思是：
            如果当前的树节点是 None，也就是说：
            整棵树已经遍历到尽头了，还没有找到链表匹配起点；
            那么自然不可能匹配上链表了，直接返回 False
        Q: 你怎么知道 “还没有找到链表匹配起点；”
        ✅ 回答要点：
        其实它并不知道是否已经找到过匹配起点。
        它的作用仅仅是说：
            如果现在这个节点是空的（None），那这个位置不可能是起点，也不能再继续下探了，所以返回 False。
        也就是说：
            isSubPath(head, root) 的任务是：遍历整棵树，看有没有哪一个节点 root 能作为匹配链表的起点。
            所以它会在每一个节点调用 self.match(root, head) 来尝试
            如果你现在已经遍历到空节点（None），说明你已经走到了这条分支的尽头——在这条路径上，“无节点可供尝试了”。
        """
        if root is None:
            return False
        #return self.match(root, head) or self.match(root.left, head) or self.match(root.right, head)
        return self.match(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


    def match1(self, root, head):
        if root is None and head is None:
            return False
        elif not root or not head:
            return False
        
        """
        ## ❌❌❌ 这行非常错！！不应该用 and 链接
        """
        """
        奥，我之前做的一道题是匹配子树，所以是and，对于链表只要or即可？
        完全正确！你总结得非常到位 👍
            要左右子树都完全对上才算匹配成功 ➜ 所以用 and
            链表在树上只需沿一条单一路径匹配即可 ➜ 所以用 or
        🧠 小贴士：
            树结构对比：左右都要一模一样 ➜ and
            路径延续/链状结构对比：只要某一方向通就行 ➜ or
        """
        return (root.val == head.val) and self.match(root.left, head.next) and self.match(root.right, head.next)

    def match(self, root, head):
        if head is None:
            return True  # 链表匹配完了
        if root is None:
            return False  # 树没了，链表还没走完
        if root.val != head.val:
            return False
        return self.match(root.left, head.next) or self.match(root.right, head.next)
        
# @lc code=end



#
# @lcpr case=start
# [4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

#

