#! /usr/local/bin/python3

# https://www.lintcode.com/problem/house-robber-iii/
# https://leetcode.com/problems/house-robber-iii/
# Example
# The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called the "root." Besides the root,
# each house has one and only one parent house. After a tour, the smart thief realized that
# "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
# 这题是House Robber和House Robber II的扩展，只不过这次地形由直线和圈变成了二叉树
#
#   3
#  / \
# 2   3
#  \   \
#   3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#     3
#    / \
#   4   5
#  / \   \
# 1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
Algo: (DP), divide-conquer, DFS
D.S.:

Solution:
Time: O(1)
Space: O(1)

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
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        if not root:
            return 0
        # return [take, nottake]
        return max(self.helper(root))
    def helper(self, node):
        if node is None:
            return [0, 0]

        leftValue = self.helper(node.left)
        rightValue = self.helper(node.right)
        takeValue = leftValue[1] + rightValue[1] + node.val
        nottakeValue = max(leftValue) + max(rightValue)
        return [takeValue, nottakeValue]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
