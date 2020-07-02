#! /usr/local/bin/python3

# https://leetcode.com/problems/network-delay-time/
# Example
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
# v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Example 1:
# 2--(1)-->1
# |
# (1)
# |
# v
# 3--(1)-->4
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

"""
Algo: BFS /DFS
D.S.:

Solution:
BFS
Time: O(n ^ n) worst
Space: O(N)
Corner cases:
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        import collections, sys
        w = {} # key: from, val: (to, dist)
        for u, v, ww in times:
            if u not in w:
                w[u] = []
            w[u].append((v, ww))

        q = collections.deque([(K, 0)])
        dist = [sys.maxsize] * (N + 1)
        # 注意 要把dist[K] = 0 因为不会再回来 否则就是SYS.MAXSIZE
        dist[K] = 0
        while q:
            (cur, d) = q.popleft()
            if cur not in w:
                continue
            for (nei, weight) in w[cur]:
                new_d = d + weight
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    q.append((nei, new_d))
        res = 0
        for i in range(1, N + 1):
            if dist[i] == sys.maxsize:
                return -1
            res = max(res, dist[i])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
