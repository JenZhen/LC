#! /usr/local/bin/python3

# https://www.lintcode.com/problem/subsets-ii/description
# Example
# nums = [2,1,2]
# res = [[], [1], [1,2], [1,2,2], [2], [2,2]]

"""
Algo: 顺序无关DFS
D.S.:

Solution:
1. DFS
Same as Subsets I solutions1 (suggested solution)
res: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
前序遍历查找顺序

Complexity:
Time: 经典的计算复杂度的公式 O(构造解的复杂度 * 解的个数)
O(n * 2 ^ n) --
Space: O(2 ^ n)
Corner cases:
"""

class Solution1:
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
                # if i == idx, meaning idx is selected in prev recursion, dup can be picked again
                # if i != idx, meaning idx is selected in prev for iteration, then popped, dup cannot be picked again
                continue
            temp.append(nums[i])
            self.dfs(nums, temp, i + 1, res)
            temp.pop()

# Test Cases
if __name__ == "__main__":
    testCases = [[1, 2, 2]]
    s1 = Solution1()
    for t in testCases:
        res1 = s1.subsetsWithDup(t)
        print("res1: %s" %repr(res1))
