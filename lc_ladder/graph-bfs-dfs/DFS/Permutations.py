#! /usr/local/bin/python3

# https://www.lintcode.com/problem/permutations/description
# With no duplication
# Example
# For nums = [1,2,3], the permutations are:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

"""
Algo: 顺序相关DFS, Recursion, non-Recursion
D.S.:

Solution:
1. DFS, Recursion
Time: O(N!) n * (n - 1) * (n - 2) *... * 1
Space: O(N) for visited, perm
2. # TODO: non-Recursion

Corner cases:
- [], return [[]]
if not nums includes 1) nums is None, nums = []
"""

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res

        visited = [False for i in range(len(nums))]
        # Alternatively, python Boolean is simple type, it's safe to do following
        # visited = [False] * len(nums)
        perm = []
        self.dfs(nums, visited, perm, res)
        return res

    def dfs(self, nums, visited, perm, res):
        if len(nums) == len(perm):
            # IMPORTANT:
            # make a copy of perm, DO NOT append perm to res
            # perm will ne modified later
            newList = perm[:]
            # newlist = [ele for ele in perm]
            res.append(newlist)
            return
        for i in range(len(nums)):
            if visited[i]:
                # if an ele in nums is used, do not use again
                continue
            perm.append(nums[i])
            visited[i] = True
            # 和combination dfs相比，顺序无关，进入下轮递归是无需记录startIdx
            # 通过visited来保障一个元素之访问一次
            self.dfs(nums, visited, perm, res)
            # backtrack reset visited value,
            # both visited and perm are list, in python, used by reference,
            # Their value is being modified in dfs
            visited[i] = False
            perm.pop()


# Test Cases
if __name__ == "__main__":
    solution = Solution()
