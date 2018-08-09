#! /usr/local/bin/python3

# https://www.lintcode.com/problem/permutations-ii/description
# With duplication
# Example
# For numbers [1,2,2] the unique permutations are:
# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]

"""
Algo: DFS, Recursion, non-Recursion
D.S.:

Solution:
1. DFS, Recursion
How to deal with duplication:
- nums sorted O(nlogn)
- if nums[i] == nums[i - 1],如果前面的元素没有算入，那么这个也不能被算入

Time: O(N!) n * (n - 1) * (n - 2) *... * 1
Space: O(N) for visited, perm
2. Non-Recursion

Corner cases:
"""

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res

        visited = [False] * len(nums)
        perm = []
        nums.sort()
        self.dfs(nums, visited, perm, res)
        return res

    def dfs(self, nums, visited, perm, res):
        if len(nums) == len(perm):
            res.append([ele for ele in perm])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue
            perm.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, perm, res)
            visited[i] = False
            perm.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
