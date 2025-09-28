#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30203
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    from collections import defaultdict

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        preSum = 0
        for num in nums:
            preSum += num
            if preSum == k:
                count += 1
                preSum = 0
        return count


    """
    defaultdict(int) → value 默认是整数 0
    defaultdict(list) → value 默认是空列表 []
    """

    """ 
    依然记录下标
    """
    def subarraySum(self, nums, k):
        count = defaultdict(list)
        count[0].append(-1)  # 前缀和=0 出现过下标 -1
        preSum = 0
        out = 0
        for j, num in enumerate(nums):
            preSum += num
            target = preSum - k
            
            if target in count:
                # 如果我们真的枚举下标，而不是 len()
                out += len(count[target])
            """应该放在这里"""
            count[preSum].append(j)
            print(count)
        return out


    def subarraySum(self, nums, k):
        count = defaultdict(list)
        count[0].append(-1)  # 前缀和=0 出现过下标 -1
        preSum = 0
        out = 0
        for i, num in enumerate(nums):
            preSum += num
            if preSum-k in count:
                out += len(count[preSum-k])
            """应该放在后面"""
            count[preSum].append(i)
        return out



    """ 
    记录次数
    """
    def subarraySum1(self, nums: List[int], k: int) -> int:
        count = {0: 1}  # 前缀和为0出现1次（空数组前缀）
        preSum = 0
        out = 0
        for num in nums:
            preSum += num
            if preSum - k in count:
                out += count[preSum - k]
            """注意每次都更新"""
            count[preSum] = count.get(preSum, 0) + 1
        return out



# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

