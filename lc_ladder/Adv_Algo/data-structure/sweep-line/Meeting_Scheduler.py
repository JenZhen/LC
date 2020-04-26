#! /usr/local/bin/python3

# https://leetcode.com/problems/meeting-scheduler/
# Example
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is,
# for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
#
# Example 1:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
#
# Constraints:
#
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6

"""
Algo:
D.S.:

Solution1:
在slots1, slots2很多的情况下超时 -- 比较太多

Solution2:
优化比较

注意要先排序

Corner cases:
"""
class Solution_Faster:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            # slot1 is greater than slot2
            if slots1[p1][0] >= slots2[p2][1] or \
                slots2[p2][1] - slots1[p1][0] < duration:
                p2 += 1
            # slot2 is greater than slot1
            elif slots2[p2][0] >= slots1[p1][1] or \
                slots1[p1][1] - slots2[p2][0] < duration:
                p1 += 1
            elif (min(slots1[p1][1], slots2[p2][1]) - max(slots1[p1][0], slots2[p2][0]) >= duration):
                return [max(slots1[p1][0], slots2[p2][0]), max(slots1[p1][0], slots2[p2][0]) + duration]
            else:
                # TODO: 不清楚这个情况什么时候出现
                p1 += 1
                p2 += 1
        return []

    def get_overlap(self, itv1, itv2):
        print("p1, p2", itv1, itv2)
        res = []
        st = max(itv1[0], itv2[0])
        end = min(itv1[1], itv2[1])
        if st >= end:
            return None
        else:
            return [st, end]

class Solution_Fast:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            st = max(slots1[p1][0], slots2[p2][0])
            end = min(slots1[p1][1], slots2[p2][1])

            if st < end:
                if st + duration <= end:
                    return [st, st + duration]
                if slots1[p1][1] < slots2[p2][1]:
                    p1 += 1
                else:
                    p2 += 1
            else:
                if slots1[p1][1] < slots2[p2][1]:
                    p1 += 1
                else:
                    p2 += 1
        return []


class Solution1_TLE:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        p1, p2 = 0, 0
        res = []
        while p1 < len(slots1) and p2 < len(slots2):
            overlap = self.get_overlap(slots1[p1], slots2[p2])
            if overlap != None and overlap[1] - overlap[0] >= duration:
                return [overlap[0], overlap[0] + duration]

            # if not found, need to decide to move p1 or p2
            if slots1[p1][1] <= slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1

    def get_overlap(self, itv1, itv2):
        res = []
        st = max(itv1[0], itv2[0])
        end = min(itv1[1], itv2[1])
        if st >= end:
            return None
        else:
            return [st, end]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
