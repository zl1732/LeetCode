#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30201
#
# [543] 二叉树的直径
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
    前序方法，不推荐
    """
    def __init__(self):
        self.max_diam = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_diam
    
    def traverse(self, root):
        if root is None:
            return 
        """
        注意粘贴函数用于调用时，要去掉参数的self
        """
        cur_max = self.maxDepth(root.left) + self.maxDepth(root.right)
        self.max_diam = max(self.max_diam, cur_max)
        self.traverse(root.left)
        self.traverse(root.right)
        
    # 计算二叉树的最大深度
    def maxDepth(self, root):
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return 1 + max(leftMax, rightMax)

    """
    后序方法
    """
    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 后序位置，顺便计算最大直径
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)

        return 1 + max(leftMax, rightMax)
"""
注意：
“结构性问题（如求深度）” vs “过程性问题（如遍历）”的关键区别：

✅ 一类 return 是“结构控制”型 —— 有顺序意义
    # 前序遍历
    return [root.val] + left + right
    # 中序遍历
    return left + [root.val] + right
    # 后序遍历
    return left + right + [root.val]

✅ 另一类 return 是“数值合并”型 —— 无顺序意义
    return 的本质是“合并左右子问题的值”
    它只是 结果的传递、组合，不代表访问顺序
    例：
    return 1 + max(left, right)       # 求深度
    return is_bst_left and is_bst_right and valid(root)  # 判断 BST
    return max(left + right, ...)     # 求路径和等

🔥🔥🔥   “以节点为单位做动作”的（遍历型）
            vs
        “以子树为单位组合结果”的（结构型）
"""

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

