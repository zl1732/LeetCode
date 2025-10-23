#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30203
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    """
    核心：
    计算完之后的数字重新加回去stack里
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in "+-*/":
                a = stk.pop()  # 第二个操作数
                b = stk.pop()  # 第一个操作数
                # 注意：减法和除法的顺序必须是 b - a、b / a
                if token == "+":
                    stk.append(a + b)
                elif token == "*":
                    stk.append(a * b)
                elif token == "-":
                    stk.append(b - a)
                elif token == "/":
                    stk.append(int(b / a))  # Python的除法结果可能是float，要取整
            else:
                stk.append(int(token))
        return stk.pop()


# @lc code=end



#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

