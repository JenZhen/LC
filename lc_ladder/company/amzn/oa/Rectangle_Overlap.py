#! /usr/local/bin/python3

# https://www.lintcode.com/problem/rectangle-overlap/description?_from=ladder&&fromId=59
# Example
# 给定两个矩形，判断这两个矩形是否有重叠。
#
# 样例
# 给定 l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], 返回 true
#
# 给定 l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], 返回 false
#
# 注意事项
# l1代表第一个矩形的左上角
# r1代表第一个矩形的右下角
# l2代表第二个矩形的左上角
# r2代表第二个矩形的右下角
#
# 保证：l1 != r2 并且 l2 != r2

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        # corner cases
        if not l1 or not r1 or not l2 or not r2:
            return False
        x1 = [l1.x, r1.x]
        y1 = [r1.y, l1.y]
        x2 = [l2.x, r2.x]
        y2 = [r2.y, l2.y]

        def hasOverlap(itv1, itv2):
            if itv1[0] > itv2[1] or itv2[0] > itv1[1]:
                return False
            else:
                return True
        if hasOverlap(x1, x2) and hasOverlap(y1, y2):
            return True
        else:
            return False
            
# Test Cases
if __name__ == "__main__":
    solution = Solution()
