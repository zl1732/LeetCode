#
# @lc app=leetcode.cn id=1696 lang=python3
# @lcpr version=30203
#
# [1696] 跳跃游戏 VI
#

# @lc code=start
class Solution:
    """
    元素间隔不超过 k 的最大子序列和
    子序列的第一个元素必须是 nums[0]，最后一个元素必须是 nums[-1]。
    i-1...i-k+1 -> i
    max(nums[i-k+1],...nums[i-1]) + nums[i]
    这里因为必须从第一步开始，所以不能
    max(nums[i-k],...nums[i-1] + nums[i], nums[i])

    从上而下：
    if i == 0:
        return nums[0]
    return dp + max(dp...)
    

    从下而上：
    maxR[0] = nums[0]
    for i in range(1, n):
        maxR[i] = max(i-j) for j in range(1, k+1) +nums[i]
    """
    # 从上而下 with-memo
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.memo = {}
        return self.dp(nums, n-1, k)
        
    def dp(self, nums, i, k):
        if i <= 0:
            return nums[0]
        
        #加入memo
        if i in self.memo:
            return self.memo[i]

        res = float('-inf')
        for j in range(1, k+1):
            res = max(res, self.dp(nums, i-j, k))
        self.memo[i] = res + nums[i]
        return self.memo[i]
        
    # 这个从上到下的没法加入单调队列快速计算max，必须用从下而上



    # 从下而上
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(1,k+1):
                # 这种写法不错，代替用max(i-j, 0)
                # lookBack = max(i-j, 0)
                if i - j < 0:
                    continue
                # 直接在dp[i]的基础上计算max就行
                # temp = max(temp, dp[i-j])
                dp[i] = max(dp[i], dp[i - j])
            dp[i] += nums[i]
        return dp[n-1]
    

    # 从下而上 用单调队列快速计算max值
    from collections import deque
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        q = deque([0])
        for i in range(1, n):
            # 维护长度
            while q and q[0] < i - k:
                q.popleft()
            
            """ 注意是dp[q[0]]"""
            dp[i] = dp[q[0]] + nums[i]

            # push
            """
            注意：
            是dp[i] 不能用 nums[i] 了！！
            >= 如果出现相等的值，会把前面的旧索引也弹掉；队列里不会存在两个相同 dp 值，只保留最新的那个。
            """
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)

        return dp[n-1]
    


        
# @lc code=end



#
# @lcpr case=start
# [1,-1,-2,4,-7,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,-5,-2,4,0,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,-5,-20,4,-1,3,-6,-3]\n2\n
# @lcpr case=end

#

