#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    def cleanRoom(self, robot):
        visited = set()
        #               up,   right,  down,  left
        # this order is fixed, each is derived by turn right from previous
        self.dirs = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        x, y = 0, 0
        start_dir_idx = 0
        self.dfs(robot, x, y, start_dir_idx, visited)

    def dfs(self, robot, x, y, dir_idx, visited):
        # clean current location
        robot.clean()
        # if a place is cleaned, put in set
        visited.insert(str(x) + '-' + str(y))
        for i in range(4):
            next_dir = (i + dir) % 4
            newx, newy = x + self.dirs[next_dir][0], y + self.dirs[next_dir][1]
            if not visited[str(newx) + '-' + str(newy)] and robot.move():
                # if next position is not visited and can move over there
                self.dfs(robot, newx, newy, next_dir, visited)
                # move back to prev location, aka, [x, y]
                # step1: turn back 180 degree
                robot.turnRight()
                robot.turnRight()
                # step2: move one step
                robot.move()
                # step3: turn back 180 degree to original dir
                robot.turnLeft()
                robot.turnLeft()
            # turn right to next dir in the self.dirs list
            robot.turnRight()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
