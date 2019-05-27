#! /usr/local/bin/python3

# https://leetcode.com/problems/unique-binary-search-trees/
# Example

"""
Algo: DP
D.S.:

Solution:
node_num = 0: 1种
node_num = 1: 1种
node_num = 2: 2种 2个点分别为root，左右孩子为空（node_num = 0) 或是1个点（node_num = 1）


Corner cases:
"""
class Solution:
    def numTrees(self, n: int) -> int:
        if n is None: return 0
        if n == 0 or n == 1:
            return 1
        mem = [1] * (n + 1)
        mem[0] = mem[1] = 1
        for i in range(2, n + 1):
            sum = 0
            for k in range(i):
                sum += mem[k - 0] * mem[i - 1 - k]
            mem[i] = sum
        print(mem)
        return mem[n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
