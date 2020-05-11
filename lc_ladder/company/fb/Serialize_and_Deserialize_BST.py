#! /usr/local/bin/python3

# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Example
# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
Algo: Post order traversal, DFS
D.S.:

Solution:
Serialization:
postorder: left child res + right child res + root
deserialization:
reverser post order: build root node + root's right child (continue recursion) + root's left child

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

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = self.postorder(root)
        print(vals)
        return ",".join([str(val) for val in vals])

    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.val] if node else []

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        vals = [int(val) for val in data.split(',') if val]
        print('vals: ', vals)
        root = self.helper(-sys.maxsize, sys.maxsize, vals)
        return root

    def helper(self, low, high, vals):
        print(vals)
        if not vals or vals[-1] < low or vals[-1] > high:
            return None
        val = vals.pop()
        node = TreeNode(val)
        node.right = self.helper(val, high, vals)
        node.left = self.helper(low, val, vals)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Test Cases
if __name__ == "__main__":
    solution = Solution()
