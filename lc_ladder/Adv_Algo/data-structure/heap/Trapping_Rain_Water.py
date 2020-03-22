#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/trapping-rain-water/
# Example

"""
Algo:
D.S.: Two-pointers

Solution:
- Needs to narrowing down from 2 ends
- lower one of the 2 ends decides the max height
- 2 points moving towards
Time: O(N)
Corner cases:
"""
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        lHeight = heights[l]
        rHeight = heights[r]
        res = 0
        while l < r:
            if lHeight < rHeight:
                # search left side
                l += 1
                if lHeight > heights[l]:
                    res += (lHeight - heights[l])
                else:
                    lHeight = heights[l]
            else:
                # search right side
                r -= 1
                if rHeight > heights[r]:
                    res += (rHeight - heights[r])
                else:
                    rHeight = heights[r]
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
