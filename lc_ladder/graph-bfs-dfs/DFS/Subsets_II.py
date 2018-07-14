#! /usr/local/bin/python3

# https://www.lintcode.com/problem/subsets-ii/description
# Example
# nums = [2,1,2]
# res = [[], [1], [1,2], [1,2,2], [2], [2,2]]

"""
Algo: DFS
D.S.:

Solution:
1. DFS
Same as Subsets I solutions1 (suggested solution)

Corner cases:
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res
        nums.sort()
        temp = []
        self.dfs(nums, temp, 0, res)
        return res

    def dfs(self, nums, temp, idx, res):
        res.append(temp[:])
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.dfs(nums, temp, i + 1, res)
            temp.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
