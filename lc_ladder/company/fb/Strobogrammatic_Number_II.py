#! /usr/local/bin/python3

# https://www.lintcode.com/problem/strobogrammatic-number-ii/description
# Example
# 对称数是一个旋转180度后(倒过来)看起来与原数相同的数.找到所有长度为 n 的对称数.
#
# 样例
# 例1:
#
# 输入: n = 2,
# 输出: ["11","69","88","96"]
# 例2:
#
# 输入: n = 1,
# 输出: ["0","1","8"]

"""
Algo: DFS, Backtracking,
D.S.: map

Solution:
Time: ## TODO:
Space: O(n)

Corner cases:
"""

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        if not n:
            return [""]

        res = []
        path = ["" for _ in range(n)]
        l, r = 0, n - 1
        self.helper(l, r, path, res)
        return res

    def helper(self, l, r, path, res):
        mp = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        if l > r:
            res.append("".join(path))
            return
        if l == r:
            for ele in ['0', '1', '8']:
                path[l] = ele
                self.helper(l + 1, r - 1, path, res)

        if l < r:
            for ele in ['0', '1', '6', '8', '9']:
                if l == 0 and ele == '0':
                    continue
                path[l] = ele
                path[r] = mp[ele]
                self.helper(l + 1, r - 1, path, res)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
