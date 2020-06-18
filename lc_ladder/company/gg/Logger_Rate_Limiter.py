#! /usr/local/bin/python3

# https://leetcode.com/problems/logger-rate-limiter/submissions/
# Example
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
# It is possible that several messages arrive roughly at the same time.
#
# Example:
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;

"""
Algo: map
D.S.:

Solution:
map: # key: message, val: prev_ts
Time: O(1)
Time: O(n) -- n is count of different messages

Corner cases:
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {} # key: message, val: prev_ts

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.mp:
            self.mp[message] = timestamp
            return True
        else:
            prev_ts = self.mp[message]
            if timestamp - prev_ts >= 10:
                self.mp[message] = timestamp
                return True
            else:
                return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
