#
# @lc app=leetcode.cn id=95 lang=python3
# @lcpr version=30203
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.build(1, n)


    def build(self, lo, hi):
        res = []
        if lo > hi:
            return [None]
        
        for i in range(lo, hi+ 1):
            left = self.build(lo, i-1)
            right = self.build(i+1, hi)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

# 增加memo
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {}
        if n == 0:
            return []
        return self.build(1, n)


    def build(self, lo, hi):
        res = []
        if lo > hi:
            return [None]
        if (lo, hi) in self.memo:
            return self.memo[(lo, hi)]

        for i in range(lo, hi+ 1):
            left = self.build(lo, i-1)
            right = self.build(i+1, hi)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        self.memo[(lo, hi)] = res
        return res


# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

