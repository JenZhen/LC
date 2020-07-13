#! /usr/local/bin/python3

# https://leetcode.com/problems/24-game/submissions/
# Example
# You have 4 cards each containing a number from 1 to 9.
# You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example,
# with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
Algo: DFS, Permutations
D.S.:

Solution:
在现有的Nums 中，任取2个数，他们计算的可能结果，和剩下的 数拼成一个新的nums,
继续计算，直到 最后nums中只有 1个数， 且这个数是24 那么就找到了解

Time Complexity: O(1). There is a hard limit of 9216 possibilities, and we do O(1)O(1) work for each of them.
Space Complexity: O(1). Our intermediate arrays are at most 4 elements, and the number made is bounded by an O(1)O(1) factor.

Corner cases:
"""

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        return self.dfs(nums)

    def dfs(self, nums):
        if len(nums) == 1 and abs(nums[0]-24) < 0.00000001:
            return True
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # 从现有的nums 中任取2个不一样的数
                remaining = []
                # 记录剩下的元素在remaining中
                for k in range(len(nums)):
                    if k != i and k != j:
                        remaining.append(nums[k])
                for permutation in self.possibilities(nums[i], nums[j]):
                    if self.dfs(remaining+[permutation]):
                        return True
        return False


    def possibilities(self, a, b):
        if a != 0 and b != 0:
            return [a + b, a - b, b - a, a * b, a / b, b / a]
        elif a != 0: # b == 0
            return [a + b, a - b, b - a, a * b, b / a]
        elif b != 0: # a == 0
            return [a + b, a - b, b - a, a * b, a / b]
        else: # a == 0 and b == 0
            return [0]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
