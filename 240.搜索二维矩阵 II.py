#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30203
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # start: 0, n-1
        i, j = 0, n-1
        while i < m and j >= 0: #"""注意是>="""
            cur = matrix[i][j]
            if target > cur: # down
                i += 1
            elif target < cur:
                j -= 1
            elif target == cur:
                return True
        return False
                


# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

