#!/usr/bin/python

# http://www.jiuzhang.com/solution/zigzag-iterator-ii/
# Example

"""
Algo:
D.S.:

Solution:
Same solution as ZigZagIterator, but to prepre a queue of all those K vectors

Corner cases:
"""

class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.queue = [v for v in vecs if v]

    def next(self):
        # Write your code here
        v = self.queue.pop(0)
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value

    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result

# Test Cases
if __name__ == "__main__":
    solution = Solution()
