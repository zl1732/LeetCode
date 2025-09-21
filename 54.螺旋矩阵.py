#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30203
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    """
    边界收缩法

        外层必须是 while len(res) < m*n 或 while top <= bottom and left <= right。

        因为内部是「批量走一条边」，不是一步一步走。

    方向向量法

        外层可以是 for _ in range(m*n)，因为每轮都只加一个元素。

        不需要担心越界，只要每次判断转向就行。
    """
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        top, bottom, left, right = 0, m - 1, 0, n - 1
        #for _ in range(m * n): # 是错的
        while len(res) < m*n:
            # 从左到右
            if top <= bottom:
                for j in range(left, right + 1):
                    res.append(matrix[top][j])
                top += 1
            # 从上到下  # 也不能用elif，因为从上到下走的，否则被跳过
            if left <= right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
            # 从右到左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res



class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        res = []
        
        # 方向向量: 右, 下, 左, 上
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        row, col, dir_idx = 0, 0, 0
        
        for _ in range(m * n):
            res.append(matrix[row][col])
            visited[row][col] = True
            """
            必须先计算一次，如果先判断方向，第一次没有next_col，会报错
            """
            next_row, next_col = row + dirs[dir_idx][0], col + dirs[dir_idx][1]
            # 如果越界或已访问，换方向
            if not (0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]):
                dir_idx = (dir_idx + 1) % 4
                next_row, next_col = row + dirs[dir_idx][0], col + dirs[dir_idx][1]
            row, col = next_row, next_col
        
        return res



class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        top, bottom, left, right = 0, m-1, 0, n-1
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]  # 右, 下, 左, 上
        row, col, dir_idx = 0, 0, 0
        
        for _ in range(m * n):
            res.append(matrix[row][col])
            # 预测下一步
            next_row, next_col = row + dirs[dir_idx][0], col + dirs[dir_idx][1]
            
            # 判断是否需要转向
            if dir_idx == 0 and next_col > right:   # 右 → 下
                dir_idx = 1
                top += 1
                """
                注意这里是elif
                """
            elif dir_idx == 1 and next_row > bottom: # 下 → 左
                dir_idx = 2
                right -= 1
            elif dir_idx == 2 and next_col < left:   # 左 → 上
                dir_idx = 3
                bottom -= 1
            elif dir_idx == 3 and next_row < top:    # 上 → 右
                dir_idx = 0
                left += 1
            
            # 更新坐标
            row += dirs[dir_idx][0]
            col += dirs[dir_idx][1]
        
        return res


# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

