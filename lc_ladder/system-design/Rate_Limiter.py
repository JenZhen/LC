#!/usr/local/bin/python3

# https://www.lintcode.com/problem/rate-limiter/description?_from=ladder&&fromId=8
# Example
# mplement a rate limiter, provide one method: is_ratelimited(timestamp, event, rate, increment).
#
# timestamp: The current timestamp, which is an integer and in second unit.
# event: The string to distinct different event. for example, "login" or "signup".
# rate: The rate of the limit. 1/s (1 time per second), 2/m (2 times per minute), 10/h (10 times per hour), 100/d (100 times per day). The format is [integer]/[s/m/h/d].
# increment: Whether we should increase the counter. (or take this call as a hit of the given event)
# The method should return true or false to indicate the event is limited or not.
#
# 样例
# is_ratelimited(1, "login", "3/m", true), return false.
# is_ratelimited(11, "login", "3/m", true), return false.
# is_ratelimited(21, "login", "3/m", true), return false.
# is_ratelimited(30, "login", "3/m", true), return true.
# is_ratelimited(65, "login", "3/m", true), return false.
# is_ratelimited(300, "login", "3/m", true), return false.
# 挑战
# How many different algorithms you can come up with?

"""
Solution:

Corner cases:
"""

class Solution:
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def __init__(self):
        # key: event, val: list of timestamps
        self.mp = {}
    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        start = rate.find("/")
        # total_time denotes a time interval
        total_time = int(rate[:start])
        type = rate[start+1:]

        time = 1
        if type == 'm':
            time *= 60
        elif type == 'h':
            time = time * 60 * 60
        elif type == 'd':
            time = time * 60 * 60 * 24
        # from current timestamp back time interval
        last_time = timestamp - time + 1

        if event not in self.mp:
            self.mp[event] = []

        rt = self.find_event(self.mp[event], last_time) >= total_time
        if increment and not rt:
            self.insert_event(self.mp[event], timestamp)

        return rt

    def insert_event(self, event, timestamp):
        event.append(timestamp)

    def find_event(self, event, last_time):
        l, r = 0, len(event) - 1
        if r < 0 or event[r] < last_time:
            return 0

        ans = 0
        while l + 1 < r:
            mid = l + (r - l) // 2
            if event[mid] >= last_time:
                ans = mid
                r = mid
            else:
                l = mid
        if event[l] >= last_time:
            ans = l
        else:
            ans = r
        return len(event) - ans

        # Another binary search flow
        # while l <= r:
        #     mid = (l + r) >> 1
        #     if event[mid] >= last_time:
        #         ans = mid
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return len(event) - 1 - ans + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
