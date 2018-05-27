#! /usr/local/bin/python3

# https://www.lintcode.com/problem/max-tree/description
# Given an integer array with no duplicates. A max tree building on this array is defined as follow:
# The root is the maximum number in the array
# The left subtree and right subtree are the max trees of the subarray divided by the root number.
# Construct the max tree by the given array.
# Example
# Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:
#     6
#    / \
#   5   3
#  /   / \
# 2   0   1
# O(n) time and memory.

"""
Algo:
D.S.: Monotonous stack (decreasing order)

Solution:
# TODO: better analysis of use cases of ascending/descending monotonous stack

Time: O(n)
Space: O(n)

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
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        import sys
        stack = []

        for i in range(len(A) + 1): # including i == len(A) will be a max int
            newNode = TreeNode(sys.maxsize) if i == len(A) else TreeNode(A[i])
            while len(stack):
                if newNode.val > stack[-1].val:
                    # when newNode val > latest stack val (making an ascending)
                    # pop the stack, the based on the new stack[-1] to decide parent relationship
                    poppedNode = stack.pop()
                    if not stack: #stack is empty:
                        newNode.left = poppedNode
                    else:
                        leftNode = stack[-1]
                        if leftNode.val > newNode.val:
                            # 6, 0 newNode 3
                            # known: 0 is 3 left child
                            # unknown 6 and 3 relationship, maybe a 4 after 3
                            newNode.left = poppedNode
                        else:
                            # 6, 3, 1, newNode sys.maxsize
                            # known: 1 is 3's right child
                            leftNode.right = poppedNode
                else:
                    # if newNode val < latest stack val, just push in stack to maintian a descending stack
                    break
            # no matter what newNode need to be pushed in stack after all
            stack.append(newNode)
        # after pushed in maxsize，original max(tree root) will be the left child of the maxsize
        # Node(maxsize) was the last one pushed to stack
        # therefore return peek.left
        return stack[-1].left

# Test Cases
if __name__ == "__main__":
    s = Solution()
