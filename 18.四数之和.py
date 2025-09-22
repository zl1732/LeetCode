#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30203
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i, n = 0, len(nums)
        while i < n:
            cur =  nums[i]
            remain = target - cur
            # call 3sum to get tuples
            tuples = self.threeSum(nums, i+1, remain)
            for tuple in tuples:
                res.append([cur] + tuple)
            # if next cur is same, skip
            """
            注意两种写法：
            第一种写法：“往前看” 去重，总会先跳一步
            第二种写法：“往后看” 去重，如果不相同就需要手动跳一步
            """
            # # 方法1
            # while i< n and nums[i] == cur:
            #     i += 1
            # # i+= 1

            # 方法2
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def threeSum(self, nums, start, target):
        res = []
        i, n = start, len(nums)
        while i < n:
            cur =  nums[i]
            remain = target - cur
            tuples = self.twoSum(nums, i+1, remain)
            for tuple in tuples:
                res.append([cur] + tuple)
            # 方法2
            while i< n and nums[i] == cur:
                i += 1
            # i+=1
        return res
    
    def twoSum(self, nums, start, target):
        res = []
        lo, hi = start, len(nums)-1
        while lo < hi:
            left, right = nums[lo], nums[hi]
            curSum=left+right

            if curSum < target:
                while lo<hi and nums[lo] == left:
                    lo +=  1
            elif curSum > target:
                while lo<hi and nums[hi] == right:
                    hi -= 1
            
            else:
                res.append([left, right])
                while lo<hi and nums[lo] == left:
                    lo +=  1
                while lo<hi and nums[hi] == right:
                    hi -= 1
        return res



class Solution:
    def fourSum(self, nums, target):
        return self.nSum(nums, 4, 0, target)

    def nSum(self, nums, n, start, target):
        nums.sort()
        res = []
        length = len(nums)

        # base case
        if n < 2 or length < n:
            return res
        if n == 2:
            return self.twoSum(nums, start, target)

        # n > 2
        for i in range(start, length):
            if i > start and nums[i] == nums[i-1]:
                continue
            tuples = self.nSum(nums, n-1, i+1, target - nums[i])
            for tuple in tuples:
                res.append([nums[i]] + tuple)
        return res


    def twoSum(self, nums, start, target):
        res = []
        lo, hi = start, len(nums)-1
        while lo < hi:
            left, right = nums[lo], nums[hi]
            curSum=left+right

            if curSum < target:
                while lo<hi and nums[lo] == left:
                    lo +=  1
            elif curSum > target:
                while lo<hi and nums[hi] == right:
                    hi -= 1
            
            else:
                res.append([left, right])
                while lo<hi and nums[lo] == left:
                    lo +=  1
                while lo<hi and nums[hi] == right:
                    hi -= 1
        return res


# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

