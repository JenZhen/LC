#!/usr/bin/python

# http://lintcode.com/en/problem/jump-game/
# Example

"""
Algo: Sequence DP
D.S.:

Solution:
- State: f[i]: True/False, if position i can be reached
- Function: When at i, checking range A[i], if position is reachable f[j] = True
            If at i, f[i] is False, then all after i will be False, return False
            If at i, reachale to last element, return True directly.
- Initialization: f[i] = False f[0] = True
- Answer: f[length - 1]

Solution1: DP
Time: O(n ^ 2)
Space: O(n)

Solution2: Greedy
Time: O(n)
Corner cases:
"""

class Solution1:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        length = len(A)
        # init f an array of length, f[0] = True, else False
        f = [False] * length
        f[0] = True

        # Iterate to update f value
        for i in range(length):
            if f[i] == False:
                return False
            # if from i can reach out the position length - 1, return True
            if A[i] >= length - 1 - i:
                return True
            for j in range(1, A[i] + 1):
                f[i + j] = True
        # return f[length - 1] This will not be executed


def repr(arr):
    joinArr = ", ".join([str(ele) for ele in arr])
    print("[%s]" %(joinArr))


class Solution2:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        length = len(A)

        farthestPos = A[0]
        for i in range(1, length):
            if i <= farthestPos:
                # see if farthest to be updated
                farthestPos = max(farthestPos, A[i] + i)
            else:
                # i is not reachable
                return False
        return farthestPos >= length - 1


# Test Cases
if __name__ == "__main__":
    testCases = [
        [2,3,1,1,4], # True
        [3,2,1,0,4], # False
        [0,8,2,0,9], # False
        [1,1,0,1],   # False
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    for A in testCases:
        res1 = solution1.canJump(A)
        print("res1: %s" %res1)

        res2 = solution2.canJump(A)
        print("res2: %s" %res2)
