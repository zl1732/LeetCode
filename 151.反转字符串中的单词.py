#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30203
#
# [151] 反转字符串中的单词
#
# https://leetcode.cn/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (59.07%)
# Likes:    1342
# Dislikes: 0
# Total Accepted:    800.3K
# Total Submissions: 1.4M
# Testcase Example:  '"the sky is blue"'
#
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
# 
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
# 
# 
# 示例 2：
# 
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：反转后的字符串中不能存在前导空格和尾随空格。
# 
# 
# 示例 3：
# 
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 包含英文大小写字母、数字和空格 ' '
# s 中 至少存在一个 单词
# 
# 
# 
# 
# 
# 
# 
# 进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
# 
#

# @lc code=start
class Solution:    
    """
    思路是双指针，
    i：先找到词的末尾，然后赋值给j， 然后继续找到初始位置
    j: 始终记录末尾
    """
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0: break
            j = i
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i+1:j+1])
        return " ".join(res)

            
    """
    如果用if, 必须有else break，
    """
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            # 跳过空格
            while i >= 0:
                if s[i] == " ":
                    i -= 1
                else:
                    break
            if i < 0: break

            # 找单词
            j = i
            while i>= 0:
                if s[i] != " ":
                    i -= 1
                else:
                    break

            res.append(s[i+1: j+1])
            # i = j  # 更新 i，继续往前走

        return " ".join(res)


class Solution:    
    """
    另一种思路：
    1. 先整体翻转
    2. 然后逐个单词翻转
    """
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        # 1. 去除多余空格（双指针）
        def remove_spaces(chars):
            n = len(chars)
            i = 0
            j = 0
            while j < n:
                # 跳过前导空格
                while j < n and chars[j] == ' ':
                    j += 1
                # 拷贝单词
                while j < n and chars[j] != ' ':
                    chars[i] = chars[j]
                    i += 1
                    j += 1
                # 跳过单词后的空格，并插入一个空格
                while j < n and chars[j] == ' ':
                    j += 1
                if j < n:   # 不是最后一个单词
                    chars[i] = ' '
                    i += 1
            return chars[:i]

        # 2. 翻转函数
        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        chars = remove_spaces(chars)

        # 3. 整体翻转
        reverse(0, len(chars) - 1)

        # 4. 翻转每个单词
        n = len(chars)
        start = 0
        for end in range(n+1):
            if end == n or chars[end] == ' ':
                reverse(start, end - 1)
                start = end + 1

        return "".join(chars)



class Solution:
    def reverseWords(self, s: str) -> str:
        sb = []
        for c in s:
            if c!= ' ':
                sb.append(c)
            # is ‘ ’
            else:
                if not sb:
                    continue
                elif sb[-1] != ' ':
                    sb.append(' ')
        if not sb:
            return ''
        if sb[-1] == ' ':
            sb.pop()
        

        chars = list(''.join(sb))
        n = len(chars)
        self.reverse(chars, 0, n - 1)
        
        # 再把每个单词翻转
        start = 0
        for end in range(n+1):
            if end == n or chars[end] == ' ':
                self.reverse(chars, start, end-1)
                start = end + 1

        return ''.join(chars)


    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

