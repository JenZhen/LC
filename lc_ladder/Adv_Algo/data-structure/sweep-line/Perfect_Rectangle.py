#! /usr/local/bin/python3

# https://leetcode.com/problems/perfect-rectangle/
# Example
# Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
#
# Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2].
# (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
#
# Example 1:
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
# Return true. All 5 rectangles together form an exact cover of a rectangular region.
#
# Example 2:
# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
# Return false. Because there is a gap between the two rectangular regions.
#
# Example 3:
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
# Return false. Because there is a gap in the top center.
#
# Example 4:
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# Return false. Because two of the rectangles overlap with each other.
"""
Algo:
D.S.:

Solution1:
数CORNER
每个矩形的四个点取出来
- 每个点可以出现偶数次，或是只有一次。最后只能剩下4个只出现1次的点，这个就是最后大矩阵的四个点
- 每个小矩阵面积和应该等于最后大矩阵的面积

Solution2:
# TODO: Sweeping line

Corner cases:
"""

class Solution2:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area_sum = 0
        coor_set = set()
        for rec in rectangles:
            p1 = (rec[0], rec[1]) # bottom left
            p2 = (rec[0], rec[3]) # top left
            p3 = (rec[2], rec[3]) # top right
            p4 = (rec[2], rec[1]) # bottom right

            for p in [p1, p2, p3, p4]:
                if p not in coor_set:
                    coor_set.add(p)
                else:
                    coor_set.remove(p)
            area_sum += ((rec[2] - rec[0]) * (rec[3] - rec[1]))

        # only 4 corner left
        if len(coor_set) != 4:
            return False

        return self.get_area(coor_set) == area_sum

    def get_area(self, coor_set):
        p1 = coor_set.pop()
        p2 = coor_set.pop()
        p3 = coor_set.pop()
        return (max(abs(p1[0] - p2[0]), abs(p2[0] - p3[0])) *
                max(abs(p1[1] - p2[1]), abs(p2[1] - p3[1])))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
