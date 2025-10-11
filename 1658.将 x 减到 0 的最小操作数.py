#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30203
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    """
    11 12 9993 0
    12 13 9904 0
    13 14 8819 0
    14 15 1231 0
    15 16 6309 0

    下面这个方法的问题在于：
    最后一轮 走到 15 16，left += 1执行完，
    while left < right不会再执行了，但是其实16 16这一轮才是解
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        # 用 window 记sum
        window = 0
        target = sum(nums) - x
        max_len = -1
        left = right = 0 
        
        while right < len(nums):
            num = nums[right]
            right += 1
            window += num
            while left < right and window >= target:
                if window == target:
                    max_len = max(max_len,right - left)

                # 左移动
                num = nums[left]
                window -= num
                left += 1
        return -1 if max_len == -1 else len(nums) - max_len

            
    def minOperations(self, nums: List[int], x: int) -> int:
        # 用 window 记sum
        window = 0
        target = sum(nums) - x
        max_len = float('-inf')
        left = right = 0 
        
        while right < len(nums):
            num = nums[right]
            right += 1
            window += num
            while left < right and window > target:
                # 左移动
                num = nums[left]
                window -= num
                left += 1

            if window == target:
                max_len = max(max_len,right - left)
                """
                这样会漏掉很多情况：
                如果 window == target 出现在「刚好加上 nums[right] 后」，但是窗口没触发收缩（window <= target），你根本没检查。

                比如 testcase [1,1,4,2,3], x=5：
                target = 6

                当窗口 [1,1,4] 时，window = 6，正好命中，但没进收缩循环 → 漏掉。
                """
                # if window == target:
                #     max_len = max(max_len,right - left)

        return -1 if max_len == float('-inf') else len(nums) - max_len

# 对比76题，那个是最小，这个是最大
"""
滑动窗口收缩条件总结
=================

📌 LeetCode 1658 (最小操作数 / 转换为最大子数组问题)
------------------------------------------------
- 本质：要找一个 **最长子数组和 = target**
- 窗口随着 right 增大，window 单调增加
- 只有在 window > target 时，才需要收缩
- 因为一旦超了，就必须缩小才能回到 target
- 模板：
    while window > target:
        shrink()
    if window == target:
        update_ans()

📌 LeetCode 76 (最小覆盖子串)
------------------------------------------------
- 本质：要找一个 **最短子串，覆盖所有目标字符**
- 只要窗口满足条件 (valid == required)，就尝试收缩
- 因为满足后，不收缩就可能不是最短
- 模板：
    while valid == required:
        update_ans()
        shrink()

🔑 核心对比
------------------------------------------------
- 最大化问题 → 收缩条件是「超了」(window > target)
- 最小化问题 → 收缩条件是「够了」(valid == required / >=)
- 口诀：最长看超，最短看够
"""



# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

