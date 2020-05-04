#! /usr/local/bin/python3

# https://leetcode.com/problems/strobogrammatic-number-ii/submissions/
# Example
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
# Input:  n = 2
# Output: ["11","69","88","96"]
"""
Algo: DFS, Backtracking
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        MAP = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        LIST = ['0', '1', '6', '8', '9']
        # 单独处理 长度为0 和 1的情况
        if not n: return [""]
        if n == 1: return ['0', '1', '8']
        res = []
        tmp = ['' for _ in range(n)]
        self.dfs(0, len(tmp) - 1, tmp, res, MAP, LIST)
        return res

    def dfs(self, l, r, tmp, res, MAP, LIST):
        if l > r:
            res.append(''.join(tmp[:]))
            return
        for i in range(len(LIST)):
            if l == 0 and LIST[i] == '0':
                continue
            if (l == r) and (LIST[i] == '6' or LIST[i] == '9'):
                continue
            tmp[l] = LIST[i]
            tmp[r] = MAP[tmp[l]]
            self.dfs(l + 1, r - 1, tmp, res, MAP, LIST)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
