#! /usr/local/bin/python3

# https://www.lintcode.com/problem/zigzag-iterator-ii/description
# Example
# 给你两个一维向量，实现一个迭代器，交替返回两个向量的元素
#
# 样例
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# [1, 3, 2, 4, 5, 6]

"""
Algo:
D.S.: Iteator, queue

Solution:
Time: O(n) -- each element visited once
Space: O(n) for queue

in next()
- directly get the next value
- move element to next position
in has()
- check if current element/position valid, if not, move to next possible position
Corner cases:
empty vector len(v) == 0
and invalid vector, cannot do len(v)

Corner cases:
"""

from collections import deque
class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.Q = deque([deque(v) for v in (v1, v2) if v])
    """
    @return: An integer
    """
    def next(self):
        # write your code here
        curlist = self.Q.popleft()
        res = curlist.popleft()
        if len(curlist) > 0:
            self.Q.append(curlist)
        return res

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.Q) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

# Test Cases
if __name__ == "__main__":
    solution = Solution()
