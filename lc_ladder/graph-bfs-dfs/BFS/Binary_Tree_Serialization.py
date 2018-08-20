#! /usr/local/bin/python3

# https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/description
# Example
# {1,#,2}
#   1
#   /\
#  #  2

"""
Algo: BFS (use index to loop thru without pop queue)
D.S.: list queue

Solution:
Time: O(n)
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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return "{}"
        q = [root]
        index = 0
        while index < len(q):
            if q[index] is not None:
                q.append(q[index].left)
                q.append(q[index].right)
            index += 1
        '''
        # IMPORTANT: DO NOT USE for loop in this case, since len(q) of the for loop
        # condition won't change as length of q increases. Use while loop
        for index in range(len(q)):
            if q[index] is not None:
                q.append(q[index].left)
                q.append(q[index].right)
            index += 1
        '''
        while q[-1] is None:
            q.pop()
        return '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in q])

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        data = data.strip('\n')
        if data == "{}":
            return None

        vals = data[1:-1].split(',')
        idx = 0 # adding child to which node in queue
        root = TreeNode(int(vals[0]))
        q = [root]
        isLeftChild = True # consider left child first

        for i in range(1, len(vals)):
            curVal = vals[i]
            if curVal != '#':
                curNode = TreeNode(int(curVal))
                if isLeftChild:
                    q[idx].left = curNode
                else:
                    q[idx].right = curNode
                q.append(curNode)
            if not isLeftChild:
                idx += 1 # this node's right child is found, find next node in queue
            isLeftChild = not isLeftChild
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
