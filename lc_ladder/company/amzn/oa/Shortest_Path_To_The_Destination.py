#! /usr/local/bin/python3

# https://www.lintcode.com/problem/shortest-path-to-the-destination/description
# Example
# 给定表示地图上坐标的2D数组，地图上只有值0,1,2.0表示可以通过，1表示不可通过，2表示目标位置。从坐标[0,0]开始，你只能上，下，左，右移动。找到可以到达目的地的最短路径，并返回路径的长度。
#
# 样例
# 给定:
#
# [
#  [0, 0, 0],
#  [0, 0, 1],
#  [0, 0, 2]
# ]
# 返回: 4
#
# 注意事项
# 1.地图一定存在且不为空，并且只存在一个目的地

"""
Algo: BFS -- without using visited map
D.S.: Grid BFS

Solution:
Time: O(n) -- each cell visited once
Space: O(1)

Solution1: exam if target when reading from queue (curCoor)
Solution2: exam if target when adding to queue (newCoor)

Corner cases:
"""

class Solution1:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here

        # no need to validate map
        row = len(targetMap)
        col = len(targetMap[0])
        from collections import deque
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque([[0, 0]])
        step = -1
        while q:
            size = len(q)
            step += 1
            for _ in range(size):
                curCoor = q.popleft()
                if targetMap[curCoor[0]][curCoor[1]] == 2:
                    return step
                for d in dirs:
                    newCoor = [curCoor[0] + d[0], curCoor[1] + d[1]]
                    if self.validateCoor(targetMap, newCoor):
                        # mark curCoor as visited in targetMap
                        targetMap[curCoor[0]][curCoor[1]] = 1
                        q.append(newCoor)
        return -1

    def validateCoor(self, targetMap, coor):
        row = len(targetMap)
        col = len(targetMap[0])
        if coor[0] < 0 or coor[0] >= row: return False
        if coor[1] < 0 or coor[1] >= col: return False
        if targetMap[coor[0]][coor[1]] == 1: return False
        return True

class Solution2:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        # no need to validate map
        row = len(targetMap)
        col = len(targetMap[0])
        from collections import deque
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque([[0, 0]])
        step = 0
        if targetMap[0][0] == 2:
            return step
        while q:
            size = len(q)
            step += 1
            for _ in range(size):
                curCoor = q.popleft()
                for d in dirs:
                    newCoor = [curCoor[0] + d[0], curCoor[1] + d[1]]
                    if self.validateCoor(targetMap, newCoor):
                        if targetMap[newCoor[0]][newCoor[1]] == 2:
                            return step
                        targetMap[newCoor[0]][newCoor[1]] = 1
                        q.append(newCoor)
        return -1

    def validateCoor(self, targetMap, coor):
        row = len(targetMap)
        col = len(targetMap[0])
        if coor[0] < 0 or coor[0] >= row: return False
        if coor[1] < 0 or coor[1] >= col: return False
        if targetMap[coor[0]][coor[1]] == 1: return False
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
