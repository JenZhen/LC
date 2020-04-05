#! /usr/local/bin/python3

# https://leetcode.com/problems/validate-binary-tree-nodes/submissions/
# Example
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
#
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
#
# Note that the nodes have no values and that we only use the node numbers in this problem.
#
# Some Cases
# 1. OK
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
#
# 2. Share one child (visited before)
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
#
# 3. Child points to father (visited before)
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
#
# 4. More than 1 tree, aka more than 1 root
# Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# Output: false
#
# 5.
# n = 4
# [1,2,0,-1]
# [-1,-1,-1,-1]

"""
Algo: BFS
D.S.:

Solution:

Time: O(n)
Spcae: O(n)

Corner cases:
"""

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if not n: return True
        if len(leftChild) != len(rightChild) or len(leftChild) != n:
            return False

        # find root
        root_candidates = set([i for i in range(n)])

        for i in leftChild + rightChild:
            if i == -1:
                continue
            if not (0 <= i <= (n - 1)):
                return False
            if i in root_candidates:
                root_candidates.remove(i)
        if len(root_candidates) == 0 or len(root_candidates) > 1:
            return False

        root = root_candidates.pop()
        visited = set([root])
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            if leftChild[cur] != -1:
                if leftChild[cur] in visited:
                    return False
                q.append(leftChild[cur])
                visited.add(leftChild[cur])
            if rightChild[cur] != -1:
                if rightChild[cur] in visited:
                    return False
                q.append(rightChild[cur])
                visited.add(rightChild[cur])
        return len(visited) == n


# Test Cases
if __name__ == "__main__":
    solution = Solution()
