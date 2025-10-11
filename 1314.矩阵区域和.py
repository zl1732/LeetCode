#
# @lc app=leetcode.cn id=1314 lang=python3
# @lcpr version=30203
#
# [1314] 矩阵区域和
#

# @lc code=start
class Solution:
    """
    sum(x1,y1,x2,y2) = pre[x2+1][y2+1] - pre[x1][y2+1] - pre[x2+1][y1] + pre[x1][y1]
                                                   |           |
    """
    def __init__(self):
        self.preSum = None

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        self.buildPreSum(mat)
        out =  [[0] * n for _ in range(m)]
        print(self.preSum)
        for i in range(m):
            for j in range(n):
                # 左上角
                x1 = max(i-k,0)
                y1 = max(j-k,0)
                # 右下角
                x2 = min(i+k,m-1)
                y2 = min(j+k,n-1)
                """ 注意中间两个+1的位置，分在x和y"""
                # out[i][j] = (self.preSum[x2+1][y2+1] - self.preSum[x2][y1+1] -
                #              self.preSum[x1][y2+1] + self.preSum[x1][y1])
                out[i][j] = (self.preSum[x2+1][y2+1] - self.preSum[x2+1][y1] -
                             self.preSum[x1][y2+1] + self.preSum[x1][y1])
        return out


    def buildPreSum(self, mat):
        m, n = len(mat)+1, len(mat[0])+1
        self.preSum = [[0] * n for _ in range(m)]
        """
        下标从1开始！！！
        """
        for i in range(1, m):
            for j in range(1,n):
                self.preSum[i][j] = (self.preSum[i-1][j] + self.preSum[i][j-1] -
                                     self.preSum[i-1][j-1] + mat[i-1][j-1])
<<<<<<< HEAD
    

=======
>>>>>>> b0d0ed76e32d11849717c8194682fdfeeb87ce5a
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n2\n
# @lcpr case=end

#

