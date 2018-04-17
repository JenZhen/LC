#!/usr/bin/python

# http://lintcode.com/en/problem/jump-game-ii/
# Example

"""
Algo: Sequence DP
D.S.:

Solution:
Same as Jump Game 1
- State:
- Function:
- Initialization:
- Answer:

Solution1: DP
Time: O(n ^ 2)
Space: O(n)

Solution2: Greedy
Time: O(n)


Corner cases:
"""

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A or len(A) == 1:
            return 0
        length = len(A)
        f = [0] * length
        for i in range(1, length):
            for j in range(i):
                if A[j] < i - j:
                    # not reachable
                    continue
                else:
                    if f[i] == 0:
                        f[i] = f[j] + 1
                    else:
                        f[i] = min(f[i], f[j] + 1)
        return f[length - 1]

# Greedy
class Solution2:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A or len(A) == 1:
            return 0
        length = len(A)
        start, end, jump = 0, 0, 0
        while (end < length - 1):
            jump += 1
            farthest = end
            for i in range(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i
            start = end + 1
            end = farthest
        return jump
# Test Cases
if __name__ == "__main__":
    solution = Solution()
