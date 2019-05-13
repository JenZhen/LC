#! /usr/local/bin/python3

# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Example
# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which
# randomly and uniformily picks an integer point in the space covered by the rectangles.
#
# Note:
#
# An integer point is a point that has integer coordinates.
# A point on the perimeter of a rectangle is included in the space covered by the rectangles.
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner,
# and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output:
# [null,[4,1],[4,1],[3,3]]
# Example 2:
#
# Input:
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output:
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's
# constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
Algo: random， binary search，presum
D.S.:

Solution:
1. 先算出每个矩形里包含多少个点，根据此加权做presum
2. random 定位到某个矩阵 O(logn)
3. 根据矩阵点数大小 random int，再转化为点 O(logm) -- m is number of points in a rectangle

Follow up:
如果有重叠的怎么办？
类似:
https://leetcode.com/problems/rectangle-area-ii/
#TODO

Corner cases:
"""


from random import randint
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.cnt_rects = len(rects)
        self.pts_sum = [0] * self.cnt_rects
        for i in range(self.cnt_rects):
            if i == 0:
                self.pts_sum[i] = self._get_cnt(rects[i])
            else:
                self.pts_sum[i] = self._get_cnt(rects[i]) + self.pts_sum[i - 1]
        self.ttl_weight = self.pts_sum[-1]

    def pick(self) -> List[int]:
        rand = randint(1, self.ttl_weight)
        rect_idx = bisect.bisect_left(self.pts_sum, rand)
        pt = self._get_random_pt(self.rects[rect_idx])
        return pt

    def _get_cnt(self, rect):
        x = abs(rect[0] - rect[2])
        y = abs(rect[1] - rect[3])
        return (x + 1) * (y + 1)

    def _get_random_pt(self, rect):
        cnt = self._get_cnt(rect)
        rand_target = randint(0, cnt - 1)
        row_cnt = abs(rect[0] - rect[2]) + 1
        col_cnt = abs(rect[1] - rect[3]) + 1
        x = rand_target // col_cnt
        y = rand_target % col_cnt
        return [min(rect[0], rect[2]) + x, min(rect[1], rect[3]) + y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
