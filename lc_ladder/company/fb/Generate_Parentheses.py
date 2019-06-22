#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    def generateParenthesis(self, n):
        path = ""
        self.res = []
        self.dfs(path, 0, 0, n)
        return self.res

    def dfs(self, path, l, r, n):
        print(l, r)
        if l > n or r > n or l < r:
            # print('test')
            return
        if n == n and r == n:
            # print('get res')
            print(path)
            self.res.append(path)
            return
        self.dfs(path + '(', l + 1, r, n)
        self.dfs(path + ')', l, r + 1, n)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    testCases = [
        3
    ]
    for t in testCases:
        res = solution.generateParenthesis(t)
        print(res)
