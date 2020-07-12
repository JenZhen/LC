#! /usr/local/bin/python3

# https://leetcode.com/problems/bus-routes/
# Example
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
# For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only,
# what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Note:
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.

"""
Algo: BFS, map
D.S.:

Solution:
https://www.youtube.com/watch?v=vEcm5farBls

Time: O(mn)
Space: O(mn) 所有station bfs 一遍

Corner cases:
"""


from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        q = deque([])
        visited_routes = set()
        routes_taken = 0
        station_routes_map = {} #key: station, val: routes set
        # populate station_routes_map
        for route, stations in enumerate(routes):
            for s in stations:
                if s not in station_routes_map:
                    station_routes_map[s] = set()
                station_routes_map[s].add(route)
        # visited_routes init as station Source's routes
        for route in station_routes_map[S]:
            visited_routes.add(route)
        # queue init with stations shares same routes with Source station
        for route in station_routes_map[S]:
            for station in routes[route]:
                # q may have duplicate stations
                q.append(station)

        while len(q):
            # 数层数模板
            q_size = len(q)
            routes_taken += 1
            while q_size > 0:
                cur_station = q.popleft()
                if cur_station == T:
                    return routes_taken
                for route in station_routes_map[cur_station]:
                    if route not in visited_routes:
                        visited_routes.add(route)
                        for station in routes[route]:
                            q.append(station)
                q_size -= 1
        return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        from collections import deque
        if S == T:
            return 0
        q = deque([])
        visited_routes = set()
        station_routes_map = {} #key: station, val: routes set
        # populate station_routes_map
        for route, stations in enumerate(routes):
            for s in stations:
                if s not in station_routes_map:
                    station_routes_map[s] = set()
                station_routes_map[s].add(route)
        # visited_routes init as station Source's routes
        for route in station_routes_map[S]:
            visited_routes.add(route)
        # queue init with stations shares same routes with Source station
        for route in station_routes_map[S]:
            for station in routes[route]:
                # q may have duplicate stations
                q.append((station,1))

        # 另一种数层方式
        while len(q):
            # 数层数模板
            cur_station, stop = q.popleft()
            if cur_station == T:
                return stop
            for route in station_routes_map[cur_station]:
                if route not in visited_routes:
                    visited_routes.add(route)
                    for station in routes[route]:
                        q.append((station, stop + 1))
        return -1
# Test Cases
if __name__ == "__main__":
    solution = Solution()
