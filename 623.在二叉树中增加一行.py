#
# @lc app=leetcode.cn id=623 lang=python3
# @lcpr version=30201
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    完全自创的答案，牛逼
    """
    # def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    #     from collections import deque
    #     q = deque()
    #     q.append(root)
    #     cur_depth = 1

    #     if depth ==1:
    #         newNode = TreeNode(val)
    #         newNode.left = root
    #         root = newNode
    #     while q:
    #         sz = len(q)
    #         for i in range(sz):
    #             cur = q.popleft()
    #             # 到达目标深度
    #             if cur_depth == depth-1:
    #                 print(cur.val)
    #                 # 创建新节点
    #                 newNode1 = TreeNode(val)
    #                 newNode2 = TreeNode(val)
    #                 # 原始子树
    #                 leftNode = cur.left
    #                 rightNode = cur.right
    #                 # 插入新节点，连接子树
    #                 cur.left = newNode1
    #                 cur.right = newNode2
    #                 newNode1.left = leftNode
    #                 newNode2.right = rightNode

    #             if cur.left is not None:
    #                 q.append(cur.left)
    #             if cur.right is not None:
    #                 q.append(cur.right)
    #         cur_depth += 1
    #     return root
    
    def __init__(self):
        self.curDepth = 1
        self.depth = 0
        self.val = 0

    def addOneRow1(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth = depth
        self.val = val

        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return 
        # pre-order
        if self.curDepth == self.depth-1:
            newNode1 = TreeNode(self.val)
            newNode2 = TreeNode(self.val)
            newNode1.left = root.left
            newNode2.right = root.right
            root.left = newNode1
            root.right = newNode2
        self.curDepth += 1
        self.traverse(root.left)
        self.traverse(root.right)
        self.curDepth -= 1



    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        def traverse(root, curDepth = 1):
            if root is None:
                return 
            # pre-order
            if curDepth == depth-1:
                newNode1 = TreeNode(val)
                newNode2 = TreeNode(val)
                newNode1.left = root.left
                newNode2.right = root.right
                root.left = newNode1
                root.right = newNode2
            traverse(root.left,curDepth+1)
            traverse(root.right,curDepth+1)
        traverse(root)
        return root

        


# @lc code=end



#
# @lcpr case=start
# [4,2,6,3,1,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,null,3,1]\n1\n3\n
# @lcpr case=end

#

