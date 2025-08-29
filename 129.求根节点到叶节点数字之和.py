#
# @lc app=leetcode.cn id=129 lang=python3
# @lcpr version=30201
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def __init__(self):
        self.res = 0
        self.path = ""
    
    def traverse(self, root):
        # 这部分还是需要的
        if root is None:
            return
        
        if root.left is None and root.right is None:
            self.path += str(root.val)
            self.res += int(self.path)
            self.path = self.path[:-1]
            return 
        # 前序遍历添加路径节点
        self.path += str(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后续遍历删除路径节点
        self.path = self.path[:-1]


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        from collections import deque
        q = deque()
        res = 0
        cur = ""
        q.append((root, cur))
        while q:
            node, cur = q.pop()
            if node.left is None and node.right is None:
                cur += str(node.val)
                res += int(cur)
            
            if node.left is not None:
                q.append((node.left, cur+str(node.val)))
            if node.right is not None:
                q.append((node.right, cur+str(node.val)))
        return res



    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        from collections import deque
        q = deque()
        res = 0
        cur = ""
        q.append((root, cur))
        while q:
            node, cur = q.pop()
            cur += str(node.val)
            if node.left is None and node.right is None:
                res += int(cur)
            if node.left is not None:
                q.append((node.left, cur))
            if node.right is not None:
                q.append((node.right, cur))
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#

