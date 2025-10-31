#
# @lc app=leetcode.cn id=581 lang=python3
# @lcpr version=30203
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    """
    思路1. 先对原数组排序，然后对比左右第一次出现不同的地方
    [2,6,4,8,10,9,15]
    [2,4,6,8,9,10,15]
       ↑        ↑
       
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 排序法
        left = 0
        sorted_nums = sorted(nums)
        for i, num in enumerate(nums):
            if num != sorted_nums[i]:
                left = i
                break
        
        right = -1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num != sorted_nums[i]:
                right = i
                break
        
        return right - left +1


    #
    """
    思路2. 单调栈、扫描
    → → → → → 
    [2,12,4,8,10,3,15]
       max       last_violet

    [2, 4, 8,10,] max=12 cur=3
    所以12 最终的位置应该在 3的位置
    
    思路：
        数组中有一段“局部混乱”，
        那段的最小值应该往前挪、最大值应该往后挪

    如果一个数组已经排好序，它一定满足：
        扫描方向	条件
        左→右	   当前元素 ≥ 前面最大值
        右→左	   当前元素 ≤ 后面最小值

    状态维护：
        从左维护 max，从右维护 min；

    局部检测：
        当当前值 < max_so_far 或 > min_so_far 时，说明违序；

    边界更新：
        记录最远违序的位置 → [left, right]；
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 扫描线
        n = len(nums)
        """ 注意下面这俩不要写反了 """
        max_, min_ = float('-inf'), float('inf')
        left, right = 0, -1
        # right
        for i in range(n):
            cur = nums[i]
            if cur < max_:
                right = i
            else:
                max_ = cur
        # left
        for i in range(n-1, -1, -1):
            cur = nums[i]
            if cur > min_:
                left = i
            else:
                min_ = cur
        print(left, right)
        return right - left + 1
                

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 单调栈
        # 肯定不能用正序法的思路
        # [2,6,4,8,10,9,15]
        #  → 递增栈  ← 递减栈
        #    → cur < st[-1] 记录 cur index right
        #    ← cur > st[-1] 记录 cur index left

        """
        ❌ 
        [1,3,2,2,2]
        Answer	Expected Answer
        2	4

        为什么错的：
            while st and cur < st[-1]:
            当遇到相等值 2 == 2 时，不会 pop。但真正的“无序”是从 3 开始，到最后一个 2 结束。
            但 没有再触发 cur < st[-1]，右边界没有继续向右推进。

        🚫 为什么不能简单改成 <=？
            那 [1,1,1,1] 会被误判为无序。
            等值本身在有序数组中是允许存在的。 <= 就会误把平的地方当下降。
        
        ✅ 扫描线为什么能处理这个？
            因为扫描线维护的不是局部比较，而是全局单调性。

            max_so_far 一直更新成看到的最大值；
            不管是第一个 2、第二个 2、还是第三个 2，都会触发更新。
            例：
            nums = [1,3,2,2,2]
            max_so_far: 1,3,3,3,3
            cur<max?  F,T,T,T
            → right = 4 ✅
        
        所以总的来说，这是一种错误的写法，本质是扫描线，但错误，没有用到栈的关键信息



        """
        n = len(nums)
        max_, min_ = float('-inf'), float('inf')
        left, right = 0, -1
        # →
        st = []
        for i in range(n):
            cur = nums[i]
            while st and cur <= st[-1]:
                st.pop()
                right = i
            st.append(cur)

        st = []
        for i in range(n-1, -1, -1):
            cur = nums[i]
            while st and cur > st[-1]:
                st.pop()
                left = i
            st.append(cur)
        
        return right - left + 1


"""
正确使用单调栈的写法如下:
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1
        """
        🔥 这里可以等价于 找右侧更小值 + 正序 + 最后替换的最左侧
        """
        st = []
        for i in range(n):
            while st and nums[i] < nums[st[-1]]:
                idx = st.pop()  # 正序pop
                left = min(left, idx) # 记录pop的最小的index
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[i] > nums[st[-1]]:
                idx = st.pop()
                right = max(right, idx)
            st.append(i)
            
        print(left, right)
        return right - left + 1 if left != n else 0
        

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1

        """
        🔥 同理，试试反序 找右侧更小值，找到更小值==st非空，记录cur的i
        注意倒序 是>=
        """
        st = []
        for i in range(n-1,-1, -1):
            while st and nums[i] <= nums[st[-1]]:
                # 被弹出的索引说明打破了递增性，左边界可能更左
                st.pop()
            if st:
                left = min(left, i)
            st.append(i)

        st = []
        for i in range(n):
            while st and nums[i] >= nums[st[-1]]:
                st.pop()
            if st:
                right = max(right, i)
            st.append(i)
            
        print(left, right)
        return right - left + 1 if left != n else 0
        

# @lc code=end

    

#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

