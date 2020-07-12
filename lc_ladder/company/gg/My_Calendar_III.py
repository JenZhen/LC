#! /usr/local/bin/python3

# https://leetcode.com/problems/my-calendar-iii/submissions/
# Example
# Implement a MyCalendarThree class to store your events. A new event can always be added.
#
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)
#
# For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.
#
# Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
# Example 1:
#
# MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3
# Explanation:
# The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
# The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
# The remaining events cause the maximum K-booking to be only a 3-booking.
# Note that the last event locally causes a 2-booking, but the answer is still 3 because
# eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
#
#
# Note:
#
# The number of calls to MyCalendarThree.book per test case will be at most 400.
# In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
"""
Algo:
D.S.: C++ map, Java TreeMap, Python sort

Solution1: AC
Time: O(nlogn) -- for each booking call
Space: O(n) -- mapping, same ts can share the same key
Save more space than solution2

Solution2: 超时
Time: O(nlogn) -- for each booking call
Space: O(n) -- save all interval ts points with their flags

Corner cases:
"""

class MyCalendarThree1:

    def __init__(self):
        self.mp = {} # key: ts, val: cnt +1 or -1

    def book(self, start: int, end: int) -> int:
        if start not in self.mp:
            self.mp[start] = 1
        else:
            self.mp[start] += 1
        if end not in self.mp:
            self.mp[end] = -1
        else:
            self.mp[end] -= 1

        sorted_mp = sorted(self.mp.items(), key=lambda x: x[0]) # sort key
        # print(sorted_mp)
        cur = 0
        res = 0
        for key, val in sorted_mp:
            cur += val
            res = max(res, cur)
        return res


class MyCalendarThree2:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> int:
        self.arr.append((start, end))
        return self._get_max_booking()

    def _get_max_booking(self):
        ll = []
        for s, e in self.arr:
            ll.append((s, 1))
            ll.append((e, 0))
        ll.sort(key=lambda x: (x[0], x[1]))
        # print(ll)
        res = 0
        cnt = 0
        for ts, flag in ll:
            if flag == 1:
                cnt += 1
                res = max(res, cnt)
            elif flag == 0:
                cnt -= 1
        return res



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
