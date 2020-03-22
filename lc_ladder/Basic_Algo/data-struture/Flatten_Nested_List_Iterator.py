#!/usr/bin/python

# http://lintcode.com/en/problem/flatten-nested-list-iterator/
# Example

"""
Algo: DFS
D.S.: Stack

Solution:
This is similar to NestedListWeightSum.
However, next() and hasNext() command require stop in the middle of the process.
Hence using stack to implement a iteration process is more proper.

Corner cases:
- Not sure exactly how this program executed. The best way to do is
    - check if next ready or not and get next element ready in hasNext() function
    - only do return data in next() function
- be aware of cases
    - multiple nested levels
    - [[], []] should return [] (no element out)
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        if len(nestedList) > 0:
            # loop thru reversely (start(included), end(not included), step)
            for i in range(len(nestedList) - 1, -1, -1):
                self.stack.append(nestedList[i])

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            if self.stack[-1].isInteger(): # in python stack has no top() function using stack[-1]
                return True
            else:
                nestedList = self.stack.pop().getList()
                #if len(nestedList) == 0: # is for checking a nested empty list []
                    #continue
                for i in range(len(nestedList) - 1, -1, -1):
                    self.stack.append(nestedList[i])
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Test Cases
if __name__ == "__main__":
    solution = Solution()
