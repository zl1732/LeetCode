#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30203
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    """
    找右边更大值 idx-cur 的长度
    思路：
    1. pop一次就+1
    2. 正序idx记录？
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 正序
        n = len(temperatures)
        res = [0] * n
        st = []
        for i, cur in enumerate(temperatures):
            while st and cur > temperatures[st[-1]]:
                idx = st.pop()
                diff = i - idx
                res[idx] = diff
            st.append(i)
        return res
    
    """
    注意下这种反序写法，res[i] = 0 if not st else st[-1] - i
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 反序
        n = len(temperatures)
        res = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            cur = temperatures[i]
            while st and cur >= temperatures[st[-1]]:
                st.pop()
            res[i] = 0 if not st else st[-1] - i
            st.append(i)
        return res


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 反序
        n = len(temperatures)
        res = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            cur = temperatures[i]
            while st and cur >= st[-1]:
                st.pop()
            # 这是计算右侧有几个当前值高的点
            res[i] = 0 if not st else len(st)
            st.append(cur)
        return res



# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

