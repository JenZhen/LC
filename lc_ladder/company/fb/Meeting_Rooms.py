#! /usr/local/bin/python3

# https://leetcode.com/problems/meeting-rooms/
# Example
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
Algo: Sort
D.S.:

Solution:
Time: O(nlogn) -- 先考虑终点再考虑起点
Space: O(1)

Corner cases:
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or not intervals[0]:
            return True

        ts_list = []
        for [s, e] in intervals:
            ts_list.append((s, 1))
            ts_list.append((e, 0))
        ts_list.sort()
        cnt = 0
        for ts, flag in ts_list:
            if flag == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt > 1:
                return False
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
