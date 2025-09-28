#
# @lc app=leetcode.cn id=525 lang=python3
# @lcpr version=30203
#
# [525] 连续数组
#

# @lc code=start
class Solution:
    """
    2. 525 题

    题目问的是 子数组的最大长度。

    逻辑是：

    如果某个 count 在两个位置 i 和 j 都出现过（i < j），说明 (i, j] 区间和为 0。

    那么子数组长度 = j - i。

    这里需要的是「第一次出现的下标」，因为第一次出现的位置越靠前，区间就越长。

    所以我们要存「前缀和第一次出现的位置 i」，而不是出现次数。
    """
    def findMaxLength(self, nums: List[int]) -> int:
        count= {0:-1}
        preSum = 0
        max_len = 0
        for i, num in enumerate(nums):
            preSum += 1 if num == 1 else -1
            if preSum in count:
                prev_idx = count[preSum]
                length = i - prev_idx
                max_len = max(max_len, length)
            else:
                count[preSum] = i
        return max_len


        
# @lc code=end



#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,1,1,0,0,0]\n
# @lcpr case=end

#

