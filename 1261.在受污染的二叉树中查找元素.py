#
# @lc app=leetcode.cn id=1261 lang=python3
# @lcpr version=30201
#
# [1261] 在受污染的二叉树中查找元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    """
    1. ❌ 你在 traverse 中始终操作的是 self.root
    self.traverse(self.root.left, self.root.val*2+1)
    self.traverse(self.root.right, self.root.val*2+2)
    总结：traverse里永远用local变量，最好叫node，区分root
         永远不能用self.root

    2. 这里大问题，赋值之后最后又二次赋值
        if newVal == self.target:
            self.res = True
        ...
        self.res = False
        正确的方法是初始化时直接赋值False
    """
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.target = 0
        self.res = False
    
    def find(self, target: int) -> bool:
        self.target = target
        self.traverse( 0)
        return self.res
    

    def traverse(self, newVal):
        if self.root is None:
            return
        
        # 更新节点值
        self.root.val = newVal

        if newVal == self.target:
            self.res = True
            return
        """
        ❌ 你在 traverse 中始终操作的是 self.root
        """
        # pre order
        self.traverse(self.root.left, self.root.val*2+1)
        self.traverse(self.root.right, self.root.val*2+2)
        """
        ❌ 写在这有明显问题，会覆盖前面找到的self.res = True
        """
        #self.res = False



"""
❌ 这个版本的问题：超出时间限制
["FindElements", "find", "find", ..., "find"]  // 几百次调用 
33 / 34 个通过的测试用例

每次调用find都要traverse遍历整棵树一遍。
如果调用了几百次 find()，时间复杂度是 O(q·n)（q 是查询次数，n 是树节点数）。

✅ 正确优化思路：初始化时一次性恢复树+保存值集合，后续 O(1) 查询
"""
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.target = 0
        self.res = False

    def find(self, target: int) -> bool:
        self.target = target
        self.res = False
        self.traverse(self.root, 0)
        return self.res

    def traverse(self, node, newVal):
        if node is None:
            return

        node.val = newVal

        if newVal == self.target:
            self.res = True
            return

        self.traverse(node.left, newVal * 2 + 1)
        self.traverse(node.right, newVal * 2 + 2)


"""
✅ 正确优化思路：初始化时一次性恢复树+保存值集合，后续 O(1) 查询
"""
class FindElements:
    # 帮助 find 函数快速判断
    def __init__(self, root):
        self.allValue = set()
        self.traverse(root, 0)

    # 二叉树遍历函数
    def traverse(self, root, val):
        if root is None:
            return 
        
        root.val = val
        self.allValue.add(val)

        self.traverse(root.left, val*2 + 1)
        self.traverse(root.right, val*2 + 2)

    def find(self, target):
        return target in self.allValue



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end



#
# @lcpr case=start
# ["FindElements","find","find"]\n[[[-1,null,-1]],[1],[2]]\n
# @lcpr case=end

# @lcpr case=start
# ["FindElements","find","find","find"]\n[[[-1,-1,-1,-1,-1]],[1],[3],[5]]\n
# @lcpr case=end

# @lcpr case=start
# ["FindElements","find","find","find","find"]\n[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]\n
# @lcpr case=end

#

