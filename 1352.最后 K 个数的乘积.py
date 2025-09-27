#
# @lc app=leetcode.cn id=1352 lang=python3
# @lcpr version=30203
#
# [1352] 最后 K 个数的乘积
#

# @lc code=start
class ProductOfNumbers:
    """
    如果遇到 num == 0：

        把前缀数组清空，重新开始。
        因为 0 会把之前所有的乘积都清零。

    如果 k 大于上次清空后的长度，说明结果里必定有 0 → 返回 0

        否则正常用前缀积做除法。
    """
    def __init__(self):
        self.nums = []
        

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end



#
# @lcpr case=start
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]\n[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]\n
# @lcpr case=end

#

