#! /usr/local/bin/python3

# https://leetcode.com/problems/interval-list-intersections/
# Example
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
#
# Note:
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
Algo:
D.S.:

Solution1:
merge on the fly -- better
Time: O(m + n)
Space: O(1)

Solution2:
sort timestamp
Time: O(nlogn) where n = # of timestamp in two array
Space: O(n)
Corner cases:
"""
class Solution1:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


class Solution2:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        ts_list = []
        for s, e in A:
            ts_list.append((s, 0))
            ts_list.append((e, 1))
        for s, e in B:
            ts_list.append((s, 0))
            ts_list.append((e, 1))

        ts_list.sort()
        cnt = 0
        tmp = []
        for item in ts_list:
            ts, ts_type = item[0], item[1]
            if ts_type == 0:
                cnt += 1
                if cnt == 2:
                    tmp.append(ts)
            elif ts_type == 1:
                cnt -= 1
                if cnt == 1:
                    tmp.append(ts)
                    res.append(tmp[:])
                    tmp = []
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
