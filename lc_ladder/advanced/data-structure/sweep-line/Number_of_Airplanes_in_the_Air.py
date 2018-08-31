#! /usr/local/bin/python3

# https://lintcode.com/problem/number-of-airplanes-in-the-sky/description
# Example
# [
#   (1,10),
#   (2,3),
#   (5,8),
#   (4,7)
# ]
# Return 3

"""
Algo:
D.S.: Sweep Line

Solution:
Sweep line classic problem
Time: O(nlogn) -- for sorting

Corner cases:
IMPORTANT: when at a time point, there are both ups and downs, need to consider downs as well
Therefore, we need to sort the secondary making donws before ups.

Python3 sorted function lambda for sorting rules
# TODO:

"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        timestampList = []
        for plane in airplanes:
            timestampList.append((plane.start, True))
            timestampList.append((plane.end, False))
        timestampList = sorted(timestampList, key=lambda x: (x[0], x[1]))
        print("list: %s" %repr(timestampList))
        res = 0
        onAir = 0
        for timestamp in timestampList:
            if timestamp[1]:
                onAir += 1
                print("At %s there are %s" %(timestamp[0], onAir))
                res = max(res, onAir)
            else:
                onAir -= 1
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
