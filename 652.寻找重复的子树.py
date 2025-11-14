#
# @lc app=leetcode.cn id=652 lang=python3
# @lcpr version=30203
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    #     self.res = []
    #     self.seen = set()
    #     self.path = []
    #     self.findSub(root)
    #     return self.res

    # def findSub(self, root):
    #     if not root:
    #         return
    #     # 叶子
    #     if not root.left and not root.right:
    #         self.seen.add(self.path)

    #     # 前序遍历找
    #     self.path.append(root.val)

    #     if self.path in self.seen:
    #         self.res.append(self.path)

    #     # 左右子树
    #     self.findSub(root.left)
    #     self.findSub(root.right)
        
    #     # 手动回滚
    #     self.path.pop()

    """
        if self.seen.get(cur, 0):
            ...
        else:
            self.seen[cur] += 1
        会报错，如果没有cur，也会进入else！！！
    
    背诵：
        freq = self.seen.get(cur,0)
        if freq ==1:
            self.res.append(root)
        self.seen[cur] = freq + 1

        ### self.seen[cur] = self.seen.get(cur,0) + 1
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.seen = {}
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        # 还是要记录子树的全部结构（空缺位置），否则无法判断是否为同一个
        if not root:
            return "Null"
        
        # 左右子树
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # 后序位置
        cur = left + "," + right + "," + str(root.val)
        
        freq = self.seen.get(cur, 0)
        if freq == 1:
            self.res.append(root)
        self.seen[cur] = freq + 1
        return cur


"""
ID 压缩

用三元组 key = (left_id, node.val, right_id) 来唯一表示当前子树（结构+值）。
维护一个字典 triplet_to_id：把从未见过的 key 分配一个新 ID；见过就复用旧 ID。
维护一个计数表 id_freq：ID 出现次数从 1 变 2 的那一刻，把当前节点加入答案（防止重复加入多次）。
递归返回当前子树的 ID，而不是字符串。

小例子（手动走一遍）
以树：

      1
     / \
    2   3
   /   / \
  4   2   4
     /
    4

空子树 None → 0
叶子 4：(0,4,0) → 分配 id=1
子树 2(4, None)：(1,2,0) → 分配 id=2
右侧叶子 4 又是 (0,4,0) → 复用 id=1，频次从 1→2，收集这个 4 的根节点
右子树根 3：左 id=2，右 id=1，(2,3,1) → id=3
最顶 1：左 id=2，右 id=3，(2,1,3) → id=4
左侧子树 2(4,None) 再次出现时 id=2 频次从 1→2，收集这个 2 的根节点
"""
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root):
        triplet2id = {}               # (left_id, val, right_id) -> id
        cnt = defaultdict(int)        # id -> 出现次数
        next_id = 1                   # 0 预留给空
        ans = []

        def dfs(node):
            nonlocal next_id
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            key = (l, node.val, r)
            if key not in triplet2id:
                triplet2id[key] = next_id
                next_id += 1
            cur = triplet2id[key]
            cnt[cur] += 1
            if cnt[cur] == 2:
                ans.append(node)
            return cur

        dfs(root)
        return ans

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,null,2,4,null,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,null,3,null]\n
# @lcpr case=end

#

