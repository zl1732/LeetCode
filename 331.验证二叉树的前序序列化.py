#
# @lc app=leetcode.cn id=331 lang=python3
# @lcpr version=30201
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    """
    你可以想象整个构建过程，每个节点“占用一个槽位”，如果是非空节点，它又会“制造两个新槽位”供其左右子节点填充。
    | 情况                | 槽位变化                  |
    | -------------      | -----------------        |
    | 读到一个节点（非 `#`）| 消耗 1 个槽位，增加 2 个槽位 |
    | 读到一个 `#`        | 消耗 1 个槽位，不再增加     |
    
    🚨 合法条件：
        槽位数必须始终 ≥ 0（不能出现负值）
        遍历完所有节点后，槽位必须正好为 0（不能剩槽位）
    """
    # 层序遍历
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        # number in queue, root only
        cnt = 1
        for cur in nodes:
            # 到达叶子，不加，减当前点
            if cur == "#":
                cnt -= 1
                # 判断
                if cnt < 0:
                    return False
            # 非叶子节点
            else:
                # 先减当前点
                cnt -= 1
                # 判断
                if cnt < 0:
                    return False
                # 加左右子树
                cnt += 2
        """这里错了，最后可能有剩余，也不行"""
        #return True
        return cnt == 0




    # 递归
    """
    # 前序递归反序列化
    class Codec:
        SEP = ","
        NULL = "#"

        def deserialize(self, data: str):
            if not data:
                return None
            nodes = data.split(self.SEP)
            return self._deserialize(nodes)

        def _deserialize(self, nodes: List[str]):
            if not nodes:
                return None
            
            val = nodes.pop(0)
            if val == self.NULL:
                return None
            root = TreeNode(val)
            # 注意这里是先构造左子树，后构造右子树
            root.left = self._deserialize(nodes)
            root.right = self._deserialize(nodes)
            return root
    """
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        def build() -> bool:
            if not nodes:
                return False  # ❗说明节点提前用完，非法！
            val = nodes.pop(0)
            if val == "#":
                return True  # 空节点，合法结束
            # 非空节点，必须有两个合法子树
            return build() and build()
        # nodes最后检测
        return build() and not nodes  # ❗不能有多余节点残留
    

        """
        "1,#,#,#"  # 非法输入
        这种不会再if val == "#"时返回True，而是会在后续的build()调用中返回False。
        return build() and 【not nodes】
        """
# @lc code=end



#
# @lcpr case=start
# "9,3,4,#,#,1,#,#,2,#,6,#,#"\n
# @lcpr case=end

# @lcpr case=start
# "1,#"\n
# @lcpr case=end

# @lcpr case=start
# "9,#,#,1"\n
# @lcpr case=end

#

