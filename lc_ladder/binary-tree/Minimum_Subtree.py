#!/usr/bin/python
import BinaryTree

# http://www.jiuzhang.com/solution/minimum-subtree/
# Given a binary tree, find the subtree with minimum sum.
# Return the root of the subtree.

"""
Algo: Divide-and-Conquer
D.S.: Binary Tree

Solution_1:
Recursively calculate sum of each subtree.
Update global minSum when necessary.

Similar to;
This is a sub-problem of "Subtree with Maximum Average"
Corner cases

Solution_2: (Suggested solution)
同一种思，利用helper function的 return type来传递遍历过程中的最优解
而不是像solution_1 中用全局变量来记录最后的解

"""

class Solution_1:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the minimun weight node

    # An alternative way to init min/max other than float('inf')
    # import sys
    # minumun_weight = sys.maxint
    minSum = 0
    minNode = None

    def findSubtree(self, root):
        # Write your code here
        if root is None:
            return None
        # Don't care return of self.helper(root)
        self.helper(root)
        return self.minNode

    def helper(self, node):
        # return each node's sum
        if node is None:
            # when None node, return 0(weight 0)
            return 0
        leftSum = self.helper(node.left)
        rightSum = self.helper(node.right)
        nodeSum = leftSum + rightSum + node.val

        if minNode is None or nodeSum < minSum:
            minSum = nodeSum
            minNode = node
        # don't forget to return nodeSum
        return nodeSum


class Solution_2:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the minimun weight node

    def findSubtree(self, root):
        # Write your code here
        if root is None:
            return None
        # Don't care return of self.helper(root)
        self.helper(root)
        return self.minNode

    def helper(self, node):
        # return minsum, minNode, currentRootSum
        if node is None:
            # when None node, return 0(weight 0)
            return sys.maxsize, None, 0

        leftMinSum, leftMinNode, leftSum = self.helper(node.left)
        rightMinSum, rightMinNode, rightSum = self.helper(node.right)
        currentRootSum = leftSum + rightSum + node.val

        if leftMinSum == min(leftMinSum, rightMinSum, currentRootSum):
            return leftMinSum, leftMinNode, currentRootSum
        if rightMinSum == min(leftMinSum, rightMinSum, currentRootSum):
            return rightMinSum, rightMinNode, currentRootSum
        return currentRootSum, node, currentRootSum

# Test Cases
if __name__ == "__main__":
    solution = Solution()
