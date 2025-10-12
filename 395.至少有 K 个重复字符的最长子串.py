#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30203
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
class Solution:
    """
    本题的场景中，我们想尽可能多地装字符，即扩大窗口，但不知道什么时候应该开始收缩窗口。
    为什么呢？比如窗口中有些字符出现次数不满足 k，但有可能再扩大扩大窗口就能满足 k 了呀？但要这么说的话，你干脆一直扩大窗口算了，所以你说不准啥时候应该收缩窗口。
    理论上讲，这种情况就不能用滑动窗口模板了，但有时候我们可以自己添加一些约束，来进行窗口的收缩。

    题目说让我们求每个字符都出现至少 k 次的子串，我们可以再添加一个约束条件：求每个字符都出现至少 k 次，仅包含 count 种不同字符的最长子串。

    1、什么时候应该扩大窗口？窗口中字符种类小于 count 时扩大窗口。
    2、什么时候应该缩小窗口？窗口中字符种类大于 count 时扩大窗口。
    3、什么时候得到一个合法的答案？窗口中所有字符出现的次数都大于等于 k 时，得到一个合法的子串。
    ababbcdd 
    """
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, 27):
            cur = self.longestSubstringHelper(s, k, i)
            res = max(res, cur)
        return res

    """
    不能模仿最小子串，因为问的是最大串
    所以需要用unique_char_num, count_at_least_k两个记录
    1. unique_char_num 大于 count时候开始收缩
    2. 收缩后 检查 count_at_least_k == unique_char_num 
    3. 满足的记录
    """
    # def longestSubstringHelper(self, s, k, count):
    #     left = 0
    #     window = {}
    #     valid = 0
    #     res = 0
    #     for right, char in enumerate(s):
    #         window[char] = window.get(char,0) + 1
    #         if window[char] == k:
    #             valid += 1
    #         #
    #         while left < right and valid == count:
    #             res = max(res, right-left)
    #             char = s[left]

    #             window[char] -= 1
    #             if window[char] == 0:
    #                 valid -= 1
    #             left += 1
    #     return res


    def longestSubstringHelper(self, s, k, unique_target):
        left = right = 0
        # 记录出现的
        window = {}
        cur_unique = 0
        valid = 0
        max_len = 0
        while right < len(s):
            char = s[right]
            if char not in window:
                cur_unique += 1
                window[char] = 1
            else:
                window[char] += 1
            # 判断valid
            if window[char] == k:
                valid += 1
            right += 1

            while left < right and cur_unique > unique_target:
                # shrink
                char = s[left]
                """
                这个区别于76题的是，76外层严格控制valid = k，valid-1之后即退出
                本题：可能多次执行 window[char] < k 导致valid减多次数
                解决
                1. 先判断 == k  然后再window[char] -= 1  ✅ 这个更好
                2. 先window[char] -= 1， 然后判断 == k-1
                
                推荐顺序是：
                    先判断是否正好等于 k；
                    再执行 window[char] -= 1。
                """
                # window[char] -= 1
                # if window[char] < k:
                #     valid -=1
                if window[char] == k:
                    valid -= 1
                window[char] -= 1
                if window[char] == 0:
                    cur_unique -= 1
                    del window[char]
                # update left
                left += 1
                
            # 判断是否满足
            if valid == unique_target:
                max_len = max(max_len, right- left)
        return max_len
                    







        
# @lc code=end



#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

