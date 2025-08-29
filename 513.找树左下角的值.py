#
# @lc app=leetcode.cn id=513 lang=python3
# @lcpr version=30201
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque
        q = deque([root])
        
        res = 0
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()

                # 只记录最左侧值
                if i==0:
                    res = cur.val
                # 添加左侧，右侧
                """
                注意:
                这里不要写成root.left，那样永远执行不完的
                跟dfs的traverse()弄混了！
                """
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res


# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,5,6,null,null,7]\n
# @lcpr case=end

#

