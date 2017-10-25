#!/usr/bin/python
import BinaryTree
# http://www.jiuzhang.com/solution/convert-binary-search-tree-to-doubly-linked-list/
# Inorder traversal of binary search tree to doubly linked list
## Example
#      6
#    /  \
#   2    7
#  / \    \
# 1   4    9
#    / \  /
#   3   5 8
# Inorder traversal: 1<=>2<=>3<=>4<=>5<=>6<=>7<=>8<=>9

"""
Algo: DFS/Divide and Conquer
D.S.: Binary Search Tree

Solution:
1. DFS to get inorder traverse list of binary search tree, then connect to
doubly linked list

2. divide conquer
root 6 convert to
     6.left subtree right most <=> 6 <=> 6.right subtree left most
recusion function return the leftmost and rightmost

Time Complexity: O(N), access all nodes
Corner cases:
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution1:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        def dfs(node, list):
            if node is None:
                return
            dfs(node.left, list)
            list.append(node.val)
            dfs(node.right, list)

        nodeList = []
        # include case of root is None nodeList is empty
        dfs(root, nodeList)
        if len(nodeList) == 0:
            return None

        head = None # keep the head of this doublylinkedList
        cursor = None
        while val in nodeList:
            curNode = DoublyListNode(val)
            if head is None:
                #this is handling the first element
                head = curNode
            else:
                cursor.next = curNode
            curNode.prev = cursor
            cursor = curNode
        return head


class Solution2:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        def helper(node):
            # return
            # left subtree list <=> root <=> right subtree list
            # @start: leftmost node
            # @end: rightmost node
            if node is None:
                return None, None

            leftListStart, leftListEnd = helper(node.left)
            rightListStart, rightListEnd = helper(node.right)

            curListStart, curListEnd = node
            if leftListEnd is not None:
                leftListEnd.next = node
                node.prev = leftListEnd
                curListStart = leftListEnd
            if rightListStart is not None:
                node.next = rightListStart
                rightListStart.prev = node
                curListEnd = rightListEnd
            return curListStart, curListEnd

        newListStart, _ = helper(root)
        return newListStart


# Test Cases
if __name__ == "__main__":
	solution = Solution()
