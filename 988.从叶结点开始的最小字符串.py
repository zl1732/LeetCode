#
# @lc app=leetcode.cn id=988 lang=python3
# @lcpr version=30201
#
# [988] 从叶结点开始的最小字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
# 1. 字典序比较大小
Python 中字符串的大小比较，是逐字符按 ASCII 值进行比较的，就像字典中单词排序规则一样：

    'a' < 'b' < 'c' < ... < 'z'

    'abc' < 'abd' 因为第3个字符 'c' < 'd'

    'abc' < 'abcd' 因为前3个相同，前者更短

    'abz' > 'abx' 因为第3个字符 'z' > 'x'

    
# 2. ord & chr
✅ ord()：字符 → 整数（Unicode编码）
ord('a')  # 输出 97
✅ chr()：整数（Unicode编码）→ 字符
chr(97)   # 输出 'a'
✅ 常见用途
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
"""
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # will solve with recursive dfs
        # noted that from leaf to root

        self.res = None
        self.path = ""
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return
        
        self.path = chr(ord('a') + root.val) + self.path
        if root.left is None and root.right is None:
            # 到达叶子节点，累加路径和
            if self.res is None or self.res > self.path:
                self.res = self.path
                ### 提前终止并回退，如若终止，则：
                ### Python的函数调用机制会自动：返回到上一层调用该函数的地方，继续执行上一级函数中接下来的语句。
                self.path = self.path[1:]
                return
        self.traverse(root.left)
        self.traverse(root.right)
        
        self.path = self.path[1:]


# 标准答案
class Solution1:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.traverse(root)
        return self.res
    
    # 遍历过程中的路径
    """
    也可以这样直接写成全局变量
    """
    path = ""
    res = None

    # 二叉树遍历函数
    def traverse(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            # 找到叶子结点，比较字典序最小的路径
            # 结果字符串是从叶子向根，所以需要反转
            self.path = chr(ord('a') + root.val) + self.path

            # 如果字典序更小，则更新 res
            if self.res is None or self.res > self.path:
                self.res = self.path

            ### 提前终止并回退，如果没有这行，则去到下面
            self.path = self.path[1:]
            return
        # 前序位置
        self.path = chr(ord('a') + root.val) + self.path

        self.traverse(root.left)
        self.traverse(root.right)

        # 后序位置
        self.path = self.path[1:]
        
# @lc code=end



#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#

