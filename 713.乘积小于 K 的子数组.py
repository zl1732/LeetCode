#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30203
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        #注意：
        外层更新right，所以遍历添加结果，以right为锚

        在这个题里，滑动窗口的套路就是 固定 right（右端点），枚举所有以它结尾的子数组。
        为什么要固定右端点？
            因为窗口每次是靠 右端点扩张 的。
            这样一来，每次往右走一步，只产生一批新的子数组，不会跟之前重复。

        如果固定左端点会怎样？
            比如你写的这种“枚举 left 开头”：
            每次 right 增加时，你都会重新生成一堆 [nums[left:…]]，这些子数组里有的在上一步已经出现过了。
            结果就是 重复记录。
        """
        n = len(nums)
        left = right = 0
        window_dot = 1
        res = 0
        detail= []
        while right < n:
            num = nums[right]
            window_dot *= num
            right += 1

            while window_dot >= k:
                num = nums[left]
                window_dot /= num
                left += 1
            
            # 这里其实不需要if 了
            if window_dot < k:
                # # 更新左端点开始的数组，错误
                # for i in range(left, right+1):
                #     detail.append(nums[left:i])
                # # 正确
                # for i in range(left, right):
                #     detail.append(nums[i:right])
                res += (right - left)
        return res


    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """# ✅ 特殊情况，任何子数组乘积都 ≥ 1"""
        if k <= 1:   
            return 0
        n = len(nums)
        left = right = 0
        window_dot = 1
        res = 0
        while right < n:
            num = nums[right]
            window_dot *= num
            right += 1

            while window_dot >= k:
                num = nums[left]
                window_dot /= num
                left += 1
            
            res += (right - left)
        return res
    

    # gpt
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

