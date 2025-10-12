#
# @lc app=leetcode.cn id=566 lang=python3
# @lcpr version=30203
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                """
                这样会直接覆盖掉原来的目标行列数参数，之后循环再用就乱套了。
                比如第二次循环开始时，r 已经不是原来的行数了。

                计算函数也是错的

                """
                r = i*j//c
                c = i*j%c
                res[r][c] = mat[i][j]
        return res




class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        res = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                k = i * n + j  # 展平
                new_i = k // c
                new_j = k % c
                res[new_i][new_j] = mat[i][j]
        return res



# @lc code=end



#
# @lcpr case=start
# [[1,2],[3,4]]\n1\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n2\n4\n
# @lcpr case=end

#

