#! /usr/local/bin/python3

# https://www.lintcode.com/problem/my-calendar-i/description
# Example
# 实现MyCalendar类来存储您的活动。 如果新添加的活动没有重复，则可以添加。
#
# 你的类将有方法book(int start，int end)。 这代表左闭右开的间隔[start，end)有了预定，范围内的实数x，都满足start <= x < end。
#
# 当两个事件有一些非空交集时（即，两个事件在共同的时间都有预定），就会发生重复预订。
#
# 每次调用MyCalendar.book方法时，如果没有发生重复预定，那么事件可以成功添加到日历，且返回true。 否则，返回false，并且事件不会添加到日历中。
#
# 你的类以此方式被调用：MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end);
#
# 样例
# MyCalendar();
# MyCalendar.book(10, 20); // 返回true
# MyCalendar.book(15, 25); // 返回false
# MyCalendar.book(20, 30); // 返回true
# 解释:
# 第一个事件可以预定。 第二个不行，因为15已经被预定。
# 第三个事件可以预定，因为第一个事件预定了20以前的时间，但不包括20.
# 注意事项
# 每个测试样例调用 MyCalendar.book 的次数最多为 1000。
# 调用MyCalendar.book(start, end)时, start 和 end 都是 [0, 10^9]范围内的整数。

"""
Algo:
D.S.: list
Solution:
1. 需要遍历现所有schedule来判断是否有没有重复
O(N): 对于每一次查询，O(N^2) 对于所有N次查询
2. 扫描线法（要求排序） 先将区间放入已有区间，然后扫描线看有没有重复的，有的话就将它再删除
扫面线需要排序的特点要求

Corner cases:
"""

class MyCalendar:

    def __init__(self):
        # (st, end) save tuple of event start and end
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.calendar:
            self.calendar.append((start, end))
            return True
        for cal in self.calendar:
            if not (end <= cal[0] or cal[1] <= start):
                return False
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
