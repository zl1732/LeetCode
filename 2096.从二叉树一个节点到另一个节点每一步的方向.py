#
# @lc app=leetcode.cn id=2096 lang=python3
# @lcpr version=30201
#
# [2096] 从二叉树一个节点到另一个节点每一步的方向
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
📢📢📢📢 给点查找从根到该点路径 📢📢📢📢

# 方法1：使用全局self.path + 手动pop()
# 我自己平常写的，跟labuladong学的
# ✅ 优点：节省内存，不会重复创建新路径列表
# ⚠️ 缺点：必须小心管理状态，递归完后一定要path.pop()回退！
#         如果写漏pop()，可能导致路径错误或状态串联

def findPath(self, root):
    if root is None:
        return
    # pre-order
    self.path.append(root.val)
    # found startValue node
    if root.val in [self.start, self.end]:
        
        ⚠️必须使用self.path.copy()！！
        ⚠️后续递归继续运行后你会 .pop() 这个 path → 会影响 res 中保存的路径，因为是同一个列表。
        ⚠️你以为保存下来了，但实际只是保存了地址，后续改变了原列表，结果也就被改坏了。
        
        self.res.append(self.path.copy())
        
        ⚠️这里也要self.path.pop()
        ⚠️不能return，
        
    self.findPath(root.left)
    self.findPath(root.right)
    self.path.pop()

# 方法2：使用局部变量path传参 + 手动pop() 📢本质上同方法1
# ✅ 优点：不使用全局变量，更模块化
# ⚠️ 缺点：同样必须手动pop()，否则路径会串

def dfs_with_append(node, path):
    if not node:
        return

    path.append(node.val)

    if not node.left and not node.right:
        print("→", path)

    dfs_with_append(node.left, path)
    dfs_with_append(node.right, path)
    path.pop()  # 手动回退

# 调用
dfs_with_append(root, [])


# 方法3：使用 path + [val] 每层创建新路径列表
# ✅ 优点：路径独立，不需要手动pop()，更安全，不会污染上层状态
# ❌ 缺点：每次递归都新建列表，内存占用稍高（可接受）
# 🔴 目标只是“在叶子节点打印路径”。最终不能取到path的值！！！！
     如果想取path的值，需要return的地方加东西

def dfs_with_append(node, path):
    if not node:
        return

    if not node.left and not node.right:
        print("→", path)

    dfs_with_append(node.left, path + [node.val])
    dfs_with_append(node.right, path + [node.val])
    # 无需手动回退
# 调用
dfs_with_append(root, [])
"""

"""
📢📢📢📢特别笔记📢📢📢📢
🎯 为什么方法3不需要 pop()？
    path + [node.val] 会返回一个新列表对象，原始的 path 不变。
    所以每一层递归的 path 都是干净的副本，天然带“回溯”效果。
    不需要在退出当前层时 pop()，因为你根本就没有修改原列表。
比喻：你复印了一张纸交给别人，他们在副本上写，原件毫无影响。

"""
class Solution1:
    """
    递归思路，
    1. 找到所有路径，后处理 找最短路径
        第一步：找从根节点到 startValue 和 destValue 的路径
        第二步：找它们的公共前缀（LCA 思路）
    """
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        这是一个标准的模版
        ✅ 是的 —— 如果这句返回了 True，就会一级一级地向上传递 True，最终退出整棵递归调用链，下面的 path.pop() 就不会执行了！
        Q: 比如说现在递归到了第五层，出发了return，会退回到第四层，还是直接跳出呢？？
        ✅ 简明回答：
            不会直接跳到最上层，而是会“一级一级往回退”，每一层都 return，最终回到最顶层退出。
        换句话说：
            第五层 return True
            然后第四层接到了这个 True，也执行 return True
            第三层也一样……
            一直到最外层 find_path(root, target, path) 返回 True，整个递归才结束
        1
         \
          2
           \
            3
             \
              4
               \
                5
            每一层 find_path() 调用完下一层后，都要判断返回值：
            if find_path(...):   # 返回 True
                return True      # 把 True 继续返回上去
            find_path(1) → find_path(2) → find_path(3) → find_path(4) → find_path(5)
            这就形成了“一级一级传递 True”的过程。
        """
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()  # 左边失败了，回退
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()  # 右边失败了，回退
            """
            左右边失败了都要回退，之前看的只在后序位置退回的是深度
            """
            return False
        
        # 📢这个方法是错的，只能用下面那种return的
        #path + ['L'] 会创建新路径副本，外部变量不会改变
        #.append() 和 .pop() 会修改传入的列表，能影响外部变量
        # def find_path(node, target, path):
        #     if not node:
        #         return False
        #     if node.val == target:
        #         return True
        #     if find_path(node.left, target, path+['L']):
        #         return True
        #     if find_path(node.right, target, path+['R']):
        #         return True
        #     return False
        
        #不需要额外回溯，但返回的是新路径而不是原地修改。
        def traverse(self, root, target, path):
            if root is None:
                return None
            if root.val == target:
                return path
            left = self.traverse(root.left, target, path + 'L')
            if left is not None:
                return left
            right = self.traverse(root.right, target, path + 'R')
            if right is not None:
                return right
            return None

        path2start = []
        path2end = []
        find_path(root, startValue, path2start)
        find_path(root, destValue, path2end)
        i = 0
        while i < len(path2start) and i < len(path2end) and path2start[i] == path2end[i]:
            i += 1

        return 'U' * (len(path2start) - i) + ''.join(path2end[i:])


# labuladong
class Solution:
    def __init__(self):
        self.path = ""
        self.start_path = ""
        self.end_path = ""
        self.start = None
        self.end = None

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        self.start = startValue
        self.end = destValue
        self.traverse(root)
        p=0
        ls = len(self.start_path)
        le = len(self.end_path)
        while p<ls and p<le and self.start_path[p] == self.end_path[p]:
            p += 1
        new_sp = self.start_path[p:]
        new_ep = self.end_path[p:]
        return "U" * len(new_sp) + new_ep


    def traverse(self, root):
        if root is None:
            return
        if root.val == self.start:
            """
            Python 中的字符串是不可变类型（immutable）
            所以直接复制即可，list就不行哦
            """
            self.start_path = self.path
        elif root.val == self.end:
            self.end_path = self.path

        # left
        self.path += 'L'
        self.traverse(root.left)
        self.path = self.path[:-1]
        
        self.path += 'R'
        self.traverse(root.right)
        self.path = self.path[:-1]

        



# @lc code=end



#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#

