#
# @lc app=leetcode.cn id=1019 lang=python3
# @lcpr version=30203
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return self.next_greater(nums)

    def next_greater(self, nums):
        n = len(nums)
        res = [0] * n
        st = []  # 存索引，保持递减（栈顶最小）

        for i in range(n):
            cur = nums[i]
            while st and cur > nums[st[-1]]:
                idx = st.pop()
                res[idx] = cur
            st.append(i)
        return res



# @lc code=end



#
# @lcpr case=start
# [2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,4,3,5]\n
# @lcpr case=end

#

