#! /usr/local/bin/python3

# https://www.lintcode.com/problem/bst-node-distance/description?_from=ladder&&fromId=62
# Example
# 给定一个integer数组（无序）和2个node值，按给出的数组构建 BST，找出这两个node在 BST 中的距离。
#
# 样例
# input:
# numbers = [2,1,3]
# node1 = 1
# node2 = 3
# output:
# 2
# 注意事项
# If two nodes do not appear in the BST, return -1
# We guarantee that there are no duplicate nodes in BST

"""
Algo: Recursion
D.S.: BST

Solution:
Time: O(n) -- each node handled once
Space: O(n) -- build a bst tree

Idea:
0. exclude node1, node2 not in numbers scenario, return -1
1. Build BST using recusion -- don't need to build all, as long as node1 & node2 are built
2. find LCA using recursion, assuming node1 and node2 are the same
3. find the distance from lca to node1 & node2 respectively.

Corner cases:
"""

class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        if not numbers or not node1 or not node2:
            return -1
        if node1 not in numbers or node2 not in numbers:
            return -1
        root = TreeNode(numbers[0])
        flag1 = False
        flag2 = False
        for i in range(1, len(numbers)):
            if numbers[i] == node1:
                flag1 = True
            if numbers[i] == node2:
                flag2 = True
            self._constructBST(root, numbers[i])
            if flag1 and flag2:
                break

        lca = self.lca(root, node1, node2)
        dist1 = self.dist(lca, node1)
        dist2 = self.dist(lca, node2)
        print("node1: %s" %dist1)
        print("node2: %s" %dist2)
        return dist1 + dist2

    def _constructBST(self, root, num):
        if num < root.val:
            if root.left:
                self._constructBST(root.left, num)
            else:
                root.left = TreeNode(num)
        else:
            if root.right:
                self._constructBST(root.right, num)
            else:
                root.right = TreeNode(num)

    def lca(self, root, node1, node2):
        if node1 < root.val and node2 < root.val:
            return self.lca(root.left, node1, node2)
        if node1 > root.val and node2 > root.val:
            return self.lca(root.right, node1, node2)
        return root

    def dist(self, top, nodeVal):
        step = 0
        while top.val != nodeVal:
            if nodeVal < top.val:
                top = top.left
                step += 1
            if nodeVal > top.val:
                top = top.right
                step += 1
        return step

# Test Cases
if __name__ == "__main__":
    solution = Solution()
