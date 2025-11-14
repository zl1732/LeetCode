#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30203
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        return self.count(0, n-1)
        
    def count(self, lo, hi):
        # [1] [2]
        if lo > hi:
            return 1
        
        # [1, 2] lo=0 hi=1
        # [1] + ([2], None)  [2] + (None, [1])  
        res = 0
        for i in range(lo, hi+1):
            left = self.count(lo, i-1)
            right = self.count(i+1, hi)
            res += left * right
        return res
        

    """
    memo version
    """
    def numTrees(self, n: int) -> int:
        self.memo = {}
        return self.count(0, n-1)
        
    def count(self, lo, hi):
        # [1] [2]
        if lo > hi:
            return 1
        
        if (lo, hi) in self.memo:
            return self.memo[(lo, hi)]
        
        res = 0
        for i in range(lo, hi+1):
            left = self.count(lo, i-1)
            right = self.count(i+1, hi)
            res += left * right
        self.memo[(lo, hi)] = res
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

