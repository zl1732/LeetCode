#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30203
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    """
    单调栈
    1. 正序
        单调栈记录未找到比自己大的元素的idx，遍历列表，遇到更大的元素，就将单调栈中idx依次弹出，记录为当前值
        更新逻辑：if cur > st[-1] idx=st.pop(), idx值 = cur, 总是把更小的值挤掉
        所以 单调性 是 递减
    
    2. 倒序
        单调栈记录最近的更大的值，从右向左遍历，遇到更大的值就把单调栈中挤掉
        更新逻辑：if cur > st[-1] st.pop, res of cur = st[-1], st.append(cur)
        所以 单调性 是 递减
    
    本题需要一个helper

    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # 在nums2找下一个更大的
        # greater = self.nextGreaterElement_helper1(nums2)
        
        # # 用nums2 生成查找字典
        # greater_map = {}
        # for i, num in enumerate(nums2):
        #     # 正序
        #     """ 
        #     注意
        #     nums2[greater[i]] 是错的，只有stack存的index， 结果都是数字
        #     """
        #     greater_map[num] = greater[i]

        # # 找nums1 里逐个找就行
        # res = [greater_map[i] for i in nums1]
        # return res
    
        greater = self.nextGreaterElement_helper2(nums2)
        greater_map = {}
        for i, num in enumerate(nums2):
            # 反序
            """ 不是 greater[num] """
            greater_map[num] = greater[i]
        res = [greater_map[i] for i in nums1]
        return res


    def nextGreaterElement_helper1(self, nums):
        # 正序,存索引
        st = []
        res = [-1] * len(nums)
        for i, cur in enumerate(nums):
            while st and cur > nums[st[-1]]:
                idx = st.pop()
                res[idx] = cur
            st.append(i)
        return res

    def nextGreaterElement_helper2(self, nums):
        # 反序
        st = []
        n = len(nums)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            cur = nums[i]
            while st and cur > st[-1]:
                st.pop()
            res[i] = -1 if not st else st[-1]
            st.append(cur)
        return res


# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2].\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4].\n
# @lcpr case=end

#

