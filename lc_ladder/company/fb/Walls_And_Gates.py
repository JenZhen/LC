#! /usr/local/bin/python3

# https://www.lintcode.com/problem/walls-and-gates/description
# Example
# 您将获得一个使用这三个可能值初始化的 m×n 2D 网格。
# -1 - 墙壁或障碍物。
# 0 - 门。
# INF - Infinity是一个空房间。我们使用值 2 ^ 31 - 1 = 2147483647 来表示INF，您可以假设到门的距离小于 2147483647。
# 在代表每个空房间的网格中填入到距离最近门的距离。如果不可能到达门口，则应填入 INF。
#
# 样例
# 样例1
#
# 输入：
# [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# 输出：
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
# 解释：
# 2D网络为：
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# 答案为：
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
# 样例2
#
# 输入：
# [[0,-1],[2147483647,2147483647]]
# 输出：
# [[0,-1],[1,2]]

"""
Algo:
D.S.:

Solution:
那gate 和距离放入queue，从所有的gate 向房子搜索
如queue条件， 不越界， 空房间没有被搜索过，也就是还是INF值
最后留下访问不到的房间值为INF

Time: O(mn)

Corner cases:
"""

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        from collections import deque
        m = len(rooms)
        n = len(rooms[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            (cur_x, cur_y, cur_dist) = q.popleft()
            for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = cur_x + dx, cur_y + dy
                if 0 <= new_x < m and 0 <= new_y < n and rooms[new_x][new_y] == 2147483647:
                    q.append((new_x, new_y, cur_dist + 1))
                    rooms[new_x][new_y] = cur_dist + 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
