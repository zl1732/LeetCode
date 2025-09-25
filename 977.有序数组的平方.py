#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30203
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    #[-3,-2,1,2,3]
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        我的思路：从中间两位开始往外扩散，因为我觉得中间一定最小，但是
        [-5,-3,-2,-1] 过不了

        思路：
            🔥从两边开始，谁绝对值大就平方放到结果数组的最后面🔥。
            因为最大的平方数一定在两端产生。
        """
        n = len(nums)
        res= []

        l = (n-1)//2
        r = l+1

        while l >= 0 and r < n:
            left = nums[l]
            right = nums[r]
            
            if abs(left) < abs(right):
                res.append(left**2)
                l -= 1
            else:
                res.append(right**2)
                r += 1
            print(l, r, left, right)
        
        for i in range(l, -1, -1):
            res.append(nums[i]**2)
        for i in range(r, n):
            res.append(nums[i]**2)
        return res
            

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        我的思路修改：找到0的位置，找到第一个 >=0 的下标
        """
        n = len(nums)
        res= []

        # l = (n-1)//2
        # r = l+1
        # 
        r = 0
        while r < n and nums[r] < 0:
            r += 1
        l = r - 1 
            
        while l >= 0 and r < n:
            left = nums[l]
            right = nums[r]
            
            if abs(left) < abs(right):
                res.append(left**2)
                l -= 1
            else:
                res.append(right**2)
                r += 1
            print(l, r, left, right)
        
        # for i in range(l, -1, -1):
        #     res.append(nums[i]**2)
        """ 这样写比较直观，不过都可以"""
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1
        for i in range(r, n):
            res.append(nums[i]**2)
        return res


    """
    最推荐方法：对撞指针
    这个题有点像 88 题
    太聪明了这个解法
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        # 从后往前填入res的指针（）
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return res



            
        
# @lc code=end



#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

