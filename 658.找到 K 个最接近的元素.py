#
# @lc app=leetcode.cn id=658 lang=python3
# @lcpr version=30203
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        先找到x的位置，然后向两端扩散
        找插入位置，右边界
        """

        p = self.left_bound(arr, x)
        i, j = p-1, p
        """
        i、j 的语义 —— 是“边界”，不是“内容” p 是第一个 ≥ x 的位置。
        左边 i 指向 x 左侧的元素；
        右边 j 指向 x 或比 x 大的第一个元素。

        举例：
            arr = [1, 2, 3, 4, 5]
            x = 3
            i = 1, j = 2
            此时区间 (i, j) 对应的实际内容是：
            arr[i+1 : j] = arr[2:2] = []   # 空区间，还没选任何数

            每扩一次（左移 i 或右移 j），窗口变大 1。
            所以窗口的真实长度 = j - i - 1

        | 变量            | 含义           | 举例            |
        | -------------- | --------        | ------------- |
        | i              | 左边界（不包含） | 初始 i = 1      |
        | j              | 右边界（不包含） | 初始 j = 2      |
        | arr[i+1:j]     | 当前选中区间     | arr[2:2] = [] |
        | 长度 = j - i - 1| 当前窗口长度    | 0             |

        """
        # while min(j,len(arr))-max(i,0) <= k:
        while j-i-1 < k:
            if i < 0:
                j += 1
            elif j >= len(arr):
                i -= 1
            elif x - arr[i] <= arr[j] - x:
                i -= 1
            else:
                j += 1
        # return arr[max(i,0):min(j,len(arr))]
        return arr[i+1:j]
    

    def left_bound(self, arr, x):
        left, right = 0, len(arr) -1
        while left <= right:
            mid = left + (right-left)//2
            if x <= arr[mid]:
                right = mid-1
            elif x > arr[mid]:
                left = mid + 1  
        return left
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,4,5]\n4\n-1\n
# @lcpr case=end

#

