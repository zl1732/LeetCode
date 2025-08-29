#
# @lc app=leetcode id=1145 lang=python3
# @lcpr version=30201
#
# [1145] Binary Tree Coloring Game
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
只要封住对手的父节点即可，问题转化为：
对手选的点的子树节点数量是否 ＜ 50%

不对：对手选完了，树被切成三部分，左子树，右子树，父节点+兄弟子树
也就是说，区域中节点数最多的那个区域中的节点个数大于 总数 / 2，你能赢。

不能用之前的套路，要找到对手点的node(tree)，
1. 计算该node左子树，右子树的数量
2. 计算root总点的数量
3. 计算最多的一块/总数 ？ 50%
"""
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        found = self.findNode(root, x)
        l_cnt = self.countNodes(found.left)
        r_cnt = self.countNodes(found.right)
        total = self.countNodes(root)
        # = total - l_cnt - r_cnt
        # max(l_cnt, max(r_cnt, other_count)) > n // 2
        if l_cnt/total > 0.5 or r_cnt/total > 0.5 or (1+l_cnt+r_cnt)/total < 0.5:
            return True
        else:
            return False

    def findNode(self, node, n):
        # 递归找
        if node is None:
            """
            不是return
            """
            return None
        if node.val == n:
            return node
        left = self.findNode(node.left, n)
        if left is not None:
            return left
        else:
            return self.findNode(node.right, n)

    
    """
    这个需要重点记忆
    """
    def countNodes(self, node):
        if node is None:
            """
            return 0
            """
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
        



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10,11]\n11\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n1\n
# @lcpr case=end

#

