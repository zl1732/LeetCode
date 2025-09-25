#
# @lc app=leetcode.cn id=1329 lang=python3
# @lcpr version=30203
#
# [1329] 将矩阵按对角线排序
#

# @lc code=start
class Solution:
    """
    观察对角线，横纵坐标之差是相同的
    比如 (0,0)、(1,1)、(2,2) 的差值都是 0，说明在同一条对角线上。
    """
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diags = defaultdict(list)
        
        # 收集所有对角线
        for i in range(m):
            for j in range(n):
                diags[i - j].append(mat[i][j])
        # 对每条对角线排序（逆序存储，方便pop）
        for key in diags:
            diags[key].sort(reverse=True)
        # print(diags)
        # 写回矩阵
        """ 这里写的不错注意下 """
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i - j].pop()
        
        return mat
    


    
# @lc code=end



#
# @lcpr case=start
# [[3,3,1,1],[2,2,1,2],[1,1,1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]\n
# @lcpr case=end

#

