#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30203
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}":"{",
                ")":"(",
                "]":"["}
        st = []
        for char in s:
            if char in '}])':
                if st and st[-1] == pair[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)

        if not st:
            return True
        
        return False
                    
                

        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

