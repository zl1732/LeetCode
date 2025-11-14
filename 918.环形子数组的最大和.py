#
# @lc app=leetcode.cn id=918 lang=python3
# @lcpr version=30203
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    # [5,-3,5 5 -3 5]
    # [5  2 7 ]
    #   [-3 2 7]
    #       5 10 7
    #0 5  2 7 12 9 14]
    """
    窗口最大 n-1
    如果是两个for + presum   on2
    
    则维护 n-1 长度的 window
    记录 min()
    直接用deque 递增栈 pop时检测是否为min
    """
    from collections import deque
    """
    第一遍自己写：
    这个方法有几个问题：
    1. q = deque() 这样会从prefix[0]开始计数，如果nums全负数，则prefix[0] = 0会盖掉正确答案
    2. 即便改成  q = deque([0]) + for i in range( 1,2*n+1 ), 先push了新的值，会盖掉q里的prefix[0] 然后再计算res，也会输出 -3-(-3)依然是错误的0
    
    a. 要不 右端点不计入window，然后跟window里比
        q = deque([0]); for i in range( 1,2*n+1 ) ✅
        先计算答案，然后再push右端点进window  ✅
    
    b. 要不 右端点计入window 本题不能这样做！
        q = deque(); for i in range(2*n)  ❌
        总会自己减自己得到0

    注意顺序，必须隔离右端点和window，所以要先计算答案，然后再push

    """
    # 错误写法
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(2*n):
            prefix.append(prefix[-1] + nums[i%n])

        res = float('-inf')
        left = 0
        q = deque()

        for i in range( 2*n ):
            cur = prefix[i]
            # push
            while q and cur < prefix[q[-1]]:
                q.pop()
            q.append(i)

            # update res
            res = max(res, cur - prefix[q[0]])
            # pop
            if i - left == n-1:
                if prefix[left] == prefix[q[0]]:
                    q.popleft()
                left += 1
        return -1 if res==float('-inf') else res 
    

    # 正确写法
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(2*n):
            prefix.append(prefix[-1] + nums[i%n])

        res = float('-inf')
        left = 0
        q = deque([0])

        for i in range(1, 2*n+1):
            cur = prefix[i]
            # update res
            res = max(res, cur - prefix[q[0]])

            # push
            while q and cur < prefix[q[-1]]:
                q.pop()
            q.append(i)

            # pop
            if i - 1 - left == n - 1:
                if prefix[left] == prefix[q[0]]:
                    q.popleft()
                left += 1
        return -1 if res==float('-inf') else res 


    # 正确写法
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(2*n):
            prefix.append(prefix[-1] + nums[i%n])

        res = float('-inf')
        left = 0
        q = deque([0])

        for i in range(1, 2*n+1):
            # pop
            while q and q[0] < i - n:
                q.popleft()

            cur = prefix[i]
            # update res
            res = max(res, cur - prefix[q[0]])

            # push
            while q and cur < prefix[q[-1]]:
                q.pop()
            q.append(i)

        return -1 if res==float('-inf') else res 


# @lc code=end



#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,-2,2,-3]\n
# @lcpr case=end

#

