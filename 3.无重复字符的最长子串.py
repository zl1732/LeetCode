#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30201
#
# [3] 无重复字符的最长子串
#

# @lc code=start

"""
这个题启发：更新答案的时机，567和76都是在内侧while里，
          且是💡左指针移动之前💡，更新答案！！

要的是最长无重复子串，哪一个阶段可以保证窗口中的字符串是没有重复的呢？
这里和之前不一样，要在收缩窗口完成后更新 res
因为窗口收缩的 while 条件是存在重复元素，换句话说收缩完成后一定保证窗口中没有重复。
"""
class Solution:
    """
    我的思路：
        右指针条件：没出现重复
        左指针移动：出现重复，判定有重复，先移动，然后记录当前子串长度
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Wrong Answer
        879/987 cases passed (N/A)
        Testcase
        " "
        Answer
        0
        Expected Answer
        1
        分析：只有再window[c]>1时才计算max_len
        如果只有一个字符，到不了这里
        """
        left = right = 0
        window = {}
        max_len = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c,0)+1
            
            while left < right and window[c]>1:
                d = s[left]
                c
                """
                这里我的思路其实是对的，
                选择在left+=1之后更新；如果在left+=1之前
                就需要max_len = right-left-1，这个我当时想到了
                但是，应该挪到while外面去做😄
                """
                if right-left > max_len: #
                    max_len = right-left #
                window[d] -= 1
            # 每次都更细
            #max_len = max(max_len, right - left)
        return max_len
    

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        window = {}
        max_len = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1

            # 无论如何都尝试更新 max_len
            max_len = max(max_len, right - left)

        return max_len

    
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

