#! /usr/local/bin/python3

# https://www.lintcode.com/problem/letter-case-permutation/description
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.
# S will be a string with length at most 12.
# S will consist only of letters or digits.
# Example
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
"""
Algo: DFS
D.S.:

Solution:
Very similar to subsets
Solution1:
iteration
Time: O(2^n)

Solution1:
BFS Time: O(2^n)


Corner cases:
"""
class Solution1:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        res = []
        if S is None:
            return res
        res.append(S) # init res with first string of S
        # i iterates thru S
        for i in range(len(S)):
            # if a number, continue, no switch
            if '0' <= S[i] <= '9':
                continue
            size = len(res)
            for j in range(size):
                # j iterates res size
                # Build a new string based on res[j]
                newStr = res[j][:i] + self.switch(res[j], i) + res[j][(i + 1):]
                res.append(newStr)
        # this is required for some question
        res.sort()
        return res

    def switch(self, S, i):
        if 'a' <= S[i] <= 'z':
            return S[i].upper()
        if 'A' <= S[i] <= 'Z':
            return S[i].lower()

class Solution_BFS:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [[]]

        for ch in S:
            size = len(res)
            if ch.isalpha():
                # if is a letter
                for i in range(size):
                    newlist = res[i][:]
                    res[i].append(ch.lower())
                    newlist.append(ch.upper())
                    res.append(newlist)
            else:
                # if a number
                for i in range(size):
                    res[i].append(ch)
        ans = []
        for li in res:
            ans.append(''.join(li))
        return ans

class Solution_DFS_BEST:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        if not S:
            return [""]

        res = []
        # S = self.transform(S)
        path = ""
        res = []
        startIdx = 0
        self.dfs(S, path, res, startIdx)
        return sorted(res)

    def dfs(self, s, path, res, startIdx):
        if startIdx == len(s):
            res.append(path)
            return
        if '0' <= s[startIdx] <= '9':
            self.dfs(s, path + s[startIdx], res, startIdx + 1)
        else:
            self.dfs(s, path + s[startIdx].lower(), res, startIdx + 1)
            self.dfs(s, path + s[startIdx].upper(), res, startIdx + 1)

class Solution_DFS_RUSTIC:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        if not S:
            return [""]

        res = []
        S = self.transform(S)
        path = ""
        res = []
        startIdx = 0
        self.dfs(S, path, res, startIdx)
        return sorted(res)

    def transform(self, S):
        res = ""
        for ch in S:
            if 'a' <= ch <= 'z' or 'A' <= 'Z':
                res += ch.lower()
            else:
                res += ch
        return res

    def dfs(self, s, path, res, startIdx):
        if startIdx == len(s):
            res.append(path)
            print(path)
            return
        if '0' <= s[startIdx] <= '9':
            path += s[startIdx]
            self.dfs(s, path, res, startIdx + 1)
        else:
            path += s[startIdx].lower()
            self.dfs(s, path, res, startIdx + 1)
            path = path[:-1]
            path += s[startIdx].upper()
            self.dfs(s, path, res, startIdx + 1)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
