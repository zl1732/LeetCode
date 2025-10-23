#
# @lc app=leetcode.cn id=1475 lang=python3
# @lcpr version=30203
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    """
    首先找到下一个更小的数,然后做减法
    [8,4,6,2,3]
    [4,2,2,0,0]
            -
    -----------
    [4,2,4,2,3]
    
    注意：相等的也算折扣
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        next_small = self.findNextSmall(prices)
        print(next_small)
        n = len(prices)
        final = [0] * n
        for i in range(n):
            final[i] = prices[i] - next_small[i]
        return final


    def findNextSmall(self, prices):
        n = len(prices)
        st= []
        res = [0] * n
        for i in range(n):
            cur = prices[i]
            while st and cur <= prices[st[-1]]:
                idx = st.pop()
                res[idx] = cur
            st.append(i)
        return res


# @lc code=end



#
# @lcpr case=start
# [8,4,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,1,6]\n
# @lcpr case=end

#

