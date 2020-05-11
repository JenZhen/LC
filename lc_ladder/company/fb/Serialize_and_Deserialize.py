#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        while res[-1] == '#':
            res.pop()
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        vals = data[1:-1].split(',')
        # print(vals)
        root =  TreeNode(int(vals[0]))
        q = [root]
        cur_father_idx = 0
        isLeft = True
        for i in range(1, len(vals)):
            cur_father = q[cur_father_idx]
            if vals[i] != '#':
                node = TreeNode(int(vals[i]))
                q.append(node)
                if isLeft:
                    cur_father.left = node
                else:
                    cur_father.right = node
            if not isLeft:
                cur_father_idx += 1 # change to next father node
            isLeft = not isLeft
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
