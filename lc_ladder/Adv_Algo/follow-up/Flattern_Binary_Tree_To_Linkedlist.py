#! /usr/local/bin/python3

# https://lintcode.com/problem/flatten-binary-tree-to-linked-list/description
# Example
# Flatten a binary tree to a fake "linked list" in pre-order traversal.

# Here we use the right pointer in TreeNode as the next pointer in ListNode.

# Example
#               1
#                \
#      1          2
#     / \          \
#    2   5    =>    3
#   / \   \          \
#  3   4   6          4
#                      \
#                       5
#                        \
#                         6
# Challenge
# Do it in-place without any extra memory.

# Notice
# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.


"""
Algo: Divide-Conquer; Iteration,
D.S.: Stack

Solution:
Time: O(n) -- each node is handle exactly once, Space O(1), in-space
1. Divide-Conquer
2. Recursively traverse node (TODO: 不理解)
3. Tree in-order iteration
Use stack to keep the in-order node visiting order
st:  1,    5, 2,              4, 3 ,        6
res:    1,      (re-link), 2,      3, 4, 5,    6

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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return None

        leftRes = self.flatten(root.left)
        rightRes = self.flatten(root.right)

        # if there is leftRes, need to merge
        if leftRes:
            leftRes.right = root.right
            root.right = root.left
            root.left = None

        # handle return value
        if rightRes:
            return rightRes
        elif leftRes:
            return leftRes
        else:
            return root

class Solution2:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def __init__(self):
        self.pre = None
    def flatten(self, root):
        # write your code here
        if not root:
            return
        if self.pre:
            self.pre.left = None
            self.pre.right = root

        self.pre = root
        right = root.right # Must leave right out, do not use root.right, root is changed
        self.flatten(root.left)
        self.flatten(right)


class Solution3:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        if not root:
            return
        st = [root]
        while st:
            top = st.pop()
            if top.right:
                st.append(top.right)
            if top.left:
                st.append(top.left)

            top.left = None
            if st:
                top.right = st[-1]
            else:
                top.right = None
        return root
# Test Cases
if __name__ == "__main__":
    solution = Solution()
