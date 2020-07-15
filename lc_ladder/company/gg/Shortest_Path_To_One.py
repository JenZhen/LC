#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

def shortest_path_to_one(N):
    if N <= 1:
        return 0

    f = [N + 1 for _ in range(N + 1)]
    f[0] = 0
    f[1] = 0
    for i in range(2, N + 1):
        f[i] = min(f[i], f[i - 1]) + 1
        if i % 2 == 0:
            f[i] = min(f[i], f[i // 2]) + 1
        if i % 3 == 0:
            f[i] = min(f[i], f[i // 3]) + 1
    return f[-1]

# Test Cases
if __name__ == "__main__":
    testcases = [0, 1, 2, 3, 4, 6, 7, 8, 9]
    for t in testcases:
        print(shortest_path_to_one(t))
