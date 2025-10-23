#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30203
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        s = []
        for cur in path:
            # if cur == '..':
            #     if s:
            #         s.pop()
            #     else:
            #         continue
            # elif cur == '.':
            #     continue
            # elif cur == "":
            #     continue
            # else:
            #     s.append(cur)

            if cur == '..':
                if s:
                    s.pop()
                continue
            elif cur == '.' or cur == "":
                continue
            s.append(cur)
        return '/' + '/'.join(s)

        
# @lc code=end



#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#

