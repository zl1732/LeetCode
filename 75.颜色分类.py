#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30203
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        mn, mx = min(nums), max(nums)
        offset = -mn

        # count
        count = [0] * (mx-mn+1)
        for num in nums:
            count[num+offset] += 1
        
        # cumsum
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        # output
        out =  [0]* len(nums)
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            out[count[num + offset]-1] = num
            count[num + offset] -= 1
        # return out[1:]"""out[1:]这是切片复制操作，不要这样"""
        
        for i in range(len(nums)):
            nums[i] = out[i]


        
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

