#! /usr/local/bin/python3

# https://leetcode.com/problems/reconstruct-itinerary/
# Example
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.
"""
Algo: DFS, Backtracking
D.S.:

Solution:
corner:
[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
KUL is not a key in the graph, need to verify

Time: O(E ^ d) -- E is # of flight d is the maximum number of flights from an airport.
Space: O(∣V∣+∣E∣)
Corner cases:
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.g = {} # key: origin, val: list of destinations
        self.visited = {}
        self.flights = len(tickets)
        for t in tickets:
            origin, dest = t[0], t[1]
            if origin not in self.g:
                self.g[origin] = []
            self.g[origin].append(dest)

        for origin, dests in self.g.items():
            self.g[origin].sort()
            self.visited[origin] = [False for _ in range(len(self.g[origin]))]

        self.res = []
        route = ['JFK']
        self.dfs(route)
        return self.res


    def dfs(self, route):
        if len(route) == self.flights + 1:
            self.res = route[:]
            return True
        # 这个情况不要忘掉！！
        origin = route[-1]
        if origin not in self.g:
            return False
        for i, next_dest in enumerate(self.g[origin]):
            if not self.visited[origin][i]:
                self.visited[origin][i] = True
                route.append(next_dest)
                ret = self.dfs(route)
                route.pop()
                self.visited[origin][i] = False
                if ret: return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
