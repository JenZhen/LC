#! /usr/local/bin/python3

# Requirement
Array size of n with value from 0, to n - 1
return the first duplicate element

# Example

"""
Algo:
D.S.:

Solution:
Time: (n)
Space: (1)


Corner cases:
"""

def find_first_duplicate_element(arr):
    n = len(arr)
    for i in range(n):
        val = abs(arr[i])
        if arr[val] < 0:
            return val
        else:
            arr[val] *= (-1)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
