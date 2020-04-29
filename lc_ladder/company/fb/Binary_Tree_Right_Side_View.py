#! /usr/local/bin/python3

# https://leetcode.com/problems/binary-tree-right-side-view/
# Example
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

"""
Algo: BFS
D.S.:

Solution:
BFS 每一行，从左到右，更新map中最右的元素
Q中记录行数
Time: O(N)
Space: O(N)

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        level_map = {} # key: level, val: rignt-most val
        q = collections.deque([(root, 0)])
        maxlevel = 0
        while q:
            node, level = q.popleft()
            maxlevel = max(maxlevel, level)
            level_map[level] = node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return [level_map[i] for i in range(maxlevel + 1)]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
