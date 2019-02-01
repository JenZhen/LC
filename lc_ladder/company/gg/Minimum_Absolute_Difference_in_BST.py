#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-absolute-difference-in-bst/description?_from=ladder&&fromId=18
# Example

"""
Algo: Recursion, inorder
D.S.: BST

Solution:
For BST, in-order traverse is to print out nodes value in order ascendingly

IMPORTANT:
in python, when using recursion, pass in a integer is the copy not a reference
So 1) use an array like python or 2) use self class member
Time: O(n) n is number of tree nodes

Corner cases:
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution1:
    """
    @param root: the root
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        if not root:
            return 0
        import sys
        self.res = sys.maxsize
        self.prev = None
        self.inOrderDfs(root)
        return self.res

    def inOrderDfs(self, node):
        if not node:
            return
        self.inOrderDfs(node.left)
        if self.prev is None:
            self.prev = node.val
        else:
            self.res = min(self.res, node.val - self.prev)
            self.prev = node.val
        self.inOrderDfs(node.right)

class Solution2:
    """
    @param root: the root
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        if not root:
            return 0
        import sys
        res = [sys.maxsize]
        prev = [None]
        self.inOrderDfs(root, prev, res)
        return res[0]

    def inOrderDfs(self, node, prev, res):
        if not node:
            return
        self.inOrderDfs(node.left, prev, res)
        if prev[0] is None:
            prev[0] = node.val
        else:
            res[0] = min(res[0], node.val - prev[0])
            prev[0] = node.val
        self.inOrderDfs(node.right, prev, res)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
