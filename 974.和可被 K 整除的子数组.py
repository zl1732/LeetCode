#
# @lc app=leetcode.cn id=974 lang=python3
# @lcpr version=30203
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
class Solution:
    """
    print(-1%4)   3
    print(-2%4)   2
    
    什么时候要写成 (x % k + k) % k？
    语言差异：Java/C/C++/C#/Go/JS 等里，-1 % 5 == -1（可能为负）。
    如果你用“数组大小为 k”来当计数表，负下标会炸；或者你想把余数规范到 0..k-1，就需要归一化。
    """
    # [4, 9, 9, 7, 4, 5]
    # {4:[0, 1, 2, 4]
    # 2:[3]
    # 0:[-1,5]}
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum = 0
        count = defaultdict(int)
        count[0] = 1
        out = 0
        for num in nums:
            preSum += num
            rem = (preSum%k)
            
            if rem in count:
                out += count[rem]
                count[rem] += 1
            else:
                count[rem] = 1
        return out
        
            


        
        
# @lc code=end



#
# @lcpr case=start
# [4,5,0,-2,-3,1]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n9\n
# @lcpr case=end

#

