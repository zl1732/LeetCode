#
# @lc app=leetcode.cn id=144 lang=python3
# @lcpr version=30203
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        太有趣：
        self.out = [] 不能放在这里，必须放在init
        preorderTraversal(1)
            -> self.out = []
            -> traverse(1)
                -> append(1)
                -> preorderTraversal(2)
                    -> self.out = []   # 💥 清空了
                    -> traverse(2)
                        -> append(2)
                        -> preorderTraversal(None)
                        -> preorderTraversal(None)
                    -> return self.out = [2]
                -> preorderTraversal(3)
                    -> self.out = []   # 💥 又清空
                    -> traverse(3)
                        -> append(3)
                -> return self.out = [3]

        """
        # self.out = []
        self.traverse(root)
        return self.out
    
    def traverse(self, root):
        if not root:
            return
        # 前序位置
        self.out.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)


class Solution: 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,8,null,null,6,7,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

