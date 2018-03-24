#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-data-structure-design/
# Example
# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
"""
Algo:
D.S.:

Solution:

Time: add O(1), find O(n)
Space: O(n)

Corner cases:
"""

class TwoSum(object):
    def __init__(self):
        # initialize your data structure here
        self.count = {}

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        if not value:
            return False
        # note that {} iteration and dict iteration difference
        for num in self.count:
            other = value - num
            if other in self.count and \
                (self.count[other] > 1 or other != num):
                # for testing purpse
                self.printResult(value, True)
                return True
        self.printResult(value, False)
        return False

    def printResult(self, value, res):
        print("Find %d: %s" %(value, res))

# Test Cases
if __name__ == "__main__":
    tw = TwoSum()
    tw.add(1)
    tw.add(1)
    tw.add(2)
    tw.find(3)
    tw.find(4)
