#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30203
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 方法1
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        self.dfs(root)
        return root
    
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        self.dfs(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
    # 方法2 标准后续
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 

        self.flatten(root.left)
        self.flatten(root.right)

        left, right = root.left, root.right
        root.left = None
        root.right = left

        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right

    
    # 遍历 从上而下
    def flatten(self, root):
        if not root:
            return None
        stack = [root]
        prev = None
        while stack:
            cur = stack.pop()
            if prev:
                prev.left = None
                prev.right = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            prev = cur
            
    
        


# @lc code=end


"""
递归写法，同方法1
注意这是个前序 -> DFS
所以不能用 queue + popleft (BFS)
    popleft() 意味着你用的是 队列 (FIFO)，也就是广度优先遍历（层序遍历）。
    但题目要的是 前序遍历 (root → left → right)。

    前序遍历要求“先访问左子树，再访问右子树”，是 深度优先 行为，要用栈 (LIFO)。
    所以这里应该用 pop() + stack
"""
def flatten(root):
    if not root: return
    stack = [root]
    prev = None
    while stack:
        cur = stack.pop()
        if prev:
            prev.left = None
            prev.right = cur
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        prev = cur



"""
方法一：反后序（右→左→根）+ prev 指针
“逆向构建”：先把整棵树的尾部（前序里的最后一个节点）处理好，然后逐步往前接；

因为前序是 root,left,right，反过来就是 right,left,root；

prev 始终指向“我应该把当前 node 的 right 指到哪儿去”。

小步干跑（举例）

树：

    1
   / \
  2   5
 / \   \
3  4    6

递归顺序：6 → 5 → 4 → 3 → 2 → 1
处理 6：6.right = None，prev = 6
回到 5：5.right = 6，prev = 5
回到 4：4.right = 5，prev = 4
回到 3：3.right = 4，prev = 3
回到 2：2.right = 3，prev = 2
回到 1：1.right = 2，prev = 1
同时每步都把 node.left = None。最终是 1→2→3→4→5→6。
"""
class Solution:
    def flatten(self, root):
        self.prev = None

        def dfs(node):
            if not node:
                return
            dfs(node.right)   # 先处理右
            dfs(node.left)    # 再处理左

            # 把当前节点接到已经整理好的链表前面
            node.right = self.prev
            node.left = None
            self.prev = node  # 更新“下一节点”

        dfs(root)


"""
方法二：真正后序（左→右→根）+ 原地“拼接”
Step 1. flatten(3)

    3 没左右 → 返回。
    3 已经是单节点链表：3

Step 2. flatten(4)

    同理，4 → 4

Step 3. flatten(2)

    此时：
    flatten(2.left) 让 3 成了链；
    flatten(2.right) 让 4 成了链。
    所以现在左、右子树都已经各自“线性化”：

    2
    ├─left: 3
    └─right: 4
    （左子树 3 已经是一条链，右子树 4 也是一条链）

    开始执行拼接逻辑：

    left, right = root.left, root.right   # left=3, right=4
    root.left = None
    root.right = left     # 现在 2.right → 3

    变成：
    2
    \
    3
    \
    (原 left 的子结构)

    然后找 3 这条链的末尾（其实就是 3 自己），让它的 right 指向原来的 right=4：
    2
    \
    3
    \
    4
    ✅ 现在 2 这一整棵子树变成了一条右链：2→3→4
"""

def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)

    left, right = root.left, root.right
    root.left = None
    root.right = left

    # 找左链尾巴
    tail = root
    while tail.right:
        tail = tail.right
    tail.right = right


#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

