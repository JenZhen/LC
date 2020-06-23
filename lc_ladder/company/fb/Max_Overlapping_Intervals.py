#! /usr/local/bin/python3

# Requirement
# Example
# Given number M and N intervals in the form [a, b] (inclusive) where for every interval -M <= a <= b <= M,
# create a program that returns a point where the maximum number of intervals overlap.
#
# Example:
#
# M: 10
# N: 4
# Intervals:
# [-3, 5]
# [0, 2]
# [8, 10]
# [6, 7]
# A correct answer would be either 0 ,1 or 2 since those points are found where 2 intervals overlap and 2 is the maximum number of overlapping intervals.

"""
Algo:
D.S.:

Solution:

Time: O(M + N)
Space: O(M)
Corner cases:
"""

def maxOverlappingPoint(M, intervals):
    l = [0] * (2 * M + 2) # [-M, M + 1]
    for s, e in intervals:
        l[s + M] += 1
        l[e + M + 1] -= 1 # convert to [ )
    # print(l)
    max_overlap = 0
    res = []
    runner = 0
    for i in range(len(l)):
        runner += l[i]
        if runner == max_overlap:
            res.append(i - M)
        elif runner > max_overlap:
            max_overlap = runner
            res = []
            res.append(i - M)
    return res


# Test Cases
if __name__ == "__main__":
    testcases = [
        {
            'M': 10,
            'intervals': [
                [-3, 5],
                [0, 2],
                [8, 10],
                [6, 7]
            ]
        }
    ]
    for t in testcases:
        M = t['M']
        intervals = t['intervals']
        res1 = maxOverlappingPoint(M, intervals)
        print(res1)
