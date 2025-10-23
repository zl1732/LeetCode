#
# @lc app=leetcode.cn id=388 lang=python3
# @lcpr version=30203
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        st = []
        max_len = 0
        # line
        paths = input.split('\n')
        for path in paths:
            level = path.rfind('\t') + 1
            # print(level, path)
            while st and level < len(st):
                st.pop()
            """
            append 要减去 level，否则后面多个path会多次加level
            """
            st.append(len(path)-level)
            # 如果是文件，就计算路径长度
            if "." in path:
                l = sum(st) + len(st) - 1
                # 加上父路径的分隔符
                max_len = max(max_len, l)
                # print(max_len)
        return max_len
        
# @lc code=end



#
# @lcpr case=start
# "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"\n
# @lcpr case=end

# @lcpr case=start
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

# @lcpr case=start
# "file1.txt\nfile2.txt\nlongfile.txt"\n
# @lcpr case=end

#

