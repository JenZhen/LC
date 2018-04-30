#!/usr/bin/python

# http://lintcode.com/en/problem/frog-jump/
# Example

"""
Algo: Sequence DP
D.S.:

Solution: TODO
- State:
- Function:
- Initialization:
- Answer:

Time: O()
Space: O()

Solution:

Corner cases:
"""

class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        #    [0,1,3,5,6,8,12,17]
        # f[0] = {0} (set) init as 0. It can only go forward as k + 1 = 1 steps
        # f[1] = {}
        # ...
        # f[8] = {}
        f = {} # dict
        for stone in stones:
            f[stone] = set() # init a set
        f[0].add(0)

        for stone in stones:
            for k in f[stone]:
                # k - 1
                if k - 1 > 0 and stone + k - 1 in f:
                    f[stone + k - 1].add(k - 1)
                # k
                if k > 0 and stone + k in f:
                    f[stone + k].add(k)
                # k + 1
                if stone + k + 1 in f:
                    f[stone + k + 1].add(k + 1)
        return len(f[stones[-1]]) > 0

# Test Cases
if __name__ == "__main__":
    testCases = [
        [0,1,3,5,6,8,12,17], # True
        [0,1,2,3,4,8,9,11]   # False
    ]

    solution = Solution()
    for stones in testCases:
        res = solution.canCross(stones)
        print("Res: %s" %res)
