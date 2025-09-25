#
# @lc app=leetcode.cn id=867 lang=python3
# @lcpr version=30203
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        3. 可读性
        面试官/同事看你写 i - j、逆序、pop，会觉得“这是在做对角线遍历吗？”，思路被绕偏。
        这种题考察点就是 下标翻转，写太复杂反而减分。
        """
        # # 仅用于方阵，可以原地反转
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix
        m = len(matrix)
        n = len(matrix[0])
        diags = defaultdict(list)
        # 0, -1, -2
        for i in range(m):
            for j in range(n):
                diags[i-j].append(matrix[i][j])
        
        for key in diags:
            diags[key] = diags[key][::-1]

        res = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = diags[j-i].pop()

        return res
    
    """
    标准解法，来自方阵反转那个版本
    """
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res
        


        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

