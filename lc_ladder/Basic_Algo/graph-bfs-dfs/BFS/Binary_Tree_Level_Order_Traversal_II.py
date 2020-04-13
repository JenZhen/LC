#! /usr/local/bin/python3

# https://lintcode.com/problem/binary-tree-level-order-traversal-ii/description
# Example
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

"""
Algo: BFS
D.S.: deque implmented queue;

Solution:
BFS -- Same with Level Order traversal, just need to append at head or reverse the whole order
Time: O(N)

Pitfall:
return res.reverse() is an empty list []
should do res.reverse(), then return res

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                cur_node = q.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            res.append(level[:])
        return res[::-1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
