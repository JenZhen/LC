#!/usr/bin/python

# http://www.jiuzhang.com/solution/flatten-2d-vector/
# For example,
# Given 2d vector =
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

"""
Algo: Iterator
D.S.:

Solution:
hasNext() method 只返回是否有下个数，不做找到下一个数的逻辑。否则每次调用都会找到下一个数
next() method 返回下个数，并将iterator挪到下一个数的位置
Corner cases:
"""

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.x = 0
        self.y = 0

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            curVal = self.vec2d[x][y]
            y += 1
            return curVal
        else:
            print ("No next element")

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.y == len(self.vec2d[x]):
            self.x += 1
            self.y = 0
        return self.x < len(vec2d)

# Test Cases
if __name__ == "__main__":
