#
# @lc app=leetcode.cn id=1124 lang=python3
# @lcpr version=30203
#
# [1124] 表现良好的最长时间段
#

# @lc code=start
class Solution:
    """
    >8 1
    <8 -1
    
    """
    def longestWPI(self, hours: List[int]) -> int:
        preSum = 0
        count = {0:-1}
        max_len = 0
        for i, hour in enumerate(hours):
            preSum += -1 if hour <=8 else 1
            if preSum-1 in count:
                length = i - count[preSum-1]
                max_len = max(max_len, length)
                print(i, count[preSum-1], max_len)
            else:
                count[preSum] = i
            """ 错误
            1. 560 题 / 974 题
            题目问的是 子数组个数。
            逻辑是：
            如果 preSum - k 出现过，说明存在某段子数组和为 k。
            那么一共有多少个，就要把 count[preSum-k] 累加进答案。
            所以我们要存「某个前缀和出现的次数」，因为次数直接决定了子数组的个数。
            """
        return max_len


    def longestWPI(self, hours: List[int]) -> int:
        preSum = 0
        count = {0: -1}
        max_len = 0
        for i, hour in enumerate(hours):
            preSum += 1 if hour > 8 else -1
            if preSum > 0:
                max_len = i + 1
            elif preSum - 1 in count:
                max_len = max(max_len, i - count[preSum - 1])
            if preSum not in count:  # 只记录最早出现
                count[preSum] = i
        return max_len

        
# @lc code=end



#
# @lcpr case=start
# [9,9,6,0,6,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6]\n
# @lcpr case=end

#

