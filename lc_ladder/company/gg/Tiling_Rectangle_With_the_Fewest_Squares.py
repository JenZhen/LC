#! /usr/local/bin/python3

# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/submissions/
# Example
# https://www.youtube.com/watch?v=2QRUgAT7sGc
"""
Algo: DFS, Backtracking
D.S.:

Solution:


Corner cases:
"""

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # This is optional
        # if n > m:
        #     return self.tilingRectangle(m, n)
        self.res = m * n
        self.h = [0] * n # 躺着的矩形 width is n, init with all 0s
        self.m = m # m <= n
        self.n = n
        self.dfs(0)
        return self.res

    def dfs(self, cur_cnt):
        if cur_cnt >= self.res:
            # it's a less efficient way
            return

        min_idx = 0
        min_h = min(self.h)
        if min_h == self.m:
            # all filled, min height is same as big height
            self.res = cur_cnt
            return

        for i in range(len(self.h)):
            if self.h[i] == min_h:
                min_idx = i
                break
        cursor = min_idx
        while cursor < self.n and self.h[cursor] == min_h and cursor - min_idx + 1 + min_h <= self.m:
            cursor += 1

        # make cursor back to be valid
        cursor -= 1
        # print('heights: ', self.h)
        # print('min val: ', min_idx, min_h)
        # print('cursor: ', cursor)
        for i in range(cursor, min_idx - 1, -1):
            # try all possible square size
            # from big to small
            size = i - min_idx + 1
            for j in range(min_idx, i + 1):
                self.h[j] += size
            self.dfs(cur_cnt + 1)
            for j in range(min_idx, i + 1):
                self.h[j] -= size

# Test Cases
if __name__ == "__main__":
    solution = Solution()
