#! /usr/local/bin/python3

# https://leetcode.com/problems/maximize-distance-to-closest-person/
# Example
# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:
#
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
Algo:
D.S.:

Solution:
Time: O(n)
Space: O(1)

Corner cases:
注意Corner在-1 并且查最后的右边界
左边界
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats:
            return None
        l = -1
        maxdist = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                dist = 0
                if l == -1:
                    dist = i
                else:
                    dist = (i - l) // 2
                print(dist)
                maxdist = max(maxdist, dist)
                l = i
        return max(maxdist, len(seats) - 1 - l)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
