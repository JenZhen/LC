#!/usr/local/bin/python3

# https://www.lintcode.com/problem/web-logger/description?_from=ladder&&fromId=8
# Example
实现下面两个方法：
# 1.hit(timestamp) 建立一个时间戳
# 2.get_hit_count_in_last_5_minutes(timestamp) 得到最后5分钟时间戳个数
#
# 样例
# hit(1);
# hit(2);
# get_hit_count_in_last_5_minutes(3);
# >> 2
# hit(300);
# get_hit_count_in_last_5_minutes(300);
# >> 3
# get_hit_count_in_last_5_minutes(301);
# >> 2
"""
Solution:
注意： 计数条件 while (len(self.timestamps) != 0 and self.timestamps[0] + 300 <= timestamp):
<= 不是 <
Corner cases:
"""

from collections import deque
class WebLogger:

    def __init__(self):
        # do intialization if necessary
        self.timestamps = deque([])

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.timestamps.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        while (len(self.timestamps) != 0 and self.timestamps[0] + 300 <= timestamp):
            self.timestamps.popleft()
        return len(self.timestamps)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
