#
# @lc app=leetcode.cn id=1448 lang=python3
# @lcpr version=30201
#
# [1448] 统计二叉树中好节点的数目
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
    我写的
    """
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        self.curMax = root.val
        self.res = 0
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        
        if root.val>=self.curMax:
            self.res += 1
            """
            应该使用局部变量 prevMax，说明：
        3
       / \
      1   4
         / \
        1   5
            当你从节点 4 递归进入 5：
                self.prevMax = 4
                self.curMax = 5
            现在回到节点 4，你以为 self.prevMax = 3（3 是 4 的父节点最大值）
            但 self.prevMax 早就被 5 覆盖成 4 了
            所以你 self.curMax = self.prevMax = 4，错了！应该回退为 3
            """
            prevMax = self.curMax
            self.curMax = root.val
            self.traverse(root.left)
            self.traverse(root.right)
            self.curMax = prevMax
        else:
            self.traverse(root.left)
            self.traverse(root.right)
        
    """
    gpt 改的好看，把max值作为递归参数自动传递
    ✅ “把变量作为参数传进去，比用全局变量+回溯的方法更安全”
    这不仅是刷题经验，也是写大型程序、做多线程、多协程、分布式开发时的一个重要编程哲学：
    显式传参 > 隐式状态共享。你已经领悟到了！👏
    """
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverse(root, root.val)
        return self.res

    def traverse(self, node: Optional[TreeNode], max_val: int):
        if not node:
            return
        
        # 更新 max值
        if node.val >= max_val:
            self.res += 1
            max_val = node.val 

        self.traverse(node.left, max_val)
        self.traverse(node.right, max_val)

# @lc code=end



#
# @lcpr case=start
# [3,1,4,3,null,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,null,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

