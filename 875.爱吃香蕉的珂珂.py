#
# @lc app=leetcode.cn id=875 lang=python3
# @lcpr version=30203
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    """
    f(x) = target, 「满足 f(x) == target 的 x 的最小值是多少」？
    x: 每小时吃香蕉的数量，取值1~max(piles)
    f(x): 吃香蕉的小时数
    target： h 即警卫离开时间

    for pile in piles:
        fx += ceil(pile // x)
    
    x 增加， fx 减少
    搜索 x = [1, max(piles)]
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left, right = 1, max_pile
        while left < right:
            mid = left+(right-left)//2
            fx = self.calc_fx(piles, mid)
            if fx > h:
                left = mid+1
            elif fx == h:
                right = mid
            elif fx < h:
                right = mid
        if left > max_pile:
            return -1
        return left

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left, right = 1, max_pile
        while left <= right:
            mid = left+(right-left)//2
            fx = self.calc_fx(piles, mid)
            if fx > h:
                left = mid+1
            elif fx == h:
                right = mid-1
            elif fx < h:
                right = mid-1
        if left > max_pile:
            return -1
        return left


    def calc_fx(self, piles, x):
        fx = 0
        for pile in piles:
            cur = pile//x
            if pile%x > 0:
                cur += 1
            fx += cur
        return fx


def time_needed(piles, k):
    # 轻量写法： (pile + k - 1) // k == ceil(pile / k)
    hours = 0
    for pile in piles:
        hours += (pile + k - 1) // k
    return hours

# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

