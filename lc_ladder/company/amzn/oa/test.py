#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

li = [0, 3, 2, 1]
sort(li, 0, len(li) - 1, 2)

def sort(li, l, r, k):
    if l >= r:
        return
    pos = 1
    if pos == k:
        return
    elif pos < k:
        return sort(li, pos + 1, r, k)
    else:
        return sort(li, l, pos - 1, k)
