#! /usr/local/bin/python3

# https://leetcode.com/problems/design-hit-counter/submissions/
# Example
# Design a hit counter which counts the number of hits received in the past 5 minutes.
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that
# calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
# Example:
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);c
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?
"""
Algo:
D.S.:

Solution:
1. linear clean up
2. bianry search clean up
ts = 350, 需要删除ts <= 50
bisect_right 50, pos 右侧都是合法的，左侧都是过期要删除的

Corner cases:
"""

from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque([])

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # hit 经常被call，可以不做clean up 操作，总体效率会提升
        # self._clean_up(timestamp)
        self.q.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._clean_up(timestamp)
        return len(self.q)

    def _clean_up_liner(self, timestamp):
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()

    def _clean_up_binary_search(self, timestamp):
        pos = bisect.bisect_right(self.q, timestamp - 300)
        for i in range(pos):
            self.q.popleft()

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
