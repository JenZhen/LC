#! /usr/local/bin/python3

# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which
#  each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Or you can follow LeetCode's level order traversal serialization format,
# where each group of children is separated by the null value.
#
# For example, the above tree may be serialized as
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
#
# You do not necessarily need to follow the above suggested formats,
# there are many more different formats that work so please be creative and come up with different approaches yourself.
#
# Constraints:
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

"""
Algo: BFS (use index to loop thru without pop queue)
D.S.: list queue

Solution:
Time: O(n)
Space: O(n)
BFS: Same as regular binary tree operation

Note:
- in this case, we don't know what's the value of N.
- If a node has 3 children, they are listed as a list of nodes in children
    for example Node(5) has 3 children, Node(1), Node(2) and None, the order won't be Node(1), None and Node(2)
    aka the children are not ordered.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        res = []
        q = collections.deque([root])
        q.append(Node('*'))

        while q:
            cur_node = q.popleft()
            res.append(str(cur_node.val))
            children = cur_node.children
            if not children and cur_node.val != "*":
                # cur_node is not a * node just has no children
                q.append(Node('*'))
                continue
            if not children: # cur_node is a * node
                continue
            for kid in children:
                q.append(kid)
            q.append(Node('*')) # append a * node meaning end of cur_node children
        return ','.join(res)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        vals = data.split(',')
        if not vals or vals[0] == '':
            return None
        root = Node(vals[0], []) # note here init children as []
        q = [root] # * node doesn't get in q
        cur_father_idx = -1 # start from -1
        for i in range(1, len(vals)):
            if vals[i] == '*':
                # * meaning end of children for cur father node
                # move to next father node
                cur_father_idx += 1
                continue
            node = Node(vals[i], [])
            q.append(node)
            q[cur_father_idx].children.append(node)
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
