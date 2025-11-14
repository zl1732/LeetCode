#
# @lc app=leetcode.cn id=894 lang=python3
# @lcpr version=30201
#
# [894] 所有可能的真二叉树
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
    如果你想生成一棵 n 个节点的满二叉树，首先要固定根节点，
    然后组装左右子树，根节点加上左右子树节点之和应该等于 n。

    # 参考生成BST那个题
    但是通过 i 的跳跃方式，本题必须0或2个子节点，所以应该选择2个跳一次

    后序位置 组装 res

    注意用 个数n 作为参数
    如果继续用lo,hi 会出现链表 比如 1 2 3, i = 1, 
    """
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []
        
        self.memo = {}
        # n个节点
        return self.build(n)


    def build(self, n):
        res = []
        # 最小级别就到1个节点
        if n == 1:
            return [TreeNode(0)]

        if n in self.memo:
            return self.memo[n]
        
        for i in range(1, n, 2):
            leftTrees = self.build(i)
            # 减去root
            rightTrees = self.build(n - i - 1)

            for left in leftTrees:
                for right in rightTrees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        # 注意这个位置
        self.memo[n] = res
        return res
    

# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

