#
# @lc app=leetcode.cn id=853 lang=python3
# @lcpr version=30203
#
# [853] 车队
#

# @lc code=start
class Solution:
    """
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    追击问题，一旦前面有人压速度，后面就会积压
    起点                    终点
    - - - -  - - - -  - - - -
                        2           1秒
                   4                1秒
    1                               12秒
             1                      7秒
        3                           3秒

    按起点到终点排序为止，记录需要的时间
    [12 3    7     1   1]
     -- ------     -----
     a    b          c
    
    问题可以转化为，寻找右侧更大值
    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0])

        times = [(target-x[0])/x[1] for x in cars]
        
        """
        使用单调栈可以记录 cluster 的数量，也就是从高到低每个小山峰的高度 12 7 1
        为什么：
            12 最慢的，赶不上前面
            7  稍快，跟12拉开距离，但是赶不上1
            1  最快
        非常巧妙的可以用单调栈统计 小车队 的数量
        使用严格单调减
        """
        n = len(times)
        st = []
        for time in times:
            # 单调减栈，cur > st[-1] 不对了
            while st and time >= st[-1]:
                st.pop()
            st.append(time)
        return len(st)



    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0])

        times = [(target-x[0])/x[1] for x in cars]
        
        """
        也可以直接倒序遍历就行！！！
        """
        res = 0
        max_time = 0
        n = len(times)
        for i in range(n - 1, -1, -1):
            if times[i] > max_time:
                max_time = times[i]
                res += 1
        return res


# @lc code=end



#
# @lcpr case=start
# 12\n[10,8,0,5,3]\n[2,4,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 100\n[0,2,4]\n[4,2,1]\n
# @lcpr case=end

#

