#! /usr/local/bin/python3

# Requirement
# Example
# You are given a list of strings. Removing a letter from any string yields a different string
# that may or may not exist in the list as an independent entity.
# This is one link of a "string chain". Find the longest chain in the array.

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

def longest_string_chain(dict):
    map = _populateMap(dict)
    # print(map)
    visited = set()
    strings = sorted(list(dict), key=lambda str: len(str), reverse=True)
    maxDist = 0
    for str in strings:
        if str not in visited:
            dist = bfs(str, dict, map, visited)
            maxDist = max(maxDist, dist)
            # print("start with: %s, dist: %s." %(str, dist))
    return maxDist

def _populateMap(dict):
    map = {}
    for str in dict:
        map[str] = []
        for i in range(len(str)):
            new_str = str[:i] + str[i + 1:]
            if new_str in dict:
                map[str].append(new_str)
    return map

def bfs(start_str, dict, map, visited):
    from collections import deque
    q = deque([start_str])
    visited.add(start_str)
    depth = 0
    while q:
        cur_str = q.popleft()
        next_strs = map[cur_str]
        if len(next_strs):
            depth += 1
        for str in next_strs:
            if str not in visited:
                visited.add(str)
                q.append(str)
    return depth

# Test Cases
if __name__ == "__main__":
    testcases = [
        {
            "abcde",
            "abcdf",
            "abce",
            "abcd",
            "abe",
            "be",
            "ab",
            "a"
        },
    ]

    for t in testcases:
        dict = set(t)
        print(longest_string_chain(dict))
