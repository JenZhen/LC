#! /usr/local/bin/python3

# https://www.lintcode.com/problem/zigzag-iterator-ii/description
# Example

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
"""

from collections import deque
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.Q = deque([deque(v) for v in vecs if v])

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        curQ = self.Q.popleft()
        res = curQ.popleft()
        if len(curQ):
            self.Q.append(curQ)
        return res

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.Q) > 0


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
# Test Cases
if __name__ == "__main__":
    solution = Solution()
