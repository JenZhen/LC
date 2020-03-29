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
<<<<<<< HEAD:lc_ladder/graph-bfs-dfs/BFS/Binary_Tree_Level_Order_Traversal_II.py

=======
>>>>>>> 6e6be9f8502d513d22931fd09d42ab273e367d36:lc_ladder/Basic_Algo/graph-bfs-dfs/BFS/Binary_Tree_Level_Order_Traversal_II.py
Corner cases:
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
        if not root:
            return []
        from collections import deque
        res = []
        q = deque([root])
        while q:
            size = len(q)
            level_tmp = []
            for i in range(size):
                cur = q.popleft()
                level_tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level_tmp[:])
        res.reverse()
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
