#
# @lc app=leetcode.cn id=894 lang=python3
# @lcpr version=30201
#
# [894] 所有可能的真二叉树
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
    如果你想生成一棵 n 个节点的满二叉树，首先要固定根节点，
    然后组装左右子树，根节点加上左右子树节点之和应该等于 n。
    """
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

