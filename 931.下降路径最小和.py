#
# @lc app=leetcode.cn id=931 lang=python3
# @lcpr version=30201
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution1:
    """
    我的思路：
    一行一行往下走，记录每行每个点位的最好值
    """
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        w,h = len(matrix[0]), len(matrix)
        """
        它创建了 h 个对同一个列表对象的引用，导致你在修改 dp[i][j] 时，会同时修改 dp 中所有的行！
            dp = [row, row, row, ..., row]  
            # 一共 h 个 row，但其实都是同一个对象！
        
        也就是说：
            每一行 dp[i] 都是同一个列表对象的引用（指向同一块内存地址）。
            当你写 dp[0][0] = 7，其实是修改了这个公共的 row[0]，其他行的第 0 列也会变成 7！
        
        举例：
            a = [[0]*3]*2
            a[0][0] = 1
            print(a)  # 输出 [[1, 0, 0], [1, 0, 0]]

        """
        #dp = [[0] * w] * h
        dp = [[0] * w for _ in range(h)]
        dp[0] = matrix[0]
        for i in range(1,h):
            for j in range(w):
                if j==0:
                    dp[i][j] = min(matrix[i][j] + dp[i-1][j],
                                matrix[i][j] + dp[i-1][j+1])
                elif j==w-1:
                    dp[i][j] = min(matrix[i][j] + dp[i-1][j-1],
                                matrix[i][j] + dp[i-1][j])
                else:
                    dp[i][j] = min(matrix[i][j] + dp[i-1][j-1],
                                matrix[i][j] + dp[i-1][j],
                                matrix[i][j] + dp[i-1][j+1])
        return min(dp[-1])

    """
    ✅ 解决方法是：使用两个数组，轮流交替（prev 和 curr）
    也就是说：
        prev 存上一行的数据，已经确定，不动。
        curr 是我们正在计算的当前行。
        每次算完当前行后，把 curr 赋值给 prev，进入下一轮。
    """
    def minFallingPathSum(matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[0][:]
        
        for i in range(1, n):
            curr = [0] * n
            for j in range(n):
                min_above = prev[j]
                
                if j > 0:
                    min_above = min(min_above, prev[j-1])
                if j < n - 1:
                    min_above = min(min_above, prev[j+1])
                curr[j] = matrix[i][j] + min_above
            prev = curr  # 下一轮作为上一行
        return min(prev)
    

class Solution:
    """
    从上而下，递归
    """
    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = float("inf")
        # 终点可能在最后一行的任意一列
        for j in range(m):
            res = min(res, self.dp(matrix, n - 1, j))
        return res
    

    def dp1(self, matrix: List[List[int]], i: int, j: int) -> int:
        # 非法索引检查
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            # 返回一个特殊值
            return float('inf')
        # base case
        if i == 0:
            return matrix[i][j]
        # 状态转移
        return matrix[i][j] + min( 
                self.dp(matrix, i - 1, j), 
                self.dp(matrix, i - 1, j - 1), 
                self.dp(matrix, i - 1, j + 1)
            )
    

    # # 自己写的第一遍
    # def dp(matrix: List[List[int]], i: int, j: int) -> int:
    #     # 非法索引检查
    #     """
    #     ❌ Bug 1：索引越界判断条件写错了
    #     """
    #     if i < 0 or j < 0 or i > len(matrix) or j > len(matrix[0]):
    #         return float('inf')
    #     # 第一排
    #     if i == 0:
    #         return matrix[0][j]
    #     """
    #     ❌ Bug 2：你没有递归调用 dp() 本身
    #     正确写法会回到上面 if i == 0:这个case正好是 matrix[i-1][j-1]
    #     """
    #     # return min(matrix[i][j] + matrix[i-1][j-1],
    #     #            matrix[i][j] + matrix[i-1][j],
    #     #            matrix[i][j] + matrix[i-1][j+1])
    #     return matrix[i][j] + min( 
    #         dp(matrix, i - 1, j), 
    #         dp(matrix, i - 1, j - 1), 
    #         dp(matrix, i - 1, j + 1)
    #     )
    

    # 自己写第二遍
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 非法索引检查
        self.memo = {}
        n = len(matrix)
        m = len(matrix[0])
        res = float("inf")
        # 终点可能在最后一行的任意一列
        for j in range(m):
            res = min(res, self.dp(matrix, n - 1, j))
        return res   
    
    def dp(self, matrix: List[List[int]], i: int, j: int) -> int:
        if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
            return float('inf')
        
        if i==0:
            return matrix[0][j]
        
        """ 注意可以直接存pair作为key"""
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        self.memo[i,j] = matrix[i][j] + min(
            self.dp(matrix, i-1, j-1),
            self.dp(matrix, i-1, j),
            self.dp(matrix, i-1, j+1))
        
        return self.memo[i,j]





# @lc code=end



#
# @lcpr case=start
# [[2,1,3],[6,5,4],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[-19,57],[-40,-5]]\n
# @lcpr case=end

#

