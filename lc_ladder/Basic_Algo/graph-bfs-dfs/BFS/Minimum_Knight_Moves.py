#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-knight-moves/
# Example
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
#
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
# then one square in an orthogonal direction.
#
# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
#
# Example 1:
#
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:
#
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#
# Constraints:
#
# |x| + |y| <= 300

"""
Algo:
D.S.: BFS

Solution:
数层 BFS 模板
Time: O(mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        dirs = [
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1)
        ]

        visited = set([(0, 0)])
        step = -1
        q = collections.deque([(0, 0)])

        while q:
            size = len(q)
            step += 1
            for _ in range(size):
                (cur_x, cur_y) = q.popleft()
                if cur_x == x and cur_y == y:
                    return step
                for (dx, dy) in dirs:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if (new_x, new_y) not in visited:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))
        return step

# Test Cases
if __name__ == "__main__":
    solution = Solution()
