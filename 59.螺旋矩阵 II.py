#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30203
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        num = 1
        left, top = 0,0
        right, bottom = n-1, n-1
        while num <= n*n:
            # 向右侧
            if top <= bottom:
                for j in range(left, right+1):
                    matrix[top][j] = num
                    num += 1
                top += 1
            if left <= right:
                for i in range(top, bottom+1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
            if top <= bottom:
                for j in range(right, left-1,-1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        return matrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[False]*n for _ in range(n)]
        res = [[0]*n for _ in range(n)]
        num = 1

        # 右，下，左，上
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        i, j, di = 0,0,0

        for _ in range(n*n):
            res[i][j] = num
            visited[i][j] = True

            ni, nj = i + dirs[di][0], j + dirs[di][1]
            if not (0<=ni<n and 0<=nj<n and not visited[ni][nj]):
                di += 1
                di %= 4
                ni, nj = i + dirs[di][0], j + dirs[di][1]
            i, j = ni, nj
            # update num
            num += 1
        return res


    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[False]*n for _ in range(n)]
        res = [[0]*n for _ in range(n)]
        num = 1

        # 右，下，左，上
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        top, bottom, left, right = 0, n-1, 0, n-1
        i, j, di = 0,0,0

        for _ in range(n*n):
            res[i][j] = num
            ni, nj = i + dirs[di][0], j + dirs[di][1]

            if di == 0 and nj > right:
                di = 1
                top += 1

            elif di == 1 and ni > bottom:
                di = 2
                right -=1
            
            elif di == 2 and nj < left:
                di = 3
                bottom -= 1
            
            elif di ==3 and ni < top:
                di = 0
                left += 1
            """
            更新i,j!!
            注意要用新的方向更新，不能直接用ni,nj，那个只是试探性的
            """
            #i, j = ni, nj
            i += dirs[di][0]
            j += dirs[di][1]
            """
            注意更新num
            """
            num += 1
        return res


# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

