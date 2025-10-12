#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30203
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        可以先搜索一遍找到最远下车点
        """
        # diff = [0] * 10000
        max_pos = max(end for _, _, end in trips)  # 找到最远的下车点
        diff = [0] * (max_pos + 1)

        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        
        cur = 0
        for i in range(1, 10000):
            cur += diff[i-1]
            if cur > capacity:
                return False
        return True



    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_pos = max(end for _, _, end in trips)  # 找到最远的下车点
        diff = [0] * (max_pos + 1)

        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num

        cur = 0
        for i in range(max_pos + 1):
            cur += diff[i]
            if cur > capacity:
                return False
        return True


# @lc code=end



#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#

