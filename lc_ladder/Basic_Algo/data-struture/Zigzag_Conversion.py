#!/usr/local/bin/python3

# https://leetcode.com/problems/zigzag-conversion/submissions/
# Example
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
"""
Algo:
D.S.:

Solution:

Corner cases:
numRows < 0
numRows == 0 -> return s
numRows == 1 -> return s

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not numRows or numRows == 1: return s
        cnt = 2 * numRows - 2
        m = [[] for _ in range(numRows)]
        for i in range(len(s)):
            pos = i % cnt
            if 0 <= pos < numRows:
                m[pos].append(s[i])
            else:
                row_idx = 2 * numRows - pos - 2
                m[row_idx].append(s[i])
        res = ""
        for i in range(numRows):
            res += "".join(m[i])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
