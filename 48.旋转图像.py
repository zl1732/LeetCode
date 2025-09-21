#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30203
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    """
    先45°翻转，然后对列reverse
    """
    def rotate(self, matrix):
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后反转二维矩阵的每一行
        for row in matrix:
            self.reverse(row)
    
    def reverse(self, arr):
        i, j = 0, len(arr) - 1
        while j > i:
            # swap(arr[i], arr[j]);
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        



# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

