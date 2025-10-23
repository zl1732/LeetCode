#
# @lc app=leetcode.cn id=402 lang=python3
# @lcpr version=30203
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    """
    🧠 第 1 步：明确目标

        题目要我们「删除 k 个数字，使剩下的数最小」。
        ➡️ 直觉：越左边的数字权重越高，所以应该优先让左边的数字尽量小。

    🧠 第 2 步：想到「局部最优」

        扫描到每个新数 c 时，我希望它左边不要有比它大的数。
        于是自然会想到：

        while st and k>0 and c < st[-1]:
            st.pop(); k -= 1


        意思是「删掉左边更大的数」，保持从左到右单调递增。
        这是典型的单调栈思路。
    
    """

    """
    维护一个递增序列，踢出的个数用k控制
    1 4 3 2 2 1 9
    [1]             k=3
    [1, 4]          k=3
    [1, 3]          k=2  4 out
    [1, 2]          k=1  3 out
    [1, 2, 2]       k=1
    [1, 2, 1]       k=0  2 out
    [1, 1]          k=-1 无法执行这一步

    1 0 2 0 0
    [1]             k = 1
    []              k = 0 注意 0 不入栈

    注意 栈 的顺序 和 原始序列是反着的！！
    
    # 维护递增栈， cur <= st[-1] pop

    """
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        for char in num:
            cur = int(char)
            while st and cur <= st[-1] and k > 0:
                st.pop()
                k -= 1
            """
            这里厉害，不让0开头，但是后面的0要保留，可以通过检测st是否为空判断
            """
            if not st and cur == 0:
                continue
            st.append(cur)

        # k没用完，从后往前删除
        st = st[:-k] if k else st

        # result = ''.join([str(x) for x in st])
        # return result if result else '0'
        return ''.join(map(str, st)) or '0'

         
            
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for c in num:
            # ⚠️ 注意：
            # 如果写成 c <= st[-1]，当相等时也会弹出，可能删掉不该删的数：
            # 比如 "112", k=1 时会变成 "12" 而不是最优的 "11"。
            while st and k > 0 and c < st[-1]:
                st.pop()
                k -= 1
            st.append(c)
        st = st[:-k] if k else st
        # 前面直接全都压入栈，最后统一去除前面的0
        return ''.join(st).lstrip('0') or '0'





"""
关于维护栈的单调性怎么记忆 < >号


🧠 1️⃣ 单调栈的本质

每来一个数，我就看它是否“破坏了”栈的单调性。
如果破坏了，就弹出栈顶，直到恢复单调。

口诀：谁坏我就踢谁。
“坏” = 破坏单调性。
递增栈怕小的，递减栈怕大的。

🔼 单调递增栈-严格
while st and cur <= st[-1]:
    st.pop()
[1 3 7] 5

🔼 单调递增栈-可等 
while st and cur < st[-1]:
    st.pop()
[1 3 5] 5

🔽 单调递减栈 - 严格
while st and cur >= st[-1]:
    st.pop()
[7 5 1] 3

🔽 单调递减栈 - 可等
while st and cur > st[-1]:
    st.pop()
[7 5 3] 3
"""

"""
2️⃣ 可以直接比较 str 吗？

✅ 可以的！

在 Python 里，比较 '2' < '3' 会返回 True，
因为字符 '0'~'9' 的 ASCII 码顺序就是递增的。

'0' < '1' < '2' < '3' < ... < '9'
"""
            
# @lc code=end



#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#

