#! /usr/local/bin/python3

# https://leetcode.com/problems/my-calendar-i/submissions/
# Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
# Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
#
# A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.
#
#
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
Algo:
D.S.:

Solution:

两个interval是否有交集的判断条件
start < e and end > s:

Solution1：suggested
balanced tree (ideally)
for python 没有treemap -- ordered hashmap
average: O(nlogn) worst case: O(n^2) when biased tree

for java use treemap structure O(nlogn)

Space: O(N)
Solution2：
暴力解法，每次添加一个新的interval 都要去和之前加进去的每一个比较
Time：O(n^2)
Space: O(n)

Corner cases:
"""
class MyCalendar:

    def __init__(self):
        self.tree = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.tree.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True

        cur = self.root
        pre = None
        while cur:
            if end <= cur.start:
                pre = cur
                cur = cur.left
            elif start >= cur.end:
                pre = cur
                cur = cur.right
            elif start < cur.end and end > cur.start:
                return False
        if end <= pre.start:
            pre.left = Node(start, end)
        elif start >= pre.end:
            pre.right = Node(start, end)
        return True

class MyCalendar_Brutal_Force:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and end > s:
                return False
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
