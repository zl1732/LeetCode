#
# @lc app=leetcode.cn id=1457 lang=python3
# @lcpr version=30201
#
# [1457] 二叉树中的伪回文路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        思路，记录路径上出现过元素数量的奇偶性
        奇数次 元素 >1 个 则不行
        3 2 2 3 -- 0奇数
        3 2 1 2 3 -- 1奇数
        3 2 1 4 2 3 -- 2奇数 ❌
        """
        self.res = 0
        self.odds = {}
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return
        
        if root.val in self.odds:
            self.odds[root.val] += 1
        else:
            self.odds[root.val] = 1
        if root.left is None and root.right is None:
            # reach leaf, check odd number
            # {3:2, 1:1, 2:1, 4:2}
            if sum([x%2 for x in self.odds.values()])<=1:
                self.res += 1
            self.odds[root.val] -= 1
            return
        
        self.traverse(root.left)
        self.traverse(root.right)
        self.odds[root.val] -= 1

# @lc code=end



#
# @lcpr case=start
# [2,3,1,3,1,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,1,3,null,null,null,null,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [9]\n
# @lcpr case=end

#

