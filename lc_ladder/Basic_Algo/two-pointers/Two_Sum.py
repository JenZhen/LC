#!/usr/bin/python

# http://lintcode.com/en/problem/two-sum/
# Example

"""
Algo:
D.S.: map for quick lookup if exists?

Solution:
Tricky part, can merge map building loop with check part

Two Sum 问题的通用思路：
1. 可以sort原数组，然后首尾两个指针收缩
2. 如果返回原数组的idx，可以组成(num[i], i) tuple，根据num sort，然后2指针
    或者使用extra space ie map
使用sort time: O(nlogn)
使用map space: O(n)
Time: O(n)
Space: O(n)
Corner cases:
"""

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if len(numbers) == 0 or target is None:
            return None

        map = {}
        for i in range(len(numbers)):
            other = target - numbers[i]
            if other in map:
                return [map[other], i]
            else:
                map[numbers[i]] = i

# Test Cases
if __name__ == "__main__":
    solution = Solution()
