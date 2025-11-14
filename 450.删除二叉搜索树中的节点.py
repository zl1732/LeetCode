#
# @lc app=leetcode.cn id=450 lang=python3
# @lcpr version=30203
#
# [450] 删除二叉搜索树中的节点
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
    情况 1：A 恰好是末端节点，两个子节点都为空，那么它可以直接被删除。
    情况 2：A 只有一个非空子节点，那么它要让这个孩子接替自己的位置。
    情况 3：A 有两个子节点，为了不破坏 BST 的性质，必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。
    """
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        # 1) 寻找 key，记录 parent
        parent = None
        cur = root
        while cur and cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        # 没找到
        if not cur:
            return root
        
        """
        也可以这样写， nonlocal：声明这个变量来自上层函数的外层作用域；
        """
        # 一个小工具：把 parent 的对应孩子指向 child
        def connect(parent, cur, child):
            nonlocal root
            if parent is None:
                # 删的是根
                root = child
            else:
                if parent.left is cur:
                    parent.left = child
                else:
                    parent.right = child


        # 2) ≤1 个孩子
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            connect(parent, cur, child)
            return root

        # 3) 两个孩子：找后继（右子树最左）
        succ_parent = cur
        succ = cur.right
        while succ.left:
            succ_parent = succ
            succ = succ.left
        # 用后继值覆盖当前节点
        cur.val = succ.val
        """
        # 情况 1️⃣：succ 是 succ_parent 的左孩子
        # 举例：
        #       cur=8
        #      /    \
        #     4      10
        #           /
        #          9   <- succ_parent
        #         /
        #        8.5 <- succ
        #
        # 经过 while succ.left: succ_parent=9, succ=8.5
        # succ.right=None, succ.left=None
        # 我们要删掉 8.5，让 9.left=None

            # 情况 2️⃣：succ 就是 cur.right 本身（右子树根节点最小）
            #
            # 举例：
            #       cur=8
            #      /    \
            #     4      9 <- succ (=cur.right)
            #
            # 右子树只有一个节点（9）
            # succ_parent=cur(8), succ=9
            # succ.right=None
            # 删除 succ 就相当于让 cur.right=None

            # -------------------------------------------------------------
            # 情况 3️⃣：succ 就是 cur.right 本身，但 succ 有右孩子
            #
            #       cur=8
            #      /    \
            #     4      9 <- succ (=cur.right)
            #              \
            #               9.5
            #
            # succ_parent = cur
            # succ = 9
            # succ.right = 9.5 (succ_child)
            #
            # 删除 succ 后，我们让 cur.right = succ.right，
            # 相当于让 9.5 顶上成为新的右子树根。
        """
        # 删除后继节点（succ 最多只有右孩子）
        succ_child = succ.right # 可能为 None
        if succ_parent.left is succ:
            succ_parent.left = succ_child
        else:
            # 说明后继就是 cur.right
            succ_parent.right = succ_child
        return root



class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            # 处理情况 3
            # 获得右子树最小的节点
            minNode = self.getMin(root.right)

            # 删除右子树最小的节点
            root.right = self.deleteNode(root.right, minNode.val)

            # 用右子树最小的节点替换 root 节点
            minNode.left = root.left
            minNode.right = root.right
            """
            不涉及parent连接到minNode
            """
            root = minNode

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left != None:
            node = node.left
        return node
    









class Solution1:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val == key:
            # 叶子 或 单侧子树
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            minNode = self.getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode

        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left != None:
            node = node.left
        return node
    



# @lc code=end



#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

