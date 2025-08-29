#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30201
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.target = targetSum
        self.traverse_all_nodes(root)
        return self.res
    
    def traverse(self, root, curSum):
        if root is None:
            return
        # 更新当前节点
        curSum += root.val

        # 找到一条路径
        if curSum == self.target:
            self.res+=1
            #curSum = curSum - root.val

        self.traverse(root.left, curSum)
        self.traverse(root.right, curSum)
        
    """
    差点就作对了，已经想到这个思路，但是怕重复性太多
    但是不能写#curSum = curSum - root.val这行。
    5 → 3 → -2 → 2
    你在遍历到 5 → 3 时满足了 curSum == 8，然后你减掉了 node.val，curSum 变成 5，等你到了 -2 → 2 时就找不到 8 了。
    但实际上：
    5 → 3 = 8
    5 → 3 → -2 = 6
    5 → 3 → -2 → 2 = 8 ← 也是合法路径
    """
    # 遍历每个节点，作为路径起点
    def traverse_all_nodes(self, node):
        if node is None:
            return
        self.traverse(node, 0)  # 从当前节点开始尝试路径
        self.traverse_all_nodes(node.left)  # 尝试左子树
        self.traverse_all_nodes(node.right)  # 尝试右子树


"""
✅ 方式二：前缀和 + 哈希表（真正的滑动窗口思想）
这个答案后面再回来看可以

      10
     /  \
    5   -3
   / \    \
  3   2    11
目标值 target = 8，我们要找所有路径（不一定从根）和为8的。
递归走到 5 → 3 时：
    路径和是 10 + 5 + 3 = 18
    查找哈希表中有没有 18 - 8 = 10：有！说明存在一条从 10 到 5 → 3 之间的路径和是8！
1️⃣ 走到 10：
    curr_sum = 0 + 10 = 10
    查找 prefix_count[10 - 8] = prefix_count[2] → 没有
    更新 prefix_count[10] += 1 → {0:1, 10:1}
    进入左子树 5

2️⃣ 走到 5：
    curr_sum = 10 + 5 = 15
    查找 prefix_count[15 - 8] = prefix_count[7] → 没有
    更新 prefix_count[15] += 1 → {0:1, 10:1, 15:1}
    进入左子树 3

3️⃣ 走到 3：
    curr_sum = 15 + 3 = 18
    查找 prefix_count[18 - 8] = prefix_count[10] = 1 ✅ 找到了
    res += 1 → res = 1
    更新 prefix_count[18] += 1 → {0:1, 10:1, 15:1, 18:1}
    左右为空，回溯：prefix_count[18] -= 1 → {0:1, 10:1, 15:1, 18:0}

⬅️ 回到 5，去右子树 2：
    curr_sum = 15 + 2 = 17
    查找 prefix_count[17 - 8] = prefix_count[9] → 没有
    更新 prefix_count[17] += 1 → {..., 17:1}
    回溯：prefix_count[17] -= 1
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0

            # 当前路径的累计和
            curr_sum += node.val

            # 查找从哪个之前的点出发，能让路径和是 target
            res = prefix_count[curr_sum - targetSum]

            # 记录当前路径和出现次数（进入当前节点）
            prefix_count[curr_sum] += 1

            # 遍历左右子树
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)

            # 回溯，离开当前节点时要撤销影响
            prefix_count[curr_sum] -= 1

            return res

        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # base case：前缀和为0的路径出现1次
        return dfs(root, 0)


# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

