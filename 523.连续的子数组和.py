#
# @lc app=leetcode.cn id=523 lang=python3
# @lcpr version=30203
#
# [523] 连续的子数组和
#

# @lc code=start
class Solution:
<<<<<<< HEAD
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
=======
    """
    1. 构建preSum
    2. for i for j, presum[i]-presum[j] 这必定是on2
        如果想变成on, 必然增加数据结构，哈希表
    3. 利用 % 当成身份标签
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """这里很大问题，不能加1，因为要看长度。比如[0]会变成[0,0]，i=1"""
        n = len(nums)+1
        """ preSum不需要list"""
        preSum = [0] * n
        count = {-1:0}
        for i in range(n):
            preSum[i] = preSum[i-1] + nums[i-1]
            """ k = 0 怎么办"""
            if preSum[i]%k in count and i-preSum[i-k] > 2:
                return True
            count[preSum[i]%k] = i
        return False
    
    
    """
    总结：
    本题目的是“找一对下标即可”。有了一个合法的 i 就够了。
    560题：个数统计
    
    """
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = 0
        rem_to_index = {0:-1}
        for i, num in enumerate(nums):
            preSum += num
            rem = preSum%k
            if rem in rem_to_index:
                if i - rem_to_index[rem] > 1:
                    return True
            else:
                rem_to_index[rem] = i
        return False
        

>>>>>>> b0d0ed76e32d11849717c8194682fdfeeb87ce5a
        
# @lc code=end



#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

