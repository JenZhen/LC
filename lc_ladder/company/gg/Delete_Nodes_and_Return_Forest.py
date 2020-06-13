#! /usr/local/bin/python3

# https://leetcode.com/problems/delete-nodes-and-return-forest/submissions/
# Example
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
# Example 1:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
# Constraints:
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
"""
Algo: BFS, Recursion (# TODO)
D.S.:

Solution:
BFS:
Time: O(N) -- iterate all nodes
Space: O(N) -- q is size of all nodes
有小细节要注意

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_BFS:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        to_delete = set(to_delete)
        res = [root]
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.val in to_delete:
                # 注意 一定要注意 有些删除的节点并没有提前放在res 集合中
                # root 提前放在 res中的
                if node in res:
                    res.remove(node)
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            if node.left:
                q.append(node.left)
                # node的孩子 在放入Q中之后就不会丢了
                # 如果他的孩子 会被删除 一定改变为 none
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
