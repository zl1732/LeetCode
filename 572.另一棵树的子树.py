#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30201
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def __init__(self):
        self.found_flag = False
        self.root_found_tree = None


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        我的思路：traverse root, 或者说就是findnode，在tree中找subtree的head
        一起traverse，记录pre-order位置，如果不一样，马上返回False，否则最终返回True
        ❌ ❌ ❌ 
        🧠 但这段逻辑存在“隐性假设”，找到了第一个匹配的就可以比一次结构”。
        但实际上可能有多个值等于 subRoot.val 的节点，只有其中一个结构和 subRoot 相同，你只比较了第一个，就提前返回了 False，会漏掉正确答案。
        ✅ ✅ ✅
        正确的思路是：更稳妥的方式是遍历整棵 root，尝试所有可能的位置
        """
        root1 = self.findnode(root, subRoot.val)
        # not found
        if not self.root_found_tree:
            return False
        else:
            return self.compare_tree(root1, subRoot)

    
    def compare_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False
        elif root2 is None and root1 is not None:
            return False
        if root1.val != root2.val:
            return False
        return self.compare_tree(root1.left, root2.left) and self.compare_tree(root1.right, root2.right)

    def findnode(self, root, n):
        if root is None:
            return
        if root.val == n:
            self.root_found_tree = root
        self.findnode(root.left, n)
        self.findnode(root.right, n)

    # 错的写法
    def findnode1(self, root, n):
        if root is None:
            return
        if root.val == n:
            return root
        self.findnode(root.left, n)
        self.findnode(root.right, n)
        """
        永远返回None，有下面这样的就必须left = self.findnode(root.left, n),接住
        if root.val == n:
            return root
        """
        return None
    # 如果想返回值，就要这样写
    # 没找到返回None，找到配合返回left，right

    def findnode2(self, root, n):
        if root is None:
            return None
        if root.val == n:
            return root
        left = self.findnode(root.left, n)
        if left:
            return left
        right = self.findnode(root.right, n)
        if right:
            return right
        return None
    


class Solution:

    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.compare_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def compare_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False
        elif root2 is None and root1 is not None:
            return False
        if root1.val != root2.val:
            return False
        return self.compare_tree(root1.left, root2.left) and self.compare_tree(root1.right, root2.right)

    # 简化版
    # def compare_tree(self, root1, root2):
    #     if not root1 and not root2:
    #         return True
    #     if not root1 or not root2:
    #         return False
    #     return (root1.val == root2.val 
    #             and self.compare_tree(root1.left, root2.left) 
    #             and self.compare_tree(root1.right, root2.right))
    
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#

