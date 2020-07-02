#! /usr/local/bin/python3

# https://leetcode.com/problems/valid-square/submissions/
# Example
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#
# Note:
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.
"""
Algo:
D.S.:

Solution:


Corner cases:
[[0,0],[0,0],[0,0],[0,0]]
[[2,1],[1,2],[0,0],[2,0]] -> 需要查四个边都一样长
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set([(p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1]), (p4[0], p4[1])])) != 4:
            return False
        ll = [p1, p2, p3, p4]
        ll.sort(key=lambda x: (x[0], x[1])) # sort on x then y
        p1 = ll[0]
        p2 = ll[1]
        p3 = ll[2]
        p4 = ll[3]

        def get_dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        # four edges of same length, 注意顺序，P1 P2 P4 P3
        # inner product is 0 -> perpendicular
        # distance same dist(p2 to p3) == dist(p1 to p4)
        if (p1[0] - p4[0]) * (p2[0] - p3[0]) + (p1[1] - p4[1]) * (p2[1] - p3[1]) == 0 and \
            get_dist(p1, p4) == get_dist(p2, p3) and \
            get_dist(p1, p2) == get_dist(p2, p4) == get_dist(p3, p4) == get_dist(p3, p1):
            return True
        else:
            return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
