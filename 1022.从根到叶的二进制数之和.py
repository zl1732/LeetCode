#
# @lc app=leetcode.cn id=1022 lang=python3
# @lcpr version=30201
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
# 二进制转十进制
binary_str = "100"
decimal = int(binary_str, 2)
print(decimal)  # 输出 4

# 十进制转二级制：bin(n)
"""
class Solution:
    """
    这种写法很不推荐，尽量用self.res
    """
    res = 0
    path = ""

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        # 注意这里也是self.res
        return self.res
    
    def traverse(self,root):
        if root is None:
            return
        
        # pre order
        self.path += str(root.val)
        # 叶子节点
        if root.left is None and root.right is None:
            self.res += int(self.path, 2)
            self.path = self.path[:-1]
            return
        self.traverse(root.left)
        self.traverse(root.right)
        # post order
        self.path = self.path[:-1]

"""
* <<：左移运算符（Left Shift）
    x << n 表示将整数 x 的二进制表示向左移动 n 位。

* 左移一位相当于乘以 2
    5 << 1   # 5 的二进制是 101，左移一位变成 1010 → 十进制为 10

* 结果依然是以十进制形式存储和显示的整数，除非
    y = x << 1 | 1
    print(bin(y))         # 输出：0b111
"""
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.path = 0
        self.res = 0
        self.traverse(root)
        return self.res

    def traverse(self, root: TreeNode):
        if root is None:
            return
        if root.left is None and root.right is None:
            # 叶子节点
            self.res += self.path << 1 | root.val
            return
        # 前序位置
        self.path = self.path << 1 | root.val
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.path = self.path >> 1

# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

