#
# @lc app=leetcode.cn id=1260 lang=python3
# @lcpr version=30203
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    """
    🔹思路
    把二维数组“摊平成一维数组”，做循环右移，然后再 reshape 回二维。
    假设 m = len(grid)，n = len(grid[0])，总长度 L = m * n。
    计算右移后的位置：newIndex = (oldIndex + k) % L。
    根据新位置重新构建二维数组。
    """
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        L = m * n
        k %= L

        # 拉平成一维
        # flat = [grid[i][j] for i in range(m) for j in range(n)]
        flat = []
        for i in range(m):
            for j in range(n):
                flat.append(grid[i][j])


        # 右移1
        # flat = flat[-k:] + flat[:-k]
        # 右移2
        shifted = [0] * L
        for idx in range(L):
            new_idx = (idx + k) % L
            shifted[new_idx] = flat[idx]
        

        # # 右移3：三次反转
        # self.reverse(flat, 0, L - 1)
        # self.reverse(flat, 0, k - 1)
        # self.reverse(flat, k, L - 1)

        # reshape 回 m x n
        # return [flat[i*n:(i+1)*n] for i in range(m)]
        res = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(shifted[i * n + j])
            res.append(row)
        return res

    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n9\n
# @lcpr case=end

#

