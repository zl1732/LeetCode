#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30203
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        target = 0
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            # 对 target - nums[i] 计算 twoSum
            tuples = self.twoSumTarget(nums, i + 1, target - nums[i])
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
            # 跳过第一个数字重复
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def threeSum(self, nums):
        target = 0
        nums.sort()
        res = []
        i = 0
        for i,num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            remain = target - num
            tuples = self.twoSumTarget(nums, i+1, remain)
            for tuple in tuples:
                res.append([num]+tuple)
            """
            位置错，i= 0,时候，i-1 = -1,应该放在开头判断
            """
            # if nums[i] == nums[i-1]:
            #     continue
        return res


    """
    关于 twoSumTarget 里 if/elif/else 和 if/if/if 的区别：

    1. 常见写法是 if/elif/else
    - 三个条件互斥，只会命中其中一个分支
    - 语义清晰：要么 sum < target，要么 sum > target，要么 sum == target
    - 一次循环中最多只会移动 lo 或 hi，或者保存一次解

    2. 如果写成三个独立的 if
    - 条件依然互斥，所以实际上效果大部分时候是一样的
    - 当 sum == target 时，只会进入第三个 if，前两个 if 不会触发
    - 第三个 if 里有 while 去重逻辑：
            while lo < hi and nums[lo] == left: lo += 1
            while lo < hi and nums[hi] == right: hi -= 1
        → 这能保证重复的数被跳过，因此不会多次加入相同解

    3. 为什么推荐 if/elif/else
    - 语义更清晰：别人一看就明白三种情况互斥
    - 更健壮：如果以后修改了第三个分支（比如只写 lo += 1 而忘了去重），
        那 if/if/if 版本更容易出 bug
    - 效率略高：if/elif/else 命中后直接跳过后续判断，if/if/if 每次都会检查三次条件

    结论：
    - 有 while 去重的情况下，if/if/if 也能避免重复解。
    - 但写成 if/elif/else 更直观、更安全，推荐使用。
    """
    def twoSumTarget(self, nums: List[int],start, target: int) -> List[int]:
        lo, hi = start, len(nums) - 1
        res = []

        while lo < hi:
            sum = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            # 左侧去重，仅去重，结束后会重新开始while
            if sum < target:
                while lo < hi and nums[lo] == left: 
                    lo += 1
            # 同上
            elif sum > target:
                while lo < hi and nums[hi] == right: 
                    hi -= 1
            # 上面去重结束后才会来到这一步
            else:
                res.append([left, right])
                # 继续去重
                while lo < hi and nums[lo] == left: 
                    lo += 1
                while lo < hi and nums[hi] == right: 
                    hi -= 1
        return res
                
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

