#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30201
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    """
    | 遍历方式     | 顺序        | 信息             |
    | ----------- | ---------- | -------------- |
    | **前序遍历** | 根 → 左 → 右 | 根节点总是当前序列的第一个  |
    | **中序遍历** | 左 → 根 → 右 | 根节点把左右子树在中间分隔开 |

    """
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立一个值到索引的映射，方便快速查找
        idx_map = {n:i for i, n in enumerate(inorder)}
        def build(cur_head, in_left, in_right):
            if in_left > in_right:
                """
                必须是None，因为是子树
                """
                return None
            
            """
            1. 注意需要root
            """
            root_val = preorder[cur_head]
            root = TreeNode(root_val)
            # 首先根据preorder点找到inorder中位置
            index = idx_map[root_val]
            """
            关于in_left 和 in_right是怎么收缩的:
                构建左子树：in_left → index - 1
                构建右子树：index + 1 → in_right
                最左侧的子树其实in_left一直都是0，只有往右边走才会变大
            """
            # inorder的左子树
            # cur_head = cur_head + 1
            # in_left = 
            """
            不要给 in_left、in_right 这些递归参数“就地赋新值”——你需要保留父调用传进来的原始边界
            比如in_right = index - 1，这里永远改变了in_right的值
            比如 本来in_left = 0, in_right = 4, 运行左子树，in_right变成2
            到右子树 build(cur_head + 1 + left_size, index + 1, in_right)
            这个in_right本来应该是4，现在是2

            所以正确传法，只是给子树的in_right传入了0， 原始in_right不变，从子树退出时，in_right还是4
            🧠 一句话总结
            🔒 函数参数是按值传递的（对于整数），每次递归都是新的一份副本，互不干扰。
            """
            in_right = index - 1
            # root.left = build(cur_head, in_left, in_right)
            root.left = build(cur_head + 1, in_left, index - 1)


            # inorder的右子树
            left_size = index - in_left
            # cur_head = cur_head + left_size
            in_left = index + 1
            # in_right = 
            # root.right = build(cur_head, in_left, in_right)
            root.right = build(cur_head + 1 + left_size, index + 1, in_right)

            return root
        """
        注意len(inorder)-1
        """
        return build(0, 0, len(inorder)-1)

    # 第二遍
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {n:i for i, n in enumerate(inorder)}
        def build(pre_left, pre_right, in_left, in_right):
            # build leaf
            if pre_left > pre_right:
                return None
            # if in_left > in_right:
            #     return None
            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])

            # build root
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            # root in inorder, index
            index = idx_map[root_val]
            left_size = index - in_left

            # build left
            root.left = build(pre_left=pre_left + 1, 
                              pre_right=pre_left + left_size, 
                              in_left=in_left, 
                              in_right=index-1)

            # build right
            root.right = build(pre_left=pre_left + 1 + left_size, 
                              pre_right=pre_right, 
                              in_left=index + 1, 
                              in_right=in_right)
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)








# 标准答案
class Solution1:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立一个值到索引的映射，方便快速查找
        idx_map = {val: i for i, val in enumerate(inorder)}

        # 定义递归函数
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            
            # 前序第一个就是根节点
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # 在中序遍历中找到根的位置
            index = idx_map[root_val]

            # 左子树节点数量
            left_size = index - in_left

            # print("右子树pre_left：",pre_left + left_size + 1)
            # print("右子树in_left：",index + 1)
            # 构建左子树
            root.left = build(pre_left + 1, pre_left + left_size,
                              in_left, index - 1)
            
            # 构建右子树
            root.right = build(pre_left + left_size + 1, pre_right,
                               index + 1, in_right)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


    """
    ✅ 总结一句话
        ✔️ 是的，当你用 self.pre_idx += 1 的方式时，到了右子树递归那一步，
        这个前序索引变量已经自动走到了右子树的根节点位置，
        所以你不用自己计算 pre_left + left_size + 1 ——它是“自然滑过去的”。
    """
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # 用一个类变量来记录前序数组当前的“根节点位置”

        def build(in_left, in_right):
            # 中序区间为空，说明没有子树了
            if in_left > in_right:
                return None
            
            # 当前前序遍历的节点是根
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # 找到这个根在中序中的位置
            index = idx_map[root_val]

            # 构建左子树（中序的左段）
            root.left = build(in_left, index - 1)
            # 构建右子树（中序的右段）
            root.right = build(index + 1, in_right)
            return root
        
        return build(0, len(inorder) - 1)
    


# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

