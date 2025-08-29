#
# @lc app=leetcode.cn id=257 lang=python3
# @lcpr version=30201
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root)
        return self.res
    
    def __init__(self):
        # 递归路径
        self.path = []
        self.res = []
        
    def traverse(self, root):
        # 这里是return 不是return []
        if root is None:
            return
        # root 是叶子节点
        if root.left is None and root.right is None:
            # self.path.append(str(root.val))
            # self.res.append("->".join(self.path))  
            """
            self.path 转成了字符串 "->".join(...)，这是一个新的字符串副本。
            所以即使后续你 .pop() 了 self.path，也不会影响之前 res 里保存的结果。
            """   
            self.path.append(root.val)
            self.res.append("->".join(map(str, self.path)))
            self.path.pop()
            return
        
        # 添加节点是前序遍历
        self.path.append(root.val)
        self.binaryTreePaths(root.left)
        self.binaryTreePaths(root.right)

        # 每条路径终点是后续遍历
        self.path.pop()

        
    # dfs + stack
    def binaryTreePaths(self, root):
        if not root:
            return
        
        from collections import deque
        stack = deque()
        res,path = [],[]
        stack.append((root, path))
        
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                path.append(str(node.val))
                res.append("->".join(map(str, path)))

            if node.right:
                stack.append((node.right, path+[node.val]))
            if node.left:
                stack.append((node.left, path+[node.val]))
        return res
        
    # bfs + queue
    # 当使用popleft时，也就是queue，就变成了bfs
    def binaryTreePaths2(self, root):
        #...
        while queue:
            node, ls = queue.popleft()
            pass


# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

