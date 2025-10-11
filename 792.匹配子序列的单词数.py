#
# @lc app=leetcode.cn id=792 lang=python3
# @lcpr version=30203
#
# [792] 匹配子序列的单词数
#

# @lc code=start
class Solution:
    """
    依然要一个一个词扫过去
    提升：
        搜索下一个词时用二分搜索
        abcabcb
        (a:[0, 3], b:[1, 4, 6], c[2, 5])
        bb,匹配第二个b，搜索[1,4,6],找到index>1的第一个,4
    """
    from collections import defaultdict
    # def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #     # 建立查询矩阵
    #     lookup = defaultdict(list)
    #     for i, char in enumerate(s):
    #         lookup[char].append(i)
        
    #     # loop 
    #     res = 0
    #     for word in words:
    #         # bbb abcabcb 
    #         i = j = 0
    #         while i < len(word) and j < len(s):
    #             search_ch = word[i]
    #             nums = lookup[search_ch]  #[-1, 1 4 6]
    #             target = j
                
    #             # 二分查找
    #             left, right = 0, len(nums)-1
    #             while left <= right:
    #                 mid = left + (right - left)//2
    #                 if nums[mid] == target:
    #                     right = mid - 1
    #                 elif nums[mid] < target:
    #                     left = mid + 1
    #                 elif nums[mid] > target:
    #                     right = mid - 1
    #             if left == len(nums):
    #                 break
    #             # 找到了当前位,bbb下一位，abcabcb移动到找到的位置left的index
    #             i += 1
    #             """ 第一次我写的就差这个+1"""
    #             j = nums[left] + 1 

                
    #         if i == len(word):
    #             res += 1
    #     return res


    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        # 建立查询矩阵
        lookup = defaultdict(list)
        for i, char in enumerate(s):
            lookup[char].append(i)
        
        # loop 
        res = 0
        for word in words:
            # bbb abcabcb 
            i = j = 0
            while i < len(word) and j < len(s):
                c = word[i]
                if c not in lookup:
                    break
                nums = lookup[c]  #[-1, 1 4 6]
                
                # 二分查找
                pos = self.left_bound(nums, j)
                if pos == len(nums):
                    break
                j = nums[pos]
                # 找到了当前位,bbb下一位，abcabcb移动到找到的位置left的index
                i += 1
                j += 1
                
            if i == len(word):
                res += 1
        return res

    # 查找左侧边界的二分查找
    def left_bound(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid
        return left



from bisect import bisect_right
"""
✅ 核心语义
    bisect_right(a, x) 返回第一个大于 x 的元素位置。

换句话说：
    如果 x 已经在列表中，它会返回 x 的右边界（即最后一个等于 x 的位置 + 1）；
    如果 x 不在列表中，它会返回 x 应该插入的位置，使得 a 仍然有序。
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        for i, ch in enumerate(s):
            lookup[ch].append(i)

        res = 0
        for word in words:
            j = -1  # 上一个匹配位置
            matched = True
            for ch in word:
                if ch not in lookup:
                    matched = False
                    break
                # 在 lookup[ch] 中找第一个 > j 的位置
                nums = lookup[ch]
                pos = bisect_right(nums, j)
                if pos == len(nums):
                    matched = False
                    break
                j = nums[pos]  # 更新为新位置
            if matched:
                res += 1
        return res

# @lc code=end



#
# @lcpr case=start
# "abcde"\n["a","bb","acd","ace"]\n
# @lcpr case=end

# @lcpr case=start
# "dsahjpjauf"\n["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]\n
# @lcpr case=end

#

