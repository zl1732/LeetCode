#
# @lc app=leetcode.cn id=870 lang=python3
# @lcpr version=30203
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
    """
    田忌赛马

    n = len(nums1)
    # 田忌的马
    nums1.sort()
    # 齐王的马
    nums2.sort()

    # 从最快的马开始比
    for i in range(n-1, -1, -1):
        if nums1[i] > nums2[i]:
            # 比得过，跟他比
            pass
        else:
            # 比不过，换个垫底的来送人头
            pass
    """

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 先排序 nums1
        nums1.sort()

        # 把 nums2 排序，但要带上原下标
        # 这样最后能恢复到原顺序
        sorted_nums2 = sorted([(val, idx) for idx, val in enumerate(nums2)], 
                              key=lambda x: x[0], reverse=True)
        # sorted_nums2 = [(val, idx) for idx, val in enumerate(nums2)]
        # sorted_nums2.sort(key=lambda x: x[0], reverse=True)

        n = len(nums1)
        res = [0] * n

        # 双指针
        lo, hi = 0, n - 1

        # 从 nums2 的最大值开始匹配
        for val, idx in sorted_nums2:
            if nums1[hi] > val:
                # 平局，不算赢。
                # 能赢，就用最大牌去赢
                res[idx] = nums1[hi]
                hi -= 1
            else:
                # 打不过，就用最小牌送掉
                res[idx] = nums1[lo]
                lo += 1

        return res
    



# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n[1,10,4,11]\n
# @lcpr case=end

# @lcpr case=start
# [12,24,8,32]\n[13,25,32,11]\n
# @lcpr case=end

#

