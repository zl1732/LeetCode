#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30203
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        k = m * n  # len

        left, right = 0, k-1
        while left <= right:
            mid = left + (right-left) //2
            i, j = mid//n, mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid-1
        return False
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

