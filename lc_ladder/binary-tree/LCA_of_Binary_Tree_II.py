#!/usr/bin/python
import BinaryTree
# http://www.jiuzhang.com/solution/lowest-common-ancestor-ii/
# With parent-pointer
"""
Algo: Iteration
D.S.: Binary Tree

Solution:
Straight-forward method

Time Complexity: O(N)
Space Complexity: O(N)

Corner cases:
"""

def lowestCommonAncestorII(self, root, A, B):
		# Write your code here
		dict = {}
		while A is not None:
			dict[A] = True
			A = A.parent

		while B is not None:
			if B in dict:
				return B
			B = B.parent

		return root

# Test Cases
if __name__ == "__main__":
	solution = Solution()
