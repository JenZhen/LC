#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: Recursion, Divide-and-Conquer
D.S.: Binary Tree

Solution:
O(N) each node is visited once

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
    @param root: the root
    @return: minimum sum
    """
    def minimumSum(self, root):
        # Write your code here
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minimumSum(root.left), self.minimumSum(root.right)) + root.val
        elif root.left and not root.right:
            return self.minimumSum(root.left) + root.val
        elif root.right and not root.left:
            return self.minimumSum(root.right) + root.val
        else:
            return root.val

# Test Cases
if __name__ == "__main__":
    solution = Solution()
