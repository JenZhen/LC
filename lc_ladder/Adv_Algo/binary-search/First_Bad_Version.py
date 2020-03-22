#! /usr/local/bin/python3

# https://www.lintcode.com/problem/first-bad-version/description
# Same as /lc_ladder/binary-search/First_Bad_Version.py
# Example
# Given n = 5
# isBadVersion(3) -> false
# isBadVersion(5) -> true
# isBadVersion(4) -> true
# Here we are 100% sure that the 4th version is the first bad version.

"""
Algo:
D.S.: Binary Search

Solution:
特征: 找第一个版本

Corner cases:
"""
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""

class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        l，r = 1, n
        while l + 1 < r:
            mid = (l + r) // 2
            if SVNRepo.isBadVersion(mid):
                r = mid
            else:
                l = mid
        if SVNRepo.isBadVersion(l):
            return l
        else:
            return r

# Test Cases
if __name__ == "__main__":
    s = Solution()
