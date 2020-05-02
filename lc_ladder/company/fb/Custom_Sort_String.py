#! /usr/local/bin/python3

# https://leetcode.com/problems/custom-sort-string/submissions/
# Example
# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously. We want to permute the characters of T
# so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
#
# Return any permutation of T (as a string) that satisfies this property.
#
# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
#
#
# Note:
#
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
"""
Algo: Sort
D.S.:

Solution1:
构建优先级MAP
排序

Time: O(N) + O(26log26） -- T 的长度
Space: O(N) -- T 的长度

Solution2:
构建优先级MAP
用类似bucket sort

Time: O(N)
Space: O(N)
Corner cases:
"""

class Solution1:
    def customSortString(self, S: str, T: str) -> str:
        mp = {} # key: char, val: priority
        for idx, c in enumerate(S):
            mp[c] = idx # assuming no duplicate

        ll = []
        for c in T:
            if c in mp:
                ll.append((mp[c], c))
            else:
                ll.append((len(S), c))
        ll.sort(key=lambda x: x[0])
        return ''.join([x[1] for x in ll])

class Solution2:
    def customSortString(self, S: str, T: str) -> str:
        mp = {} # key: char, val: priority
        for idx, c in enumerate(S):
            mp[c] = idx # assuming no duplicate

        ll = [[] for _ in range(26)]
        for c in T:
            if c in mp:
                idx = mp[c]
                ll[idx].append(c)
            else:
                ll[-1].append(c)
        res = ''
        for l in ll:
            if len(l) > 0:
                res += ''.join(l)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
