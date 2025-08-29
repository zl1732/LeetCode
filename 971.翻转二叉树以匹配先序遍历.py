#
# @lc app=leetcode.cn id=971 lang=python3
# @lcpr version=30201
#
# [971] 翻转二叉树以匹配先序遍历
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
    典型错误！！
        dfs(root.left, i+1) 和 dfs(root.right, i+1)：
        这里面固定了i+1，同一个函数调用了两个递归，同时传入i+1
        左子树用的是 i+1，右子树也用的是 i+1，等于访问了两个节点，都在用 voyage[1]
        对比使用全局self.i, 会自动更新
      1
     / \
    2   3
        访问节点 1
            node.val == voyage[0] ✅
            self.i = 1
        进入左子树，访问节点 2
            node.val == voyage[1] ✅
            self.i = 2
        左右子树为空，返回
        回到节点 1，访问右子树 3
            node.val == voyage[2] ✅
            self.i = 3  正好遍历完  ✅
    """
    # def flipMatchVoyage_WrongAnswer(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
    #     self.res = []

    #     def dfs(root, i=0):
    #         if root is None:
    #             return True
            
    #         if root.val != voyage[i]:
    #             return False
            
    #         # 核心 尝试翻转.原始先序先访问左节点
    #         if root.left and root.left.val != voyage[i+1]:
    #             self.res.append(root.val)
    #             return dfs(root.right,i+1) and dfs(root.left,i+1)
    #         else:
    #             # 正常顺序访问左右子树
    #             return dfs(root.left,i+1) and dfs(root.right,i+1)

    #     if dfs(root):
    #         return self.res
    #     else:
    #         return [-1]


    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.res = []
        self.i = 0
        # dfs解法1
        # def dfs(root):
        #     if root is None:
        #         return True
            
        #     if root.val != voyage[self.i]:
        #         return False
            
        #     self.i += 1
        #     # 核心 尝试翻转.原始先序先访问左节点
        #     if root.left and root.left.val != voyage[self.i]:
        #         self.res.append(root.val)
        #         return dfs(root.right) and dfs(root.left)
        #     else:
        #         # 正常顺序访问左右子树
        #         return dfs(root.left) and dfs(root.right)

        #dfs解法2
        self.can_flip = True
        def dfs(root):
            """
                or not self.can_flip: 剪枝机制
                如果已经发现无法翻转了，则后续节点都不看了
                其实可以写作：
                    if not self.can_flip:
                        return False
            """
            if not self.can_flip:
                return False
            
            if root is None:
                return True
            
            if root.val != voyage[self.i]:
                self.can_flip = False
                return False
            
            self.i += 1
            # 核心 尝试翻转.原始先序先访问左节点
            if root.left and root.left.val != voyage[self.i]:
                self.res.append(root.val)
                # 真的翻转
                root.left, root.right = root.right, root.left
                # 注意这里写法跟dfs方法1不一样
            return dfs(root.left) and dfs(root.right)

        if dfs(root):
            return self.res
        else:
            return [-1]


# @lc code=end



#
# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

#

