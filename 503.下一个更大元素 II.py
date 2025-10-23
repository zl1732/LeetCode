#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30203
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    """
    区别是循环数组
    走两遍
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st= []
        res = [-1] * n
        for i in range(2 * n):
            cur = nums[i % n]
            while st and cur > nums[st[-1]%n]:
                idx = st.pop()
                res[idx % n] = cur
            st.append(i)
        return res
    
    """
    可以优化点：
    第二圈时，不再更新栈，
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []
        for i in range(2 * n):  # 走两圈
            cur = nums[i % n]
            # 栈内存原始下标
            while st and nums[st[-1]] < cur:
                res[st.pop()] = cur
            # 第二圈不再入栈（避免重复）
            if i < n:
                st.append(i)
        return res
    """
    第一圈：
        5 4 3 2 1 5 4 3 2 1
        [5 4 3 2 1]          stack
    第二圈 不加：
        5 4 3 2 1 5 4 3 2 1
                    ↑
        [-1 5 5 5 5           res

        5                   stack

    --------------------------------
        5 4 3 2 1 5 4 3 2 1
                    ↑
        [-1 5 5 5 5           res
        5                   stack


    第二圈 加：
        5 4 3 2 1 5 4 3 2 1
                    ↑
        [-1 5 5 5 5           res
        5 5                 stack
    
    --------------------------------
        5 4 3 2 1 5 4 3 2 1
                    ↑
        [-1 5 5 5 5           res
        5 5 4               stack

    """

"""
A. 为什么正序第二圈不入栈？
正序模板（栈里装 待匹配的原始下标）的目的：
    第 1 圈：登记“还没找到更大值”的下标；
    第 2 圈：只负责帮这些下标去“看到”开头那段；不再登记（否则重复登记、徒增空间，甚至重复覆盖答案）。

    例子 A1：全降序
        nums = [5,4,3,2,1]，答案应是 [-1,5,5,5,5]
        第 1 圈结束时，除了 0（值 5）都还没找到更大，栈里会有一堆下标。
        第 2 圈只是让这些下标“看到”开头的 5，从而被逐个弹出并写入 5。
        如果第二圈还入栈，会把 0、1、2…又塞进来，既重复登记，又可能反复覆盖（写对了再被写一次），徒增复杂度。

B. 为什么倒序两圈都要入栈？
    倒序常用的是“值栈”写法（不是下标栈）：
    栈里保存“从右侧看见的候选更大值”（不是待匹配的下标），
    每走一步先把“不可能成为更大值”的元素（≤ 当前值）弹掉，
    此时栈顶就是“右侧第一个更大值”。
    为了保证“右侧视野”完整，你每个 i 都要把当前值压进栈（给“更左边”的人当候选）。这就意味着两圈都要入栈。
    但只在第一圈（i < n）写答案，第二圈只是为了把“右侧候选集合”铺满。
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []
        # 倒序
        for i in range(2 * n - 1, -1, -1):
            cur = nums[i % n]
            while st and cur >= st[-1]:
                st.pop()
            res[i % n] = -1 if not st else st[-1]
            """
            倒序不能这样了，因为存的是候选值，第二遍时候栈空了，会写入很多-1
            Output (0 ms)	 Expected Answer
            [-1,-1,2]	     [2,-1,2]
            [-1,-1,-1,-1,4]	 [2,3,4,-1,4]
            """
            # if i >= n:
            st.append(cur)
        return res

# 倒序值栈的正确写法（并解释“严格大于”
"""
第一遍走完要维护stack从大到小的状态，相当于多个候选目标，如果只取max，想到于只留了一个最大的，后面的全丢了

🔁 类比形象版：「看山模型」
    把 nums 想象成一排山的高度，从右往左看：
    栈里是“你右边所有能看到的山”，按高度递减排。
    新来的山（当前值）会：
    看看右边有没有比自己低的山 → 那些被挡住；
    留下比自己高的山 → 那是你能看到的第一个更大山。
"""
class Solution: 
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        st = []

        for i in range(2 * n - 1, -1, -1):
            cur = nums[i % n]
            while st and st[-1] <= cur:
                st.pop()
            if i < n:  # 只在第一圈写答案
                res[i] = st[-1] if st else -1
            # 两圈都要入栈，保证更左侧的人能看到充足的右侧候选
            st.append(cur)
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

#

