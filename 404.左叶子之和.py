#
# @lc app=leetcode.cn id=404 lang=python3
# @lcpr version=30201
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return 

        """
        注意这个位置不只有
        # if root.left is None and root.right is None:
        这一种写法，可以玩的很复杂！！
        """
        if (root.left is not None and
            root.left.left is None and root.left.right is None):
            # 找到左侧的叶子节点，记录累加值
            self.res += root.left.val
        self.traverse(root.left)
        self.traverse(root.right)




# @lc code=end

#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

