#
# @lc app=leetcode.cn id=140 lang=python3
# @lcpr version=30201
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    # 暴力+回溯，这种方法没法正确剪枝 这种方法做不出来
    """
    ❗ 统一的 self.flag 是“全局的”，但递归是“局部的”
    就像你在多条道路上探险，每条路要单独判断“是否能通往终点”。
    但你只带一个“成功旗帜”，只要有一条路插过旗，就全体都以为成功了。

    如果是问能不能找到成功路径，就可以用全局self.flag，找到一个就可以停止 139题
    但如果问全部路径，就要用分解思路
    """
    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = set()
        self.wordDict = wordDict
        self.track = []
        self.res = []
        self.flag = False
        self.dp(s, 0)
        return self.res

    def dp1(self, s, i):
        # 找到
        if i==len(s):
            self.res.append(' '.join(self.track))
            # self.flag = True
            return
        # 记录不成功的
        # if i in self.memo:
        #     return
        for word in self.wordDict:
            l = len(word)
            # 匹配到
            if i+l<=len(s) and s[i:i+l] == word:
                self.track.append(word)
                self.dp(s, i+l)
                self.track.pop()
        # if not self.flag:
        #     self.memo.add(i)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        self.wordDict = wordDict
        self.track = []
        self.res = []
        self.dp(s, 0)
        return self.res
    
    # 分解思路
    def dp1(self, s, i):
        # 找到
        if i==len(s):
            self.res.append(' '.join(self.track))
            return True
        
        # 记录不成功的
        """
        如果记录了self.memo[i] = True
        第二轮走到这里就会直接return True
        根本不会走下面的self.dp(s, i+l)，也就是没法去到if i==len(s)，走不了更新self.res
        """
        if i in self.memo:
            return self.memo[i]

        for word in self.wordDict:
            l = len(word)
            # 匹配到
            if i+l<=len(s) and s[i:i+l] == word:
                # ——① 找到一个匹配就递归
                self.track.append(word)
                subproblem = self.dp(s, i+l)
                # ——② 如果这个分支能走通，就立刻 return True（跳出整个循环）
                """
                场景：i=0，word="cat" 符合，进入 dp(s,3)
                dp(3) 又能找到 "sand"→"dog"，最终 subproblem=True
                回到 i=0，立刻执行 return True，整个 for 循环不再继续，于是…
                    永远不会试 下一个前缀 "cats"
                    只会把 "cat sand dog" 这条路径加入结果
                """
                if subproblem:
                    self.memo[i] = True
                    return True
                self.track.pop()

        # ——③ 循环跑完还没 return，就在这里记 memo[i] 并返回 False/True
        # 另外：如果if i+l<=len(s) and s[i:i+l] == word:没执行，就没有subproblem
        if not subproblem:
            self.memo[i] = False
            return False
        else:
            """
            示例
            s = "aba"
            wordDict = ["a", "b", "ab"]
            合法拆分有两种：
                "a" + "b" + "a" ⇒ "a b a"
                "ab" + "a" ⇒ "ab a"
            具体执行流程
                首次到达 i=0
                    prefix="a" 匹配，track=["a"] → 调 dp(1)
                首次到达 i=1
                    试 prefix="b"，track=["a","b"] → 调 dp(2)
                首次到达 i=2
                    试 prefix="a"，track=["a","b","a"] → i==3，执行
                    res.append("a b a")
                    return True
                    回到 i=2，success=True；
                    循环完毕后 memo[2] = True，return True
                回到 i=1
                    dp(2) 已经返回 True，标记 success=True；
                    循环完毕后 memo[1] = True，return True
                回到 i=0
                    dp(1) 返回 True，success=True；
                    继续尝试下一个前缀 prefix="ab"：
                        此时调用 dp(2)
                        立刻命中 if i in memo: return memo[i]
                        ➔ 根本不走递归体，也就不会 res.append("ab a")
                    循环结束后，memo[0] = True，return True
            最终 res 里只有 ["a b a"]，而缺少了 "ab a"。
            """

            """
            在 139（Word Break I）里，dp(i) 只关心“能不能从位置 i 拆到末尾”这一布尔值，所以：
            记录 False（剪枝失败路径）是必须的
            当某个 i 无论怎么拆都不通时，把 memo[i] = False，下次再遇到就直接返回 False，不会再白费功夫。
            
            为什么 140（Word Break II）不能同样存 True？
            在列出所有拆分结果时，存 memo[i]=True 会把“这个起点一定成功”当成“以后都不必再试”，导致后续分支（新的组合）永远得不到探索，从而漏掉答案。
            """

            """
            ❗问题一：return True 会提前结束整个 for 循环
                一旦找到第一个能拼成功的路径，你就立刻 return
                后面的其他词、其他路径根本没机会被尝试
                所以只能得到 "cat sand dog"，而 "cats and dog" 这样的路径就永远走不到了
            ❗问题二：self.memo[i] = True 会缓存成功，但阻断后续递归
                如果你后面某条路径刚好也要从这个 i 开始（例如第二轮要从 i=0 重新开始）
                会因为 if i in self.memo 命中，直接跳出递归返回 True
                于是你再也不会进入 if i == len(s)，也就无法更新 self.res.append(...)
                所以，哪怕那条路径本来也能走到底、生成结果，也没机会进入终点来更新答案
            """
            self.memo[i] = True
            return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)  # 提升查找效率
        self.res = []
        self.track = []
        self.memo_fail = set()  # 只记录失败位置
        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, i: int) -> bool:
        if i == len(s):
            self.res.append(' '.join(self.track))
            return True

        if i in self.memo_fail:
            return False

        success = False

        for word in self.wordDict:
            l = len(word)
            if i + l <= len(s) and s[i:i+l] == word:
                self.track.append(word)
                if self.dfs(s, i + l):  # 尽管成功，也继续尝试其它组合
                    success = True
                self.track.pop()

        if not success:
            self.memo_fail.add(i)  # 剪枝：这个位置起步的路径全失败

        return success
    

"""
第二轮要学习的写法：
# ✅ 更推荐的写法（返回值 + memo + 拼接）：
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    # 拿到后面所有合法句子
                    for sub in dfs(end):
                        if sub == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + sub)

            memo[start] = sentences
            return sentences

        return dfs(0)
         
    
        
# @lc code=end



#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

