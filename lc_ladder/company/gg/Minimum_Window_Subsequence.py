#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-window-subsequence/
# Example
# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such minimum-length windows, return the one with the left-most starting index.
#
# Example 1:
#
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
#
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].
"""
Algo: sliding window, two pointers
D.S.:

Solution:
i, j sliding window,
找到一个重点后，往前找起点 然后继续找

Time: O(mn)
Space: O(1)
Corner cases:
"""

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        t = 0
        i, j = 0, 0 # is beginning of s, j end of s range
        minLength = len(S) + 1
        minString = ""
        while j < len(S):
            # Going forward to match T
            if S[j] == T[t]:
                t += 1
            j += 1
            if t == len(T):
                # Going backward to match T
                t -= 1
                i = j-1
                while t >= 0:
                    if S[i] == T[t]:
                        t -= 1
                    i -= 1
                i += 1

                # Update minimum length/string when the current length is smaller
                if minLength > j - i:
                    minLength = j - i
                    minString = S[i:j]
                # 记得t = 0 归零，j = i + 1
                t = 0
                j = i + 1

        return minString

# Test Cases
if __name__ == "__main__":
    solution = Solution()
