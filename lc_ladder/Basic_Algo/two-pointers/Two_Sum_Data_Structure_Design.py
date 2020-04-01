#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-data-structure-design/
# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Example
# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
"""
Algo:
D.S.:

Solution1:

Time: add O(1), find O(n)
Space: O(n)

Solution2:
Add: O(1) add to dictionary, O(n) add to sum set
Find: O(1)
Cannot pass Time Limit Exceeded.

Corner cases:
"""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq_map = {} # key: num, val: freq


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.freq_map:
            self.freq_map[number] = 1
        else:
            self.freq_map[number] += 1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # note that {} iteration and dict iteration difference
        for num in self.freq_map:
            other = value - num
            if other in self.freq_map:
                if self.freq_map[other] > 1:
                    return True
                if num != other:
                    return True
        return False


class TwoSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq_map = {} # key: num, val: freq
        self.sum_set = set()


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        for key in self.freq_map:
            self.sum_set.add(key + number)
        if number not in self.freq_map:
            self.freq_map[number] = 1
        else:
            self.freq_map[number] += 1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.sum_set
# Test Cases
if __name__ == "__main__":
    tw = TwoSum()
    tw.add(1)
    tw.add(1)
    tw.add(2)
    tw.find(3)
    tw.find(4)
