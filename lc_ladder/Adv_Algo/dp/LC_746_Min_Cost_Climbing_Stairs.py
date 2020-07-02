#! /usr/local/bin/python3

# https://www.lintcode.com/problem/min-cost-climbing-stairs/description
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Example
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.
#
# Example
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# Notice
# 1.cost will have a length in the range [2, 1000].
# 2.Every cost[i] will be an integer in the range [0, 999].
"""
Algo: DP
D.S.:

Solution:
idx    -1, 0,  1,  2, 3, 4,  5,  6, 7,  8,  9
input     [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
mincost 0, 1,  101,2, 3, 3, 103, 4, 5, 104, 6

f[x, x] init with f[0] = 1 f[1] = 0 (for idx = -1)

Corner cases:
"""

class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        if not cost:
            return 0
        # starting position indexed as -1 with minCost = 0
        f = [cost[0], 0]
        for i in range(1, len(cost)):
            f[i % 2] = min(f[(i - 1) % 2], f[(i - 2) % 2]) + cost[i]
        return min(f)

class Solution2:
    # 没有pre-padding
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        if len(cost) == 1: return cost[-1]

        arr = [0, 0]
        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(2, len(cost)):
            arr[i % 2] = min(arr[(i - 2) % 2], arr[(i - 1) % 2]) + cost[i]
        return min(arr)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
