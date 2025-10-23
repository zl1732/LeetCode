#
# @lc app=leetcode.cn id=2073 lang=python3
# @lcpr version=30203
#
# [2073] 买票需要的时间
#

# @lc code=start
class Solution:
    # [2,3,2]
    # [5,4,2,3]
    # [5,6,2,3]
    """
    首先仔细观察第k个人前后买票数量，假设第k个人需要m个票，则k前面的人也可以买k个票
    k后面的人只能买到m-1个票。结合具体每个人需要的票数
    1, k-1: min(tickets[i], m)
    k+1, -1: min(tickets[i], m-1)

    最后再加上自己买完票需要的时间

    
    总时间 
    res = 0
    for i in range(k+1): 
        res += min(tickets[i], m)
    
    for i in range(k+1, len(tickets)): 
        res += min(tickets[i], m-1)
    
    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        m = tickets[k]
        print(m)
        # k前面的人
        for i in range(k): 
            res += min(tickets[i], m)
        
        # k后面的人
        for i in range(k+1, len(tickets)): 
            res += min(tickets[i], m-1) 
        
        # 最后加上自己买的
        res += m
        return res


    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        m = tickets[k]
        print(m)
        # 或者这样写
        # k前面的人 以及k自己
        for i in range(k+1): 
            res += min(tickets[i], m)
        
        # k后面的人
        for i in range(k+1, len(tickets)): 
            res += min(tickets[i], m-1) 
        
        return res
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#

