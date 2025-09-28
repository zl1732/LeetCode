#
# @lc app=leetcode.cn id=1352 lang=python3
# @lcpr version=30203
#
# [1352] 最后 K 个数的乘积
#

# @lc code=start
class ProductOfNumbers:
    """
    1. 遇到0就重置preSum
    2. presum[-1] / presum[-1-k]
    3. k>len(preSum) return 0
    """
    def __init__(self):
        self.preSum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.preSum = [1]
        else:
            self.preSum.append(self.preSum[-1] * num)
        

    def getProduct(self, k: int) -> int:
        # 如果最后一位是0， presum = [1]
        if k >= len(self.preSum):
            return 0
        return self.preSum[-1] // self.preSum[-1-k]
        


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

