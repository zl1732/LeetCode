#
# @lc app=leetcode.cn id=1315 lang=python3
# @lcpr version=30201
#
# [1315] 祖父节点值为偶数的节点和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.traverse(root)
        return self.sum

    def traverse(self, root):
        if root is None:
            return
        
        """
        思路是对的，但是反了， 如果当前是偶数，累加孙子的值
        不要差如果爷爷是偶数，累加当前值
        见下面的解法是这个的正确写法
        """
        # if grand.val %2 == 0:
        #     self.res += root.val
        # if root.left:
        #     if root.left.left:
        #         self.traverse(root.left.left, root)
        #     if root.left.right:
        #         self.traverse(root.left.right, root)
        # if root.right:
        #     if root.right.left:
        #         self.traverse(root.right.left, root)
        #     if root.right.right:     
        #         self.traverse(root.right.right, root)
        # 累加左子树孙子节点的值
        if root.val % 2 == 0:
            if root.left is not None:
                if root.left.left is not None:
                    self.sum += root.left.left.val
                if root.left.right is not None:
                    self.sum += root.left.right.val

            # 累加右子树孙子节点的值
            if root.right is not None:
                if root.right.left is not None:
                    self.sum += root.right.left.val
                if root.right.right is not None:
                    self.sum += root.right.right.val
        # 二叉树的遍历框架
        self.traverse(root.left)
        self.traverse(root.right)


"""
太牛逼的解法
直接递归输入(root, parent, grand)
调用时候是self.dfs(root, None, None)，就可以自己慢慢拉火车拉起来
"""
class Solution:
    def __init__(self):
        self.res = 0

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, None, None)
        return self.res

    def dfs(self,root, parent, grand):
        if not root:
            return

        # 前序位置：检测祖父是否为偶数
        if grand and grand.val % 2 == 0:
            self.res += root.val

        # 递归左右子树，当前节点作为 parent，原来的 parent 作为 grand
        self.dfs(root.left, root, parent)
        self.dfs(root.right, root, parent)

    
# @lc code=end



#
# @lcpr case=start
# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]\n
# @lcpr case=end

#

