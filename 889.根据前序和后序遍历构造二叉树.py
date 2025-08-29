#
# @lc app=leetcode.cn id=889 lang=python3
# @lcpr version=30201
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
通过前序中序，或者后序中序遍历结果可以确定一棵原始二叉树，
但是通过前序后序遍历结果无法确定原始二叉树。

所以你能假设每个非叶子节点都有左右子树，就可以用 pre[1] 去 post 里找出左子树的边界。
满二叉树定义： 每个非叶子节点都有两个子节点
    如果你不是叶子节点，就一定有左子树、右子树
    所以只要当前节点不是叶子，前序的下一个节点一定是左子树的根
preorder:  [1] [2, 4, 5] [3, 6, 7]
postorder:     [4, 5, 2] [6, 7, 3] [1]
               ↑  left  ↑  right  ↑ root

"""
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {n:i for i, n in enumerate(postorder)}

        def build(pre_left, pre_right, pos_left, pos_right):
            # leaf
            if pre_left > pre_right:
                return None
            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])
            # root
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            left_val = preorder[pre_left+1]
            index = idx_map[left_val]
            left_size = index - pos_left + 1

            # left tree
            root.left = build(pre_left = pre_left + 1,
                              pre_right = pre_left + left_size, #
                              pos_left = pos_left, #
                              pos_right = index #
                              )            
            # right tree
            """
            注意是pos_right = pos_right-1 ！！！
            """
            root.right = build(pre_left = pre_left + left_size + 1, #
                              pre_right = pre_right,
                              pos_left = index + 1, #
                              pos_right = pos_right-1 #
                              )         
            return root
        return build(0, len(preorder)-1, 0, len(postorder)-1)



class Solution1:
    def __init__(self):
        self.valToIndex = {}

    def constructFromPrePost(self, preorder, postorder):
        self.val_to_idx = {val: i for i, val in enumerate(postorder)}
        
        return self.build(preorder, 0, len(preorder) - 1,
                          postorder, 0, len(postorder) - 1)

    def build(self, preorder, preStart, preEnd, postorder, postStart, postEnd):
        if preStart > preEnd:
            return None
        
        """
        在 889 这题中，我们依赖 preStart + 1 去找左子树的根：
        leftRootVal = preorder[preStart + 1]
        如果你当前已经是叶子节点，preStart == preEnd，那么就没有 preStart + 1，再执行上面这行就会 数组越界 (IndexError) ❌。
        ✅ 所以这个判断也起到了防御性作用：让你不会错误地继续往下分割子树
        """
        
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]

        # root.left 的值是前序遍历第二个元素
        # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
        # 确定 preorder 和 postorder 中左右子树的元素区间
        leftRootVal = preorder[preStart + 1]

        # leftRootVal 在后序遍历数组中的索引
        index = self.valToIndex[leftRootVal]

        # 左子树的元素个数
        leftSize = index - postStart + 1

        # 先构造出当前根节点
        root = TreeNode(rootVal)
        # 递归构造左右子树
        # 根据左子树的根节点索引和元素个数推导左右子树的索引边界
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                postorder, index + 1, postEnd - 1)

        return root

# @lc code=end


#
# @lcpr case=start
# [1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1]\n
# @lcpr case=end

#

