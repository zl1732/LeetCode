#
# @lc app=leetcode.cn id=386 lang=python3
# @lcpr version=30201
#
# [386] 字典序排数
#

# @lc code=start

"""
         ""
       / | | | | | | | | \
      1  2 3 4 5 6 7 8 9   ← 第一层（根节点 1~9）

     /|\  
   10 11 12 13             ← 1 的子节点（1×10 + 0~9）

"""

class Solution:
    def __init__(self):
        """
        放在 __init__ 中，避免了每次都在主函数中重复赋值。
        Your runtime beats 23.88 % of python3 submissions
        -> Your runtime beats 37.8 % of python3 submissions
        """
        self.res = []

    def lexicalOrder(self, n: int) -> List[int]:
        def traverse(num):
            if num > n:
                return
            self.res.append(num)

            for i in range(10):
                """
                剪枝加速：Your runtime beats 8.69 % of python3 submissions
                -> Your runtime beats 23.88 % of python3 submissions
                """
                if num * 10 + i > n:
                    break
                traverse(num * 10 + i)

        for i in range(1,10):
            traverse(i)
        return self.res


"""
Your runtime beats 37.8 % of python3 submissions
Your memory usage beats 75.29 % of python3
"""
class Solution1:

    def __init__(self):
        self.res = []

    def lexicalOrder(self, n: int) -> List[int]:
        # 总共有 9 棵多叉树，从 1 开始
        for i in range(1, 10):
            self.traverse(i, n)
        return self.res

    # 多叉树遍历框架，前序位置收集所有小于 n 的节点
    def traverse(self, root: int, n: int) -> None:
        if root > n:
            return
        self.res.append(root)
        for child in range(root * 10, root * 10 + 10):
            if child > n:
                break
            self.traverse(child, n)

# @lc code=end



#
# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#