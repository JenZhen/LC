#! /usr/local/bin/python3

# https://lintcode.com/en/problem/minimum-size-subarray-sum/
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.
# Example
# Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

"""
Algo: 2-pointers same direction
D.S.:

Solution:
2-pointers how to improve from O(n^2) to O(n)
This is template question.

i = 0: j = 0, no; j = 1, no; j = 2, no; j = 3, yes
i = 1             j = 1, no, j = 2, no; j = 3, need to calculate
    when j = 1, 2 is for sure a no.
    hence j can stay at 3 and only move forward.
** If in a nested loop, we can make iterator only goes forward, performance can be improved.

##########
# Template
##########
for (i = 0; i < length; i++) {
    while (j < length) {
        if (meetsRequirement) {
            j++;
            update j
        } else{
            break;
        }
    }
    update i
}
Corner cases:
- if >=s not found

"""

class Solution1:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        import sys
        if nums is None or len(nums) == 0:
            return -1

        length = len(nums)
        ans = sys.maxsize
        for i in range(length):
            sum = 0
            for j in range(i, length):
                sum += nums[j]
                if sum >= s:
                    ans = min(ans, j - i + 1)
                    break
        if ans == sys.maxsize:
            return -1
        return ans



class Solution2:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        import sys

        if nums is None or len(nums) == 0:
            return -1

        length = len(nums)
        i, j, sum = 0, 0, 0
        ans = sys.maxsize

        for i in range(length):
            while j < length and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                print("sum: %s, dist: %s" %(sum, j - i))
                ans = min(ans, j - i)
            sum -= nums[i]
        if ans == sys.maxsize:
            return -1
        return ans

if __name__ == "__main__":
    testCases = [
        {
            "nums": [2,3,1,2,4,3],
            "s": 7
        }
    ]
    s1 = Solution1()
    s2 = Solution2()
    for t in testCases:
        nums = t["nums"]
        s = t["s"]
        res1 = s1.minimumSize(nums, s)
        res2 = s2.minimumSize(nums, s)
        print("res1: %s" %(res1))
        print("res2: %s" %(res2))
