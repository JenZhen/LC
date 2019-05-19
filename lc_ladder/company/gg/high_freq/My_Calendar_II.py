#! /usr/local/bin/python3

# https://leetcode.com/problems/my-calendar-ii/
# Example
# Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.
#
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
#
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
#
#
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

"""
Algo:
D.S.: sweeping line, interval

Solution:
Time: O(n)
Space: O(n)

interval non-merge
这个题目如果要用sweeping Line需要sort端点，端点需要用treemap 结构

case 1: b ends before a ends:
a: a0 |-------------| a1
b:     b0 |-----| b1

case 2: b ends after a ends:
a: a0 |--------| a1
b:     b0 |--------| b1

case 3: b starts after a ends: (negative overlap)
a: a0 |----| a1
b:              b0 |----| b1

Corner cases:
"""

class MyCalendarTwo:

    def __init__(self):
        self.overlap = [] # interval of book overlap, intervals no overlap
        self.books = [] # books interval, may have overlap, no triple overlaps

    def book(self, start: int, end: int) -> bool:
        # iterate through self.overlap to see if valid
        for intv in self.overlap:
            new_start = max(intv[0], start)
            new_end = min(intv[1], end)
            if new_start < new_end:
                return False

        # if valid need to update self.overlap and self.books
        for book in self.books:
            # find all overlap intervals added to self.overlap
            # no need to merge
            # simply append new book interval at the end
            new_start = max(book[0], start)
            new_end = min(book[1], end)
            if new_start < new_end:
                # a valid overlap
                self.overlap.append((new_start, new_end))
        self.books.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


class MyCalendarTwo {

    private TreeMap<Integer, Integer> map;

    public MyCalendarTwo() {
        map = new TreeMap<>(); // key: position, val: cnt, start point +1, end point -1
    }

    public boolean book(int start, int end) {
        map.put(start, map.getOrDefault(start, 0) + 1);
        map.put(end, map.getOrDefault(end, 0) - 1);
        int count = 0;
        // iterate treemap entry, which is a sorted list based on key
        // this is like sorted endpoints like in sweepingline method.
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            count += entry.getValue();
            if(count > 2) {
                map.put(start, map.get(start) - 1);
                if(map.get(start) == 0) {
                    map.remove(start);
                }
                map.put(end, map.get(end) + 1);
                if(map.get(end) == 0) {
                    map.remove(end);
                }
                return false;
            }
        }
        return true;
    }
}
# Test Cases
if __name__ == "__main__":
    solution = Solution()
