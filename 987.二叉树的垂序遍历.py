#
# @lc app=leetcode.cn id=987 lang=python3
# @lcpr version=30203
#
# [987] 二叉树的垂序遍历
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
    首先先traverse一遍树，用[node, col, row] 记录每个点
    然后按要求排序后 按输出格式要求输出即可
    """
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0, 0)
        # 排序
        self.nodes.sort(key = lambda x: (x[1],x[2], x[0].val))
        # 输出
        res = []
        prev_col = None
        for node_ in self.nodes:
            node, col, row = node_
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(node.val)
        return res
            


    def __init__(self):
        self.nodes = []

    def traverse(self, root, col, row):
        if not root:
            return
        self.nodes.append([root,col, row])
        self.traverse(root.left, col - 1, row + 1)
        self.traverse(root.right, col + 1, row + 1)        

        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,6,5,7]\n
# @lcpr case=end

#

