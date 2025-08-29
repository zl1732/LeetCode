#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30201
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    """
    1、确定「状态」，也就是原问题和子问题中会变化的变量。
    2、确定「选择」，也就是导致「状态」产生变化的行为。

    dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        dp = [1]*len(nums)
        # base case：dp 数组全都初始化为 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
        
        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res
    


    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义dp
        dp = [1] * len(nums)
        # 外层
        for i in range(len(nums)):
            # 内层找dp
            for j in range(i):
                # 当前值比前面的大，更新dp
                if nums[i] > nums[j]:
                    """
                    假设你写成：
                    dp[i] = dp[j] + 1  # 没有 max
                    那么你每次都会被最后一个符合条件的 j 覆盖掉，错过前面更优的选择。
                    所以其实是比较不同的dp[j]
                    """
                    #dp[i] = dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1) 
        return max(dp)
    


# 贪心 + 二分查找（时间复杂度 O(n log n)）
class Solution:
    import bisect
    def lengthOfLIS(nums):
        tails = []
        for num in nums:
            # 找到第一个大于等于 num 的位置
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)  # 新增一个更长的子序列
            else:
                tails[idx] = num  # 替换已有长度的结尾更优的值
        return len(tails)


    def lengthOfLIS(self, nums):
        """
        为啥要这样写？不直接用 top = [] 吗？
        ✅ 回答：这是一种 预分配空间 的技巧，提升性能，避免动态扩容

        我们最多会有 len(nums) 堆牌（最坏情况下数组是完全递减）
        所以先预分配 len(nums) 长度的 top 数组（全是 0 占位），节省多次 append 操作的开销
        """
        top = [0] * len(nums)
        # 牌堆数初始化为 0
        piles = 0
        for i in range(len(nums)):
            # 要处理的扑克牌
            poker = nums[i]

            # 搜索左侧边界的二分查找
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            # 没找到合适的牌堆，新建一堆
            if left == piles:
                piles += 1
            # 把这张牌放到牌堆顶
            top[left] = poker
        # 牌堆数就是 LIS 长度
        return piles




# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

