#! /usr/local/bin/python3

# https://www.lintcode.com/problem/my-calendar-ii/description?_from=ladder&&fromId=18
# Example
# 实现MyCalendarTwo类来存储您的事件。 如果添加活动不会导致三重预订，则可以添加新活动。
#
# 你的类将有一个方法，book(int start, int end)。 这代表左闭右开的间隔[start, end)有一个预订，范围内的实数x，都满足start <= x < end。
#
# 当三个事件具有一些非空交集时（即，有一个时间同时有三个预定），会发生三重预订。
#
# 每次调用MyCalendar.book时，如果没有三重预定，则事件可以成功添加到日历，且返回true。 否则，返回false，并且事件不会添加到日历中。
#
# 你的类以此方式被调用：MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end);
#
# 样例
# MyCalendar();
# MyCalendar.book(10, 20); // 返回true
# MyCalendar.book(50, 60); // 返回true
# MyCalendar.book(10, 40); // 返回true
# MyCalendar.book(5, 15); // 返回false
# MyCalendar.book(5, 10); // 返回true
# MyCalendar.book(25, 55); //返回true
# 解释:
# 前两个事件可以被预定，第三个时间是一个双重预定。
# 第四个事件(5, 15)不能被预定，因为会导致三重预定。
# 第五个事件 (5, 10)可以被预定，因为它并没有用到已经双重预定的10。
# 第六个事件(25, 55)可以背预定，因为[25, 40)这段时间里有第三个和第六个事件的双重预定，[40, 50)时间段内只有一个预定，[50, 55)时间段内有第二个和第六个事件的双重预定。
# 注意事项
# 每个测试样例调用 MyCalendar.book 的次数最多为 1000。
# 调用MyCalendar.book(start, end)时, start 和 end 都是 [0, 10^9]范围内的整数。

"""
Algo:
D.S.: Sweeping line

Solution:
My calendar I 的解法2，扫描线，需要保证sorted
1. 用list, 很慢，每次添加都要sort
2. 用treemap(带comparator的map, 区别于python ordereddict -- 顺序是写入的顺序) 之类的sortedmap结构(python 没有built-in)

Corner cases:
"""

# Java Treemap Implementation
class MyCalendarTwo {
    TreeMap<Integer, Integer> event2count;
    public MyCalendarTwo() {
        this.event2count =  = new TreeMap<>();
    }

    public boolean book(int start, int end) {
      // 先假设这个event能被放进去
      event2count.put(start, event2count.getOrDefault(start, 0) + 1);
      event2count.put(end, event2count.getOrDefault(end, 0) - 1);

      int count = 0;
      // 扫描线
      for(Map.Entry<Integer, Integer> entry : event2count.entrySet()){
        count += entry.getValue();

        // 放进去发现不符合要求, 拿出来return false
        if(count >= 3){
          event2count.put(start, event2count.get(start) - 1);
          event2count.put(end, event2count.get(end) + 1);
          return false;
        }
      }

      return true;
    }
}

class MyCalendarTwo_1:

    def __init__(self):
        # list of sorted (time, 1 if start, -1 if end) based on time
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # insert tuple first
        self.calendar.append((start, 1))
        self.calendar.append((end, -1))
        self.calendar.sort(key=lambda x: (x[0], x[1]))
        print(self.calendar)

        cnt = 0
        for cal in self.calendar:
            cnt += cal[1]
            if cnt == 3:
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                self.calendar.sort(key=lambda x: (x[0], x[1]))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
