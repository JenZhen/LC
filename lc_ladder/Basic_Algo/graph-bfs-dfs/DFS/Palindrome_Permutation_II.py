#! /usr/local/bin/python3

# https://leetcode.com/problems/palindrome-permutation-ii/submissions/
# Example
# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
#
# Example 1:
#
# Input: "aabb"
# Output: ["abba", "baab"]
# Example 2:
#
# Input: "abc"
# Output: []
"""
Algo: DFS
D.S.:

Solution:
it's a mix of palindrome_permutation and permutaion_II

注意： 必背 permuation_ii 模板
注意： 处理奇数个在中间加进去

Corner cases:
"""

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if not s:
            return []

        # populate count
        count = [0] * 256
        for ch in s:
            count[ord(ch)] += 1
        oddChar = None
        for i in range(256):
            if count[i] % 2 == 1:
                if oddChar == None:
                    oddChar = chr(i)
                else:
                    return []

        # populate candidates only half of it
        candidates = ""
        for i in range(256):
            if count[i] > 0:
                candidates += chr(i) * (count[i] // 2)

        res = []
        visited = [False for _ in range(len(candidates))]
        self.dfs(candidates, res, visited, "", oddChar)
        return res

    def dfs(self, candidates, res, visited, tmp, oddChar):
        if len(tmp) == len(candidates):
            if oddChar:
                res.append(tmp + oddChar + tmp[::-1])
            else:
                res.append(tmp + tmp[::-1])
            return
        for i in range(len(candidates)):
            if visited[i]:
                continue
            if i > 0 and candidates[i] == candidates[i - 1] and visited[i - 1] == False:
                continue
            visited[i] = True
            self.dfs(candidates, res, visited, tmp + candidates[i], oddChar)
            visited[i] = False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
