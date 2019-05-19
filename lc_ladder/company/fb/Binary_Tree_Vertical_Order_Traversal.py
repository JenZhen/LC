#! /usr/local/bin/python3

# https://www.lintcode.com/problem/binary-tree-vertical-order-traversal/description
# Example
# 给定二叉树，返回其节点值的垂直遍历顺序。 (即逐列从上到下)。
# 如果两个节点在同一行和同一列中，则顺序应 从左到右。
#
# Example
# 样例1
#
# 输入： {3,9,20,#,#,15,7}
# 输出： [[9],[3,15],[20],[7]]
# 解释：
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# 样例2
#
# 输入： {3,9,8,4,0,1,7}
# 输出：[[4],[9],[3,0,1],[8],[7]]
# 解释：
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7

"""
Algo: BFS + map
D.S.: binary tree

Solution:
纵向的level巧妙记录

Corner cases:
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        from collections import deque
        if not root:
            return []
        res = []
        q = deque([(root, 0)])
        level_map = {0: [root.val]}
        while q:
            (cur_node, level) = q.popleft()
            if cur_node.left:
                q.append((cur_node.left, level - 1))
                if level - 1 not in level_map:
                    level_map[level - 1] = []
                level_map[level - 1].append(cur_node.left.val)
            if cur_node.right:
                q.append((cur_node.right, level + 1))
                if level + 1 not in level_map:
                    level_map[level + 1] = []
                level_map[level + 1].append(cur_node.right.val)

        print(level_map)
        for key in sorted(level_map):
            res.append(level_map[key])
        print(res)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()