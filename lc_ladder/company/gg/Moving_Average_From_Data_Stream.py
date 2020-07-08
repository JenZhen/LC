#! /usr/local/bin/python3

# https://leetcode.com/problems/moving-average-from-data-stream/
# Example
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
"""
Algo: circualr queue
D.S.:

Solution:
1. Using deque
2. Using fix length array as ring
Time: O(1)
Space: O(size of queue)

Corner cases:
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque([])
        self.size = size
        self.ttl = 0

    def next(self, val: int) -> float:
        self.ttl += val
        self.q.append(val)
        if len(self.q) > self.size:
            self.ttl -= self.q[0]
            self.q.popleft()
        return self.ttl / (len(self.q) * 1.0)

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.arr = [0] * size
        self.ttl = 0
        self.i = 0
        self.cnt = 0

    def next(self, val: int) -> float:
        self.ttl += val
        self.ttl -= self.arr[self.i]
        self.arr[self.i] = val
        self.i = (self.i + 1) % self.size
        self.cnt += 1
        if self.cnt < self.size:
            return self.ttl / (self.cnt * 1.0)
        else:
            return self.ttl / (self.size * 1.0)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
