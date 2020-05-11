#! /usr/local/bin/python3

# https://leetcode.com/problems/restore-ip-addresses/submissions/
# Example
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
"""
Algo: DFS, Backtracking
D.S.:

Solution:

Time: O(2 ^ n) --> n is limited so it's constant
Space: O(n)
Corner cases:
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4 or len(s) > 12:
            return []
        res = []
        tmp = []
        self.dfs(s, tmp, res, 0)
        return res

    def dfs(self, s, tmp, res, start_idx):
        if len(tmp) == 4 and start_idx == len(s):
            res.append('.'.join(tmp))
            return

        for i in range(start_idx, len(s)):
            # 重要减枝办法
            if i >= start_idx + 3:
                continue
            left = s[start_idx:(i+1)]
            if self._valid(left):
                tmp.append(left)
                self.dfs(s, tmp, res, i + 1)
                tmp.pop()

    def _valid(self, s):
        # ‘00’ 是不合法的，如果等于0 只能有1位，不能有preceeding 0
        if len(s) > 1 and s[0] == '0':
            return False
        if 0 <= int(s) <= 255:
            return True
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
