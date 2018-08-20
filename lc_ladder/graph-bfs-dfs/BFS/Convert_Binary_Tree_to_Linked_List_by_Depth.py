#! /usr/local/bin/python3

# https://www.jiuzhang.com/solution/convert-binary-tree-to-linked-lists-by-depth/
# 给一棵二叉树，设计一个算法为每一层的节点建立一个链表。也就是说，如果一棵二叉树有D层，那么你需要创建D条链表。
# Example

"""
Algo: BFS, DFS
D.S.: Binary Tree

Solution:
1. BFS -- Same with level order traversal
2. DFS -- Note: that to maintain the correct order, dfs(node.right) then dfs(node.left)

Corner cases:
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution1: # BFS
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        res = []
        if not root:
            return res
        from collections import deque
        q = deque([root])
        while len(q):
            size = len(q)
            dummy = ListNode(-1)
            runner = dummy
            for i in range(size):
                cur = q.popleft()
                newListNode = ListNode(cur.val)
                runner.next = newListNode
                runner = runner.next
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(dummy.next)
        return res

class Solution2: # DFS
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        res = []
        if not root:
            return res
        self.dfs(root, 1, res)
        return res

    def dfs(self, node, depth, res):
        if not node:
            return
        newListNode = ListNode(node.val)
        if depth > len(res):
            # reach to a new level
            res.append(newListNode)
        else:
            # add node to existing lists
            newListNode.next = res[depth - 1] # make the new node the head of the list (instead of the tail)
            res[depth - 1] = newListNode # res[depth - 1] records head of the list
        self.dfs(node.right, depth + 1, res) # since append head, we need to check node.right first so the list order is correct
        self.dfs(node.left, depth + 1, res)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
