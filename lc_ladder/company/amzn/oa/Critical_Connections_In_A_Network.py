#! /usr/local/bin/python3

# https://leetcode.com/problems/critical-connections-in-a-network/submissions/
# Example
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections
# forming a network where connections[i] = [a, b] represents a connection between servers a and b.
# Any server can reach any other server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# Return all critical connections in the network in any order.
#
# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
#
# Constraints:
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
"""
Algo:
D.S.:

Solution:
O(V+E)

Corner cases:
"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        lows = [0]*n
        ranks = [0]*n
        visited = [False]*n
        cc = []
        counter = 0

        def dfs(at, parent, cc, lows, ranks, visited, counter):
            visited[at] = True
            counter +=1
            ranks[at] = counter
            lows[at] = counter
            for nb in adj[at]:
                if nb== parent: continue
                if not visited[nb]:
                    dfs(nb,at,cc, lows, ranks, visited, counter)
                    lows[at] = min(lows[at], lows[nb])
                    if ranks[at] < lows[nb]:
                        # if rank is lower then that means this is the only edge connecting any vertex beyond it.
                        cc.append([min(at,nb), max(at,nb)])
                else:
                    lows[at] = min(lows[at], lows[nb])

        for node in adj.keys():
            #initiate dfs
            if not visited[node]:
                dfs(node,-1, cc, lows, ranks, visited, counter)
        return cc

# Test Cases
if __name__ == "__main__":
    solution = Solution()
