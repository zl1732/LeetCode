#
# @lc app=leetcode.cn id=701 lang=python3
# @lcpr version=30203
#
# [701] 二叉搜索树中的插入操作
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
    自己写：
    递归 + 找父节点
    """
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # ① 空树：直接成为根
        if not root:
            return TreeNode(val)
        
        self.parent = None
        self.searchBST(root, val)
        if val < self.parent.val:
            self.parent.left = TreeNode(val)
        elif val > self.parent.val:
            self.parent.right = TreeNode(val)
        return root
        
    
    def searchBST(self, root, val):
        if not root:
            return None
        """
        self.parent = root
        正确更新位置：前序位置
        错误更新位置：后序位置
        在每次向下走之前就把当前节点记作 parent。这样当走到 None 时，parent 正好是插入位置的父节点
        """
        self.parent = root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right,val)
        # self.parent = root
        return root
    

# @lc code=end



# 递归直接插入  空间 O(h)（递归栈），时间 O(h)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:  # val > root.val，题目保证不相等
            root.right = self.insertIntoBST(root.right, val)
        return root


# 迭代直接插入  空间 O(1)，时间 O(h)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:  # val > cur.val
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root

# 迭代找父节点
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        parent = None
        cur = root
        while cur:
            parent = cur
            if val < cur.val:
                cur = cur.left
            else:  # val > cur.val
                cur = cur.right

        # 此时 parent 指向应插入位置的父结点
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root


#
# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [40,20,60,10,30,50,70]\n25\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3,null,null,null,null,null,null]\n5\n
# @lcpr case=end

#

