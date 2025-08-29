#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30201
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        from collections import deque
        res = []
        q = deque([root])

        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right is not None:
                    q.append(node.right)
                if node.left is not None:
                    q.append(node.left)
        return res

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.depth = 0
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return
        # 前序位置,注意在前序位置depth+1
        # 等同于递归是传入depth+1
        self.depth += 1
        if len(self.res)<self.depth:
            self.res.append(root.val)
        self.traverse(root.right)
        self.traverse(root.left)
        # 后序位置
        self.depth -= 1
    

    # 用另外一个集合记录走过的depth，另外depth直接作为参数传递
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depths= set()
        res=[]
        def traverse(root, depth=0):
            if root is None:
                return
            if depth not in depths:
                res.append(root.val)
                depths.add(depth)
            traverse(root.right, depth+1)
            traverse(root.left, depth+1)
        traverse(root)
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

