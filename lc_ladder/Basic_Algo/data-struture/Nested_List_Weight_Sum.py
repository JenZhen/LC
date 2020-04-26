#!/usr/bin/python

# http://www.jiuzhang.com/solution/nested-list-weight-sum/
# Example
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1.
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""
Algo: queue/stack
D.S.: iteration/recursion

Solution:
Similar to Tree, BFS, iteration with queue/stack and recursion methods
Solution1:
递归： DFS

Solution2:
queue/stack: BFS
Corner cases:
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class Solution1(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        # Recursion version 1
        return self.helper(nestedList, 1)

    def helper(self, list, degree):
        sum = 0
        for l in list:
            if l.isInteger():
                sum += l.getInteger() * degree
            else:
                sum += self.helper(l.getList(), degree + 1)
        return sum

class Solution2(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    # Recursion version2
    def __init__(self):
        self.sum = 0
        self.depth = 1

    def depthSum(self, nestedList):
        # Write your code here
        for l in nestedList:
            if l.isInteger():
                self.sum += l.getInteger() * self.depth
            else:
                self.depth += 1
                self.sum += self.depthSum(l.getList())
        return self.sum

class Solution3(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        # Iteration
        if len(nestedList) == 0:
            return 0
        sum = 0
        # in this question, order doesn't matter,
        # can use both stack or queue
        stack = [] # stack is a usage of list in python
        for l in nestedList:
            stack.append(l, 1)
        while not stack.empty():
            item, depth = stack.pop()
            if item.isInteger():
                sum += item.getInteger() * depth
            else:
                for l in item.getList():
                    stack.append(l, depth + 1)
        return sum


# Test Cases
if __name__ == "__main__":
    solution = Solution()
