#
# @lc app=leetcode.cn id=1104 lang=python3
# @lcpr version=30201
#
# [1104] 二叉树寻路
#

# @lc code=start
"""
我觉得是层序遍历，使用queue bfs，
这个是 二叉堆（优先级队列）原理及实现 章节之后习题
先去看那个https://labuladong.online/algo/data-structure-basic/binary-heap-basic/
"""
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        from collections import deque
        q = deque
# @lc code=end



#
# @lcpr case=start
# 14\n
# @lcpr case=end

# @lcpr case=start
# 26\n
# @lcpr case=end

#

