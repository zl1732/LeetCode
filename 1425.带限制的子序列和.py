#
# @lc app=leetcode.cn id=1425 lang=python3
# @lcpr version=30203
#
# [1425] 带限制的子序列和
#

# @lc code=start
class Solution:
    """
    本题和1696的区别是可以单独新起一个
    max(nums[i], dp[...] + nums[i])
    """
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        from collections import deque
        q = deque([0])
        for i in range(1, n):
            while q and q[0] < i-k:
                q.popleft()
            
            # update res
            dp[i] = max(dp[q[0]], 0) + nums[i]

            # push
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        """
        注意返回最大值
        """
        return max(dp)
        
# @lc code=end



#
# @lcpr case=start
# [10,2,-10,5,20]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,-3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [10,-2,-10,-5,20]\n2\n
# @lcpr case=end

#

