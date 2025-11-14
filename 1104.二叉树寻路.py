#
# @lc app=leetcode.cn id=1104 lang=python3
# @lcpr version=30201
#
# [1104] 二叉树寻路
#

# @lc code=start

import math
from typing import List

class Solution:
    """
    思路：
        根据二叉堆实现原理，索引：
        parent(label) = label//2
        13-6 3 1

        zigzag之后，13的父本来是6，也就是第三排，4 5 6 7 的第三个
        现在反转之后，变成 7 6 5 4，则新的父为 7-(6-4) = 5

    计算层数：
        某个 label 如果在第 k 层，就一定满足：
        2^k ≤ label ≤ 2^(k+1) - 1

        对这三个量取 log₂：k ≤ log₂(label) < k+1
        k = floor(log₂(label))
    
    start,end:
        k 从0开始
        2^k，2^k*2-1
    """


    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label > 0:
            path.append(label)
            # 先计算上层normal 位置，然后在转换成zigzag位置
            label //= 2
            if label==0:
                break
            # 计算层数
            level = int(math.log2(label))
            start, end = 2**level, 2**level*2 -1
            label = end-label + start
        path.reverse()
        return path


    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            # 先将本层反序，然后计算上层normal位置，也就相当于zigzag了
            level = label.bit_length() - 1
            start = 1 << level
            """
            end = 1 << (level + 1) - 1 ❎
            """
            end = (1 << (level + 1)) - 1
            
            rev_label = start + end - label
            label = rev_label//2
        path.reverse()
        return path


# @lc code=end







class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            level = label.bit_length() - 1      # 等价于 floor(log2(label))
            start = 1 << level                  # 本层起点
            end = (1 << (level + 1)) - 1        # 本层终点
            # 映射 + 找父节点
            print(start, end, label)
            label = (start + end - label) // 2  
        return path[::-1]


#
# @lcpr case=start
# 14\n
# @lcpr case=end

# @lcpr case=start
# 26\n
# @lcpr case=end

#

