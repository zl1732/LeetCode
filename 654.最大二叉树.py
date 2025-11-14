#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30203
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # find root
        maxVal = -1
        maxIdx = -1
        for i, num in enumerate(nums):
            if num > maxVal:
                maxVal = num
                maxIdx = i
        
        # 构建root
        root = TreeNode(maxVal)
        # 构建左右子树
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root

        
# @lc code=end



#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#

