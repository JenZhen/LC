#! /usr/local/bin/python3

# Requirement
# Given an array of integers and a window of size k.
# Return sliding window average.
# Window size is no bigger than the array length

# Example

"""
Algo:
D.S.:

Solution:
Time: (n)
Space: (k)


Corner cases:
"""

def sliding_window_average(arr, k):
    window = [None for _ in range(k)]
    i = 0
    res = []
    ttl = 0
    for ele in arr:
        if window[i] is not None:
            ttl -= window[i]
        ttl += ele

        window[i] = ele
        i = (i + 1) % k
        if window[i] is not None:
            res.append(ttl // k)
    return res

# Test Cases
if __name__ == "__main__":
    testcases = [
        {
            'arr': [1, -3, -1, -3, 5, 3, 6, 7],
            'k': 3
        }
    ]
    for t in testcases:
        arr = t['arr']
        k = t['k']
        print(sliding_window_average(arr, k))
