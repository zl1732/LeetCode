#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30201
#
# [139] 单词拆分
#
"""
标准的动态规划问题一定是求最值的，因为动态规划类型问题有一个性质叫做「最优子结构」，
即从子问题的最优解推导出原问题的最优解。

但在我们平常的语境中，就算不是求最值的题目，
只要看见使用备忘录消除重叠子问题，我们一般都称它为动态规划算法。
严格来讲这是不符合动态规划问题的定义的，说这种解法叫做「带备忘录的 DFS 算法」可能更准确些。
不过咱也不用太纠结这种名词层面的细节，既然大家叫的顺口，就叫它动态规划也无妨。
"""
"""
暴力回溯完整代码
def traverse(root: TreeNode):
    for child in root.children:
        # 前序位置需要的操作
        traverse(child)
        # 后序位置需要的操作1
    # 后序位置需要的操作2
后序位置 1（中间后序）	每个 child 遍历完后，立即执行一次处理；比如收集 child 返回值、合并结果
后序位置 2（最终后序）	所有 children 遍历完之后，统一对当前 root 做一次整体处理；比如汇总子树信息、判断完整性、加总大小等

位置1举例：最大高度
    max_child_depth = 0
    for child in root.children:
        child_depth = max_depth(child)
        
        # ✅ 后序位置1：当前 child 的递归已完成，获取它的高度来更新最大高度
        max_child_depth = max(max_child_depth, child_depth)
    
    # 后序位置2：所有 children 处理完后，加上当前节点本身
    return max_child_depth + 1

位置2举例：统计节点总数
    for child in root.children:
        count += count_nodes(child)   # 遍历子树
        # 后序1：可以在这里 debug 每个子树的结果
    # 后序2：此时 count 里是所有子节点数量，别忘加 root 自己
    return count + 1
"""
from typing import List

class Solution:
    def __init__(self):
        self.wordDict = []
        self.found = False
        # 记录回溯算法的路径
        self.track = []
        # 记录不能切分成功的后缀，剪枝用
        self.memo = set()


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.backtrack(s, 0)
        return self.found
    
    def backtrack(self, s: str, i: int):
        """
        没有返回值，你无法直接通过 return True 来终止上层调用。
        所以就需要用 self.flag 这样的“全局标志变量”来通知所有递归分支：
        ❗“找到了，大家都可以停了。”
        | 名称          | 是否必要       | 用途                       |
        | -----------  | ----------    | ------------------------ |
        | 没有返回值的递归| ✅ 必须用 flag | 否则无法终止整棵搜索树              |
        | 有返回值的递归  | ❌ 不需要 flag | 直接 `return True` 即可结束搜索树 |

        """
        # base case
        if self.found:
            # 如果已经找到答案，就不要再递归搜索了
            return
        if i == len(s):
            # 整个 s 都被匹配完成，找到一个合法答案
            self.found = True
            return

        for word in self.wordDict:
            # 看看哪个单词能够匹配 s[i..] 的前缀
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                # 找到一个单词匹配 s[i..i+length)
                # 做选择
                self.track.append(word)
                # 进入回溯树的下一层，继续匹配 s[i+length..]
                self.backtrack(s, i+length)
                # 撤销选择
                self.track.pop()

    """
    ✅ 加上 memo 的暴力回溯完整代码
    """
    def backtrack(self, s: str, i: int):
        if self.found:
            return

        # base case：刚好切分完
        if i == len(s):
            self.found = True
            return
        """
        右边先解决 → 左边才能确定
        通过后序位置记录无法达成目标的“右侧子序列”，避免重复探索失败路径。

        s = "catsandog"
        - 尝试 "cat" -> 递归 i = 3
            - 尝试 "sand" -> 递归 i = 7
                - 尝试 "og" -> i = 7 继续失败
        - 回溯
        - 尝试 "cats" -> 递归 i = 4
            - 尝试 "and" -> 递归 i = 7
                - 尝试 "og" again

        """
        suffix = s[i:]
        # 剪枝：这个后缀之前尝试过失败了
        if suffix in self.memo:
            return

        """
        这段可以优化
        wordDict = set(wordDict)  # 放在函数开头一次转换
        for length in range(1, len(s) - i + 1):
            prefix = s[i:i+length]
            if prefix in wordDict:
                # 合法单词，进入下一层
        """
        for word in self.wordDict:
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                self.track.append(word)
                self.backtrack(s, i + length)
                self.track.pop()

        # 后序位置：如果没有找到合法路径，记录失败
        """
        必须保留 if not self.found: 这一行，否则你会把一些成功路径也错记为失败路径，或者根本不记失败路径
        """
        if not self.found:
            self.memo.add(suffix)


#| 方法                | 返回值               | 剪枝依据               | 是否短路        | 能否完全记忆      |
#| --------------     | ------------------- | --------------------- | ---------      | -----------      |
#| 🔴 暴力回溯（你这段）  | 没有显式返回值        | `self.found` 和 `memo`| ❌ 遍历所有路径   | ❌ 不能提前终止递归  |
#| 🟢 记忆化 DFS（dp）  | `return True/False` | 直接缓存每个子问题返回值  | ✅ 找到一个即返回 | ✅ 子问题结果直接记忆 |

"""
🟢 记忆化 DFS（dp）
"""
class Solution:
    # 用哈希集合方便快速判断是否存在
    def __init__(self):
        self.wordDict = set()
        # 备忘录，-1 代表未计算，0 代表无法凑出，1 代表可以凑出
        self.memo = []

    # 主函数
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 转化为哈希集合，快速判断元素是否存在
        self.wordDict = set(wordDict)
        # 备忘录初始化为 -1
        self.memo = [-1 for _ in range(len(s))]
        return self.dp(s, 0)

    # 定义：s[i..] 是否能够被拼出
    def dp(self, s: str, i: int) -> bool:
        # base case
        if i == len(s):
            return True
        # 防止冗余计算
        if self.memo[i] != -1:
            return False if self.memo[i] == 0 else True

        # 遍历 s[i..] 的所有前缀
        for length in range(1, len(s) - i + 1):
            # 看看哪些前缀存在 wordDict 中
            prefix = s[i: i + length]
            if prefix in self.wordDict:
                # 找到一个单词匹配 s[i..i+len)
                # 只要 s[i+len..] 可以被拼出，s[i..] 就能被拼出
                sub_problem = self.dp(s, i + length)
                if sub_problem == True:
                    self.memo[i] = 1
                    """
                    🔁 如果你去掉了 return True 会发生什么？
                    if sub_problem == True:
                        self.memo[i] = 1
                        # 没有 return True
                    这会导致即使你已经找到了成功路径，函数仍然继续跑剩下的循环，最后默认走到了：
                    """
                    return True

        # s[i..] 无法被拼出
        self.memo[i] = 0
        return False
    

"""
从下而上的dp:

dp[i] 表示：s[0:i] 是否能被字典中的单词组成（注意是左闭右开）
🚶‍♂️ 状态转移逻辑：
对于每个 i，我们枚举所有可能的前缀 s[j:i]

如果：
    dp[j] == True（表示前一段 s[0:j] 是可拆分的）
    且 s[j:i] in wordDict
那就说明 s[0:i] 是可以拆分的，设 dp[i] = True
"""
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串可以被“凑”出来

    word_set = set(wordDict)
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
    

######################## 第二次记录 ########################

### 分解思路 回溯
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        self.memo = [-1 for _ in range(len(s))]
        return self.dp(s, 0)
    
    # 原始版本
    def dp(self, s: str, i: int) -> bool:
        if i == len(s):
            return True

        for word in self.wordDict:
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                """
                不能直接 return self.dp(...)！！
                    因为：只要第一个匹配成功的单词递归失败，就立刻 return False，不会尝试其他可能的单词！
                # 关于True是如何传递的：
                    ✅ dp(8) 返回了 True，是怎么“传”给上层 dp(4) 的
                    用self.dp(s, i + length) 层层传递
                """
                sub_problem = self.dp(s, i + length) # ✅ 接住下层的返回值
                if sub_problem == True:
                    return True
        return False
    

# @lc code=start
# 自己写 回溯
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.track = []
        self.wordDict = wordDict
        self.flag = False
        self.backtrack(s,0)
        return self.flag

    def backtrack(self, s, i):
        # i 当前走到index
        if self.flag:
            return
        # 末尾空串=能走到这说明找到了
        if i == len(s):
            self.flag = True
            return
        # 回溯, word每个都是一个node
        for word in self.wordDict:
            l = len(word)
            # 控制不要超过限度 & 匹配
            if i+l <= len(s) and s[i:i+l] == word:
                self.track.append(word) # 可以不要，只是遵循backtrack框架
                self.backtrack(s, i+l)
                self.track.pop()

# 自己写暴力回溯+memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.track = []
        # memo记录前面可以被拆分的子序列,可以记录i也可以记录完整序列
        self.memo = set()
        self.wordDict = wordDict
        self.flag = False
        self.backtrack(s,0)
        return self.flag

    def backtrack(self, s, i):
        # i 当前走到index
        if self.flag:
            return
        # 走到末尾=找到了
        # 只有能走到这一步才说明找到，不一定能走到这里
        if i == len(s):
            self.flag = True
            return
        # memo
        right = s[i:]
        if right in self.memo:
            return 
        
        # 回溯, word每个都是一个node
        for word in self.wordDict:
            l = len(word)
            # 控制不要超过限度 & 匹配
            if i+l <= len(s) and s[i:i+l] == word:
                self.track.append(word) # 可以不要，只是遵循backtrack框架
                self.backtrack(s, i+l)
                self.track.pop()
        # 后序位置2 尝试了所有word都不行，s[i:]找不到匹配
        if not self.flag:
            self.memo.add(s[i:])


# 自己写分解思路 回溯
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        self.wordDict = wordDict
        return self.backtrack(s,0)
        
    def backtrack(self, s, i):
        if i == len(s):
            return True
        for word in self.wordDict:
            l = len(word)
            if i+l <= len(s) and s[i:i+l] == word:
                if self.backtrack(s, i+l):
                    return True
        return False

# 自己写分解思路 回溯 + memo
    def backtrack(self, s, i):
        if i == len(s):
            return True
        """
        这样写是错的！
        ⚠️ 如果没在 memo 里（即从没尝试过），就立即返回 True
        比如：
            s = "catsandog"
            wordDict = ["cat", "cats", "and", "sand", "dog"]
        i = 3，s[3:] = "sandog" 不在 memo
        直接 return True 错啦！
        """
        if i in self.memo:
            return False
        else:
            return True
        
        for word in self.wordDict:
            l = len(word)
            if i+l <= len(s) and s[i:i+l] == word:
                if self.backtrack(s, i+l):
                    return True
        self.memo.add(i)
        return False

    def backtrack(self, s, i):
        if i == len(s):
            return True
        # 应该用一个dict直接记录True False
        if i in self.memo:
            return self.memo[i]  # ✅ 返回缓存的计算结果

        for word in self.wordDict:
            l = len(word)
            if i + l <= len(s) and s[i:i + l] == word:
                if self.backtrack(s, i + l):
                    self.memo[i] = True # 👈 这个赋值虽然没错，但确实是“不会被用到”的
                    return True

        self.memo[i] = False
        return False


# @lc code=end



def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串可以被“凑”出来

    word_set = set(wordDict)
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]



def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    ws = set(wordDict)
    
    dp = [False] * (n+1)
    dp[0] = True # 空字符

    for i in range(i, n+1):
        for j in range(i):
            if s[j:i] in ws:
                if dp[j]:
                    dp[i] = True
                    # 注意
                    break
    return dp[n]





        


#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

