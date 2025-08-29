#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30201
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        left = right = 0
        window = {}
        valid = 0

        need = Counter(p)
        required = len(need)
        start = []

        while right < len(s):
            c = s[right]
            right += 1
            # 检测是否在need中
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1

            # print(left, right,window)
            # 删除
            while right - left >= len(p):
                if valid == required:
                    start.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    """
                    注意这里的缩进，不要放在if里
                    """
                    window[d] -= 1
        return start
        
        
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

