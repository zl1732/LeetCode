#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30203
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        window {} 记录次数
        记录window的value总数- maxvalue
        小数字 > k ; 
        """
        window = {}
        left = right = 0
        res = 0
        while right < len(s):
            char = s[right]
            right += 1
            window[char] = window.get(char, 0) + 1
            
            while left < right and right - left - max(window.values()) > k:
                char = s[left]
                left += 1
                window[char] -= 1
            
            res = max(res, right - left)
        return res
    

    """
    1. 时间复杂度上的提升
    max(window.values()) 版本
        每次右移指针，都要对整个字典求一次最大值。
        字符集是 26 个大写字母 → 每次 O(26)，总体 O(26n)，常数还好，但形式上显得不够精炼。
    count + max_count 版本
        每次右移时，只更新当前字符的计数，然后更新一次 max_count。
        始终 O(1)，总体 O(n)。
    """
    
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        left = right = 0
        max_count = 0
        res = 0

        while right < n:
            char = s[right]
            right += 1
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_count = max(max_count, count.get(char, 0))
            
            while (right - left) - max_count > k:
                char = s[left]
                left += 1
                count[char] -= 1

            res = max(res, right - left)

        return res


    """
    数组写法：count = [0]*26 → 下标直接是 ord(ch) - ord('A')，
    时间复杂度严格 O(1)，空间固定 26。

    字典写法：count[char] 要做哈希查找，
    虽然 Python dict 很快，平均 O(1)，但常数比数组大一些。
    """
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 26
        left = right = 0
        max_count = 0
        res = 0

        while right < n:
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            right += 1

            while (right - left) - max_count > k:
                idx_left = ord(s[left]) - ord('A')
                count[idx_left] -= 1
                left += 1

            res = max(res, right - left)

        return res


# @lc code=end



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

