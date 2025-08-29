#
# @lc app=leetcode.cn id=264 lang=python3
# @lcpr version=30201
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    """
    这个题类似于合并两个有序链表
    生成2 3 5的倍数序列
    去重是重点，关键在于用三个if，不能用else，相同值会在三个序列分别判定
    """

    # GPT 解法
    def nthUglyNumber1(self, n: int) -> int:
        ugly = [1] + [0]* (n-1)  # 初始化丑数数组，第一个是1

        # 三个指针分别指向将乘以 2、3、5 的位置
        i2 = i3 = i5 = 0

        for i in range(1, n):
            # 当前三个候选丑数
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5

            # 取最小值放入 ugly
            ugly[i] = min(next2, next3, next5)

            # 推进对应的指针，避免重复
            if ugly[i] == next2:
                i2 += 1
            if ugly[i] == next3:
                i3 += 1
            if ugly[i] == next5:
                i5 += 1

        return ugly[-1]


    """
    # labuladong解法，注意
    ugly[0] 是浪费掉的位置，用作“下标占位”，不用参与运算。
    """
    def nthUglyNumber(self, n: int) -> int:
        # 理解为三个指向有序链表头结点的指针
        p2, p3, p5 = 1, 1, 1
        # 理解为三个有序链表的头节点的值
        product2, product3, product5 = 1, 1, 1
        # 理解为最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 理解为结果链表上的指针
        p = 1
        while p <= n:
            min_val = min(product2, product3, product5)
            ugly[p] = min_val
            p += 1
            # 前进对应有序链表上的指针
            if min_val == product2:
                product2 = 2 * ugly[p2]
                p2 += 1
            if min_val == product3:
                product3 = 3 * ugly[p3]
                p3 += 1
            if min_val == product5:
                product5 = 5 * ugly[p5]
                p5 += 1
                
        # 返回第 n 个丑数
        return ugly[n]

    # 手动填第一个丑数
    def nthUglyNumber4(self, n: int) -> int:
        # 结果数组，下标从 1 开始使用（ugly[0] 保留不用）
        ugly = [0] * (n + 1)
        ugly[1] = 1  
        product2 = ugly[p2] * 2
        product3 = ugly[p3] * 3
        product5 = ugly[p5] * 5

        p2 = p3 = p5 = 1  
        p = 2
        # 从 p = 2 开始填
        while p<=n:
            min_val = min(product2, product3, product5)
            ugly[p] = min_val
            p += 1
            if min_val == product2:
                p2 += 1
                product2 = 2 * ugly[p2]
            if min_val == product3:
                p3 += 1
                product3 = 3 * ugly[p3]
            if min_val == product5:
                p5 += 1
                product5 = 5 * ugly[p5]
        return ugly[n]



    def nthUglyNumber4(self, n: int) -> int:
        p1 = p2











"""
错误写法：
seq2 3 5是不能提前生成的，丑数的定义不是 2*1, 2*2, 2*3, 2*4， 是因式分解只有2 3 5
所以丑数是不停的动态迭代的，只是指针在丑数序列上移动
"""
def nthUglyNumber(self, n: int) -> int:
    ugly = [0] * n

    # Step 1: 预先构造好三个乘积序列
    seq2 = [1] + [0] * (n - 1)
    seq3 = [1] + [0] * (n - 1)
    seq5 = [1] + [0] * (n - 1)

    for i in range(1, n):
        seq2[i] = i * 2
        seq3[i] = i * 3
        seq5[i] = i * 5

    # Step 2: 多指针归并这三个序列
    p2 = p3 = p5 = 0
    for i in range(n):
        next_val = min(seq2[p2], seq3[p3], seq5[p5])
        ugly[i] = next_val

        if next_val == seq2[p2]:
            p2 += 1
        if next_val == seq3[p3]:
            p3 += 1
        if next_val == seq5[p5]:
            p5 += 1

    return ugly[-1]



def nthUglyNumber(n):
    # 理解为三个指向有序链表头结点的指针
    p2, p3, p5 = 1, 1, 1
    # 理解为三个有序链表的头节点的值
    product2, product3, product5 = 1, 1, 1
    # 理解为最终合并的有序链表（结果链表）
    ugly = [0] * (n + 1)
    # 理解为结果链表上的指针
    p = 1

    while p <= n:
        min_val = min(product2, product3, product5)
        ugly[p] = min_val
        p += 1
        # 前进对应有序链表上的指针
        if min_val == product2:
            product2 = 2 * ugly[p2]
            p2 += 1
        if min_val == product3:
            product3 = 3 * ugly[p3]
            p3 += 1
        if min_val == product5:
            product5 = 5 * ugly[p5]
            p5 += 1
            
    # 返回第 n 个丑数
    return ugly[n]

nthUglyNumber(10)
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

