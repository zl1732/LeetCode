#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30203
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # 层序遍历法
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]': 
        from collections import deque
        if not root:
            return None
        q = deque([root])

        while q:
            sz = len(q)
            prev = None
            for i in range(sz):
                # 注意是popleft
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if prev:
                    prev.next = node
                prev = node
            # 初始已经是指向null
            node.next = None
        return root
            

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        # 叶子
        if not root.left and not root.right:
            return root
        
        # 根 / 左节点 / 右节点
        root.left.next = root.right

        # 左节点
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
        return root




        
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1: 'Node', node2: 'Node') -> None:
        # 因为完美二叉树，叶子节点
        if not node1 and not node2:
            return
        # 前序位置 
        node1.next = node2 
        
        # 连接相同父节点的两个子节点
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # 连接跨越父节点的两个子节点
        self.traverse(node1.right, node2.left)



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

