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

# TODO: DFS Recursive way

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


# Test Cases
if __name__ == "__main__":
    solution = Solution()
