#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30203
#
# [230] 二叉搜索树中第 K 小的元素
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
    第一遍做错了，用了后序
    BST 的中序遍历其实就是升序排序的结果
    BST 的中序遍历其实就是升序排序的结果
    BST 的中序遍历其实就是升序排序的结果
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = 0
        self.res = 0
        self.traverse(root, k)
        return self.res
        

    def traverse(self, root, k):
        if not root:
            return

        self.traverse(root.left, k)
        self.rank += 1
        # 后序位置计数
        if self.rank == k:
            self.res = root.val
            return
        self.traverse(root.right, k)
        

        
    

        
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

