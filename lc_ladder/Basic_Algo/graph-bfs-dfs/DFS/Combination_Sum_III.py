#! /usr/local/bin/python3

# https://leetcode.com/problems/combination-sum-iii/submissions/
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

"""
Algo: DFS
D.S.:

Solution:
Time: O(2^n)

Corner cases:
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        res = []
        self.dfs(candidates, k, res, [], 0, n)
        return res

    def dfs(self, candidates, k, res, tmp, start_idx, target):
        if target == 0 and len(tmp) == k:
            res.append(tmp[:])
            return
        if len(tmp) == k:
            return

        for i in range(start_idx, len(candidates)):
            if candidates[i] > target:
                return
            tmp.append(candidates[i])
            self.dfs(candidates, k, res, tmp, i + 1, target - candidates[i])
            tmp.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
