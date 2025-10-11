#
# @lc app=leetcode.cn id=1109 lang=python3
# @lcpr version=30203
#
# [1109] 航班预订统计
#

# @lc code=start
"""
差分法，前缀和的逆运算

现在有个操作：在区间 [2,4] 每个位置 +10。
    执行操作 [l=2, r=4, val=10]：

    diff[2] += 10     → [0, 0,10, 0, 0, 0]
    diff[5] -= 10     → [0, 0,10, 0, 0,-10]

    🔄 还原原数组（前缀和）
    cur = 0
    i=1 → cur=0+diff[1]=0   → res[1]=0
    i=2 → cur=0+diff[2]=10  → res[2]=10
    i=3 → cur=10+diff[3]=10 → res[3]=10
    i=4 → cur=10+diff[4]=10 → res[4]=10
    i=5 → cur=10+diff[5]=0  → res[5]=0

    

差分数组（difference array）和前缀和（prefix sum）本质上就是一对逆运算：
🔄 关系
前缀和：
    已知原数组 nums，构造前缀和数组 pre：
    pre[i] = nums[0] + nums[1] + ... + nums[i]
    👉 作用：快速算区间和。

差分数组：
    已知原数组 nums，构造差分数组 diff：
    diff[i] = nums[i] - nums[i-1]   (i>=1)
    diff[0] = nums[0]
    👉 作用：快速做区间修改。
    
📐 它们互为逆运算
    从 原数组 → 差分数组：做一次减法。
    从 差分数组 → 原数组：做一次前缀和。

💡 应用场景
    前缀和：很多区间查询题（区间和、区间最大值…）
    差分数组：很多区间修改题（区间加、区间赋值…）

用途：
    差分数组这个适合做多次操作，然后最后统一扫一遍前缀和，完成所有操作的累加

局限性：
    区间连续修改，多次操作：比如航班预订、区间加 k、批量更新。
    最终一次性输出：比如「所有操作完成后输出结果」。

❌ 什么时候差分数组不合适
    只有一次或很少几次操作
    操作的下标是零散的（不连续）
    需要中途多次查询
    

对比：
    不用差分，遇到一个操作 [l,r,val]，我们就必须：
        for i in range(l, r+1):
            res[i] += val
    这个操作复杂度是 O(r-l+1)。
    如果有 m 个操作，最坏情况下每个操作都覆盖整个数组长度 n，
    总复杂度就是 O(m·n)。

    使用差分法：
        diff[l] += val
        diff[r+1] -= val
    所以是 O(1)。
    所有 m 个操作完成后，再扫一遍长度为 n 的数组做前缀和，还原结果： O(n)。
    总复杂度就是 O(m + n)。



"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)  # 多开一位，处理 r+1 下标
        
        for first, last, seats in bookings:
            diff[first] += seats
            diff[last + 1] -= seats
        
        res = [0] * n
        cur = 0
        for i in range(1, n + 1):
            cur += diff[i]
            res[i - 1] = cur
        return res


    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)  # 多开一位，处理 r+1 下标
        for start, end, seats in bookings:
            diff[start] += seats
            diff[end+1] -= seats
        print(diff)
        res = [0] * n
        for i in range(1, n+1):
            diff[i] += diff[i-1]
            res[i-1] = diff[i]
        return res
        


# @lc code=end



#
# @lcpr case=start
# [[1,2,10],[2,3,20],[2,5,25]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,10],[2,2,15]]\n2\n
# @lcpr case=end

#

