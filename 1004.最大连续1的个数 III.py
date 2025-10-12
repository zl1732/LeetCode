#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30203
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        window = 0
        res = float("-inf")
        while right < len(nums):
            num = nums[right]
            if num == 0:
                window += 1
            right += 1
            """
            错误1，必须要求window到达k，即达到k个0
                a. 可能存在没有0，永远达不到k
                b. 实际算少了
                    [0,0,1,1,0,0,1,1,1] k=3
                    [0,0,1,1,0  这时就会进入内层while，计算长度为5
                    [_,0,1,1,0,0,1,1,1] 其实这才是正确答案

                根因总结
                    你只在 window == k 时更新 → 漏掉了 window < k 时的更长窗口。
                    收缩条件写成 == → 本质上，你的算法算的是 “恰好翻转 k 个 0 的子数组”，而不是 “最多 k 个 0”。

            错误2：更新res位置不对，不应该在内层while里面
                a. 上述例子 [0,0,1,1,0  这时候不应该固定right开始缩
                所以其实应该找到 window > k,之后再缩，缩到k，计算res，更新
            
                根因总结
                    每次 while window > k 把窗口缩到合法后，此时 [left, right) 一定合法，可以直接更新 res。

            """
            while left < right and window == k:
                res = max(right - left, res)
                num = nums[left]
                if num == 0:
                    window -=1
                left += 1
        return res

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        window = 0
        res = float("-inf")
        while right < len(nums):
            num = nums[right]
            if num == 0:
                window += 1
            right += 1
            
            while window > k:
                if nums[left] == 0:
                    window -= 1
                left += 1

            res = max(res, right - left)
        return res if res != float('-inf') else 0

        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

