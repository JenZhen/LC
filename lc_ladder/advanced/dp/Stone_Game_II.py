#! /usr/local/bin/python3

# https://lintcode.com/problem/stone-game-ii/description
# Example

"""
Algo: 区间类dp
D.S.:

Solution:
There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Example
For [4, 1, 1, 4], in the best solution, the total score is 18:

1. Merge second and third piles => [4, 2, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43


Corner cases:
"""

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        # write your code here
        if not A:
            return 0
        B = [0] * len(A)
        for i in range(1, len(A)):
            B[i - 1] = A[i]
        B[-1] = A[0]
        return min(self.helper(A), self.helper(B))

    def helper(self, A):
        n = len(A)
        f = [[None for _ in range(n)] for _ in range(n)]
        sum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    sum[i][j] = A[i]
                else:
                    sum[i][j] = sum[i][j - 1] + A[j]
        return self.search(0, n - 1, f, sum, A)

    def search(self, i, j, f, sum, A):
        import sys
        if f[i][j] is not None:
            return f[i][j]
        if i == j:
            f[i][j] = 0
        else:
            f[i][j] = sys.maxsize
            for k in range(i, j):
                f[i][j] = min(f[i][j], self.search(i, k, f, sum, A) + self.search(k + 1, j, f, sum, A) + sum[i][j])
        return f[i][j]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
