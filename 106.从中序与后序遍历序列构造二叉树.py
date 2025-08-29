#
# @lc app=leetcode.cn id=106 lang=python3
# @lcpr version=30201
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {n:i for i,n in enumerate(inorder)}

        def build(pos_left, pos_right, in_left, in_right):
            # build leaf
            # if in_left > in_right:
            #     return None
            if pos_right < pos_left:
                return None
            
            # build root
            root_val = postorder[pos_right]
            root = TreeNode(root_val)
            index = idx_map[root_val]
            """
            注意是*in_right* - index
            """
            right_size = in_right - index

            # right tree
            root.right = build(pos_left = pos_right - right_size,
                               pos_right = pos_right - 1,
                               in_left = index + 1,
                               in_right = in_right
                            )

            # left tree
            root.left = build(pos_left = pos_left,
                              pos_right = pos_right - 1 - right_size,
                              in_left = in_left,
                              in_right = index - 1
                            )
            return root
    
        return build(0, len(postorder)-1, 0, len(inorder)-1)


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {n:i for i,n in enumerate(inorder)}

        def build(pos_right, in_left, in_right):
            # build leaf
            if in_left > in_right:
                return None
 
            # build root
            root_val = postorder[pos_right]
            root = TreeNode(root_val)
            index = idx_map[root_val]
            right_size = in_right - index

            # right tree
            root.right = build(pos_right = pos_right - 1,
                               in_left = index + 1,
                               in_right = in_right
                            )

            # left tree
            root.left = build(pos_right = pos_right - 1 - right_size,
                              in_left = in_left,
                              in_right = index - 1
                            )
            return root
    
        return build(len(postorder)-1, 0, len(inorder)-1)
    

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {n:i for i,n in enumerate(inorder)}
        self.pos_right = len(postorder)-1

        def build(in_left, in_right):
            # build leaf
            if in_left > in_right:
                return None
 
            # build root
            root_val = postorder[self.pos_right]
            root = TreeNode(root_val)
            index = idx_map[root_val]
            self.pos_right -= 1

            # right tree
            root.right = build(in_left = index + 1,
                               in_right = in_right
                            )

            # left tree
            root.left = build(in_left = in_left,
                              in_right = index - 1
                            )
            return root
    
        return build(0, len(inorder)-1)
    
# @lc code=end



#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

