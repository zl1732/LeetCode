#
# @lc app=leetcode.cn id=1944 lang=python3
# @lcpr version=30203
#
# [1944] 队列中可以看到的人数
#

# @lc code=start
class Solution:
    """
    这个题考察倒序时候stack的pop规律
    就比如 10,6,8,5,11, i=0
    st = [11, 8, 6]
    st.pop * 2 + 11(比10高) = 3
    
    注意如果 10,8,8,5,11 相同高度，只能看到 第一个8 和 11, 不能pop
    所以 cur > st[-1]
    """
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            cur = heights[i]
            cnt = 0
            while st and cur > st[-1]:
                st.pop()
                cnt += 1
            res[i] = cnt if not st else cnt + 1
            st.append(cur)
        return res



# @lc code=end



#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#

