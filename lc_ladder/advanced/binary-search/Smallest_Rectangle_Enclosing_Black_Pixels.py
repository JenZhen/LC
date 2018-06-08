#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: Binary Search
D.S.:

Solution:
Time: O(nlogn)

Corner cases:
"""

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return 0
        m = len(image)
        n = len(image[0])

        left = self.findleft(image, 0, y)
        right = self.findright(image, y, n - 1)
        up = self.findup(image, 0, x)
        down = self.finddown(image, x, m - 1)
        print("%s, %s, %s, %s" %(left, right, up, down))

        return (right - left + 1) * (down - up + 1)

    def findleft(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.isEmptyCol(image, mid):
                l = mid
            else:
                r = mid
        if self.isEmptyCol(image, l):
            return r
        else:
            return l

    def findright(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.isEmptyCol(image, mid):
                r = mid
            else:
                l = mid
        if self.isEmptyCol(image, r):
            return l
        else:
            return r

    def findup(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.isEmptyRow(image, mid):
                l = mid
            else:
                r = mid
        if self.isEmptyRow(image, l):
            return r
        else:
            return l

    def finddown(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.isEmptyRow(image, mid):
                r = mid
            else:
                l = mid
        if self.isEmptyRow(image, r):
            return l
        else:
            return r

    def isEmptyRow(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return False
        return True
    def isEmptyCol(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True

# Test Cases
if __name__ == "__main__":
    s = Solution()
