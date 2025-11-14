#
# @lc app=leetcode.cn id=1373 lang=python3
# @lcpr version=30203
#
# [1373] 二叉搜索子树的最大键值和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # 记录全局最大值
        self.maxBST = 0
        self.findMaxBST(root)
        return self.maxBST

    """
    后序位置：得到子树信息
    用一个数组记录树的信息，传递给上层root
    [是否为bst, 树的最小值， 树的最大值， 树的总和]
    """
    def findMaxBST(self, root):
        if not root:
            # None是BST
            return [1, float('inf'), float('-inf'),0]

        # 后序
        left = self.findMaxBST(root.left)
        right = self.findMaxBST(root.right)

        tup = [0,0,0,0]
        # 左右子树都是bst且当前值 > left max , < right min
        if left[0]==1 and right[0]==1 and left[2] < root.val < right[1]:
            # 更新当前node
            tup[0] = 1
            """
            需要min，因为左右子树可能是None，inf会污染
            """
            tup[1] = min(root.val, left[1])
            tup[2] = max(root.val, right[2])
            tup[3] = root.val + left[3] + right[3]
            # 记录全局最大值
            self.maxBST = max(self.maxBST, tup[3])

        else:
            """
            这个还是要写，不写也过了是因为刚好tup初始化是0，默认不是bst
            如果初始化为1，就不对了，所以为了区分，需要加上
            """
            tup[0] = 0
        return tup
            
            

# @lc code=end


# 因为 left/right 子树有可能为空（即 None）
# return [1, float('inf'), float('-inf'), 0]
#
# @lcpr case=start
# [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,null,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [-4,-2,-5]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,3,null,6,3]\n
# @lcpr case=end

#

