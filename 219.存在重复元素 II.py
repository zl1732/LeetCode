#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30203
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        长度为k的window
        检查 count 最大值 > 1
        """
        left = right = 0
        count = {}
        max_count = 0
        while right < len(nums):
            num = nums[right]
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            right += 1
            max_count = max(max_count, count[num])

            while right - left > k:
                num = nums[left]
                left+=1
                count[num] -= 1

            if max_count > 1:
                return True
        return False
    

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        count = {}

        while right < len(nums):
            num = nums[right]
            right += 1

            # if num in count and count[num]>0:
            #     count[num] += 1
            #     return True
            # else:
            #     count[num] = 1
        
            # 这样写更好
            if count.get(num, 0) > 0:
                return True
            count[num] = count.get(num, 0) + 1


            while right - left == k+1:
                num = nums[left]
                left += 1
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        return False
    


    """
    GPT 学习，这个写法很简略

    1、当窗口大小小于 k 时，扩大窗口。
    2、当窗口大小大于 k 时，缩小窗口。

    3、当窗口**大小等于** k 且发现窗口中存在重复元素时，返回 true。
    """
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        for right, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)

            if right - left == k:
                window.remove(nums[left])
                left += 1
        return False
    

    

    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     left = right = 0
    #     count = set()
    #     while right < len(nums):
    #         num = nums[right]
    #         if num in count:
    #             return True
    #         count.add(num)
    #         right += 1

    #         while right - left > k:
    #             count.remove(nums[left])
    #             left += 1
    #     return False



# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

