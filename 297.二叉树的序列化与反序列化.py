#
# @lc app=leetcode.cn id=297 lang=python3
# @lcpr version=30203
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 前序
    def serialize(self, root):
        if not root:
            return "#"
        return str(root.val) + "," + \
               self.serialize(root.left) + "," + \
               self.serialize(root.right)


    def deserialize(self, data):
        self.nodes = data.split(',')
        self.idx = 0
        return self._deserialize()

    """
    用外部指针，指定node的位置
    """
    def _deserialize(self):
        if self.idx >= len(self.nodes):
            return None

        val = self.nodes[self.idx]
        self.idx += 1

        if val == '#':
            return None

        root = TreeNode(int(val))
        root.left = self._deserialize()
        root.right = self._deserialize()
        return root

    """
    用pop原地修改nodes序列
    """
    def _deserialize(self, nodes: List[str]) -> TreeNode:
        if not nodes: return None
        # 前序位置
        first = nodes.pop(0)
        if first == '#': return None
        root = TreeNode(int(first)) 

        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,null,4,5]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

