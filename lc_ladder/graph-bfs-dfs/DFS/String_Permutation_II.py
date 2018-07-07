#! /usr/local/bin/python3

# https://www.jiuzhang.com/solution/string-permutation-ii/
# 给出一个字符串，找到它的所有排列，注意同一个字符串不要打印两次。（题意不清）
# Example

"""
Algo: DFS, NextPermutation
D.S.:

Solution:
1. Use DFS to construct new strings
Time O(n!)
2. Use Next permutation to find next possible permutation

Corner cases:
"""
import copy
class Solution1:
    # @param {string} str a string
    # @return {string[]} all permutations
    def stringPermutation2(self, str):
        # Write your code here
        res = []
        if str is None:
            return res
        visited = [False for i in range(len(str))]
        perm = ""
        self.dfs(str, visited, perm, res)
        return res

    def dfs(self, str, visited, perm, res):
        if len(perm) == len(str):
            res.append(copy.copy(perm))
            return
        for i in range(len(str)):
            if visited[i]:
                continue
            perm += str[i]
            visited[i] = True
            self.dfs(str, visited, perm, res)
            perm = perm[:len(str) - 1]

class Solution2:
    # @param {string} str a string
    # @return {string[]} all permutations
    def stringPermutation2(self, str):
        # Write your code here
        result = []
        if str == '':
            return ['']

        s = list(str)
        s.sort()
        while True:
            result.append(''.join(s))
            s = self.nextPermutation(s)
            if s is None:
                break

        return result

    def nextPermutation(self, num):
        # write your code here
        n = len(num)
        i = n - 1
        while i >= 1 and num[i - 1] >= num[i]:
            i -= 1
        if i == 0: return None
        j = n - 1
        while j >= 0 and num[j] <= num[i - 1]:
            j -= 1
        num[i - 1], num[j] = num[j], num[i - 1]
        num[i:] = num[i:][::-1]
        return num
# Test Cases
if __name__ == "__main__":
    solution = Solution()
