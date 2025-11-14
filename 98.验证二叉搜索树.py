#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30203
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        self.res = True
        self.traverse(root)
        return self.res

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        """
        if self.prev:
        这个写法有问题：
            [0,null,-1]
            中序遍历到右孩子 -1 时，self.prev 恰好是 0
        """
        # if self.prev:
        if self.prev is not None:
            if root.val <= self.prev:
                self.res = False
                return
        self.prev = root.val
        self.traverse(root.right)



    """
    上下界解法
    后序 
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, float('-inf'), float('inf'))

    def traverse(self, root, low, high):
        if not root:
            return True
        if not (low < root.val < high):
                return False
        subleft = self.traverse(root.left, low, root.val)
        subright = self.traverse(root.right, root.val, high)
        return subleft and subright
        



    
        
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

