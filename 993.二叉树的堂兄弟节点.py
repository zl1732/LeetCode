#
# @lc app=leetcode.cn id=993 lang=python3
# @lcpr version=30201
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    """
    自创解法BFS
    """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            nodes = []
            for i in range(sz):
                cur = q.popleft()
                # 亲兄弟节点
                if cur.left and cur.right:
                    if (x==cur.left.val and y==cur.right.val) or \
                        (y==cur.left.val and x==cur.right.val):
                        return False
                # 添加左右节点 
                if cur.left:
                    q.append(cur.left)
                    nodes.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    nodes.append(cur.right.val)
                # 查询
            if x in nodes and y in nodes:
                return True
        return False
    

class Solution:
    """
    ✅ 解法一：BFS + 记录父节点和层级（推荐）
    这个解法太牛了。
    启示：
        * q = deque([(root, None, 0)]) 这里面可以带着很多信息，不用限定root
        * 在遍历时即可记录 找到的对应x, y值的节点信息x_info，y_info
    """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q = deque([(root, None, 0)])  # 节点, 父节点, 层级
        x_info = y_info = None

        while q:
            node, parent, depth = q.popleft()
            if node.val == x:
                x_info = (parent, depth)
            elif node.val == y:
                y_info = (parent, depth)
            if node.left:
                q.append((node.left, node, depth + 1))
            if node.right:
                q.append((node.right, node, depth + 1))
        
        return x_info and y_info and x_info[1] == y_info[1] and x_info[0] != y_info[0]


    # ✅ 解法二：DFS + 记录父节点和深度 （gpt）
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_info = self.y_info = None

        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x:
                self.x_info = (parent, depth)
            elif node.val == y:
                self.y_info = (parent, depth)
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
        
        dfs(root, None, 0)
        """
        这里注意虽然 None and None 输出 None
        但在布尔条件判断中，if None and None: 等价于：
        if False and False → False
        """
        return self.x_info and self.y_info and \
               self.x_info[0] != self.y_info[0] and \
               self.x_info[1] == self.y_info[1]
    

    # labuladong
    def __init__(self):
        self.depthX = 0
        self.depthY = 0
        self.parentX = None
        self.parentY = None
        self.x = 0
        self.y = 0

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y
        """
        注意这里parent可以选择从None开始
        后面执行一次后自动更新为root
        """
        self.traverse(root, depth=0, parent=None)
        if self.depthX == self.depthY and self.parentX != self.parentY:
            # 判断 x，y 是否是表兄弟节点
            return True
        return False

    def traverse(self,root, depth, parent):
        if root is None:
            return
        
        # 前后续在这里没意义了
        # 直接查看是否匹配目标值
        if root.val == self.x:
            # 记录深度和父节点
            self.depthX = depth
            self.parentX = parent

        if root.val == self.y:
            self.depthY = depth
            self.parentY = parent
        
        self.traverse(root.left, depth+1, root)
        self.traverse(root.right, depth+1, root)



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4,null,5]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4]\n2\n3\n
# @lcpr case=end

#

