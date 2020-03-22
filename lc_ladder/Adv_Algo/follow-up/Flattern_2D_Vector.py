#! /usr/local/bin/python3

# https://www.lintcode.com/problem/flatten-2d-vector/description
# Example
# 设计一个迭代器来实现摊平二维向量的功能
#
# 样例
# 给一个二维向量
#
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# 通过重复调用，直到hasNext返回false，下一个返回的元素的顺序应该是：[1,2,3,4,5,6]。
"""
Algo:
D.S.: Iterator， queue

Solution:
1. Time: O(n), space: O(1)
2. Time: O(n), space: O(n)

key points:
1) 根据题意 # while i.hasNext(): v.append(i.next())
# This operation means, no need to check hasNext within next()
在call next()之前都会把新的位置准备好，所以在next不用验证是否有next， 而是直接访问next

Corner cases:
"""

class Vector2D1(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col = 0, 0
        self.vec = vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.col += 1 # increment after increase
        return self.vec[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0

        return self.row < len(self.vec)


from collections import deque
class Vector2D2(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.q = deque([])
        self.Q = deque([])
        # prepare Q as list of list int
        for li in vec2d:
            self.Q.append(li)

    # @return {int} a next element
    def next(self):
        # Write your code here
        return self.q.popleft()

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while len(self.q) == 0 and len(self.Q):
            li = self.Q.popleft()
            if len(li) > 0:
                for ele in li:
                    self.q.append(ele)
        return len(self.q) > 0


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
# This operation means, no need to check hasNext within next()
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
# This operation means, no need to check hasNext within next()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
