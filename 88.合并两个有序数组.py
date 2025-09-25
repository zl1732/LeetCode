#
# @lc app=leetcode.cn id=88 lang=python3
# @lcpr version=30203
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        👉 正确的写法是 从后往前合并，因为 nums1 后面已经留出了空间，不会覆盖前面的未处理数据。
       
         输入：
        nums1 = [1,2,5,0,0,0], m=3
        nums2 = [3,4,6],       n=3

        初始化：
        i=2 (nums1[i]=5), j=2 (nums2[j]=6), k=5

        Step 1: 比较 5 和 6 → 6 大
        nums1 = [1,2,5,0,0,6]
        i=2, j=1, k=4

        Step 2: 比较 5 和 4 → 5 大
        nums1 = [1,2,5,0,5,6]
        i=1, j=1, k=3

        Step 3: 比较 2 和 4 → 4 大
        nums1 = [1,2,5,4,5,6]
        i=1, j=0, k=2

        Step 4: 比较 2 和 3 → 3 大
        nums1 = [1,2,3,4,5,6]
        i=1, j=-1, k=1

        nums2 用完，结束。

        最终结果：
        nums1 = [1,2,3,4,5,6]
        """
        # 三个指针：i 指向 nums1 有效部分末尾，j 指向 nums2 末尾，k 指向合并数组的末尾
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:  # nums2 还有没放完的
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        

        

        
                
                

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#

