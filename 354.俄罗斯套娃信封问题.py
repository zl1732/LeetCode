#
# @lc app=leetcode.cn id=354 lang=python3
# @lcpr version=30201
#
# [354] Russian Doll Envelopes
#

# @lc code=start
"""
首先，对宽度 w 从小到大排序，确保了 w 这个维度可以互相嵌套，所以我们只需要专注高度 h 这个维度能够互相嵌套即可。
其次，两个 w 相同的信封不能相互包含，所以对于宽度 w 相同的信封，对高度 h 进行降序排序
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
# @lc code=end



#
# @lcpr case=start
# [[5,4],[6,4],[6,7],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1],[1,1]]\n
# @lcpr case=end

#

