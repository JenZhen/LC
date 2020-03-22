#!/usr/bin/python

# http://lintcode.com/en/problem/3sum-ii/
# Example
# Given n, find the number of solutions for all x, y, z that conforms to x^2+y^2+z^2 = n.(x, y, z are non-negative integers)
# Given n = 0, return 1.

# Explanation:
# When x = 0, y = 0, z = 0, the equation holds.
"""
Algo: 3Sum, two pointers
D.S.:

Solution:
Construct the data structure as 3 sum.
Since looking for x^2 + y^2 + z^2 = n, construct structure as
[x^2,x^2,x^2,y^2,y^2,y^2,z^2,z^2,z^2], each value appears 3 times and less than n

Time: O(n^2) same as 3Sum, need to prepare the origingal in put array nums for O(n)
Space: O(n) nums

Corner cases:
"""

class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    def threeSum2(self, n):
        # Write your code here
        if n < 0:
            return 0
        nums = []
        cnt = 0
        # NOTE: (important)
        # Tricky that range is (n + 1), make sure to include n, such as 0^2 = 0
        # Do not use math way, which is error-prone
        #import math
        #for i in range(int(math.ceil((n/3) ** 0.5)) + 1):
        for i in range(n + 1):
            if i ** 2 > n:
                break
            nums.append(i ** 2)
            nums.append(i ** 2)
            nums.append(i ** 2)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ttl = nums[i] + nums[l] + nums[r]
                if ttl == n:
                    cnt += 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif ttl < n:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return cnt

# Test Cases
if __name__ == "__main__":
    solution = Solution()
