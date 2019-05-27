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
        self.dirs = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        i, j = 0, 0
        start_dir = 0
        self.dfs(robot, i, j, start_dir, visited)

    def dfs(self, robot, i, j, dir, visited):
        robot.clean()
        visited.insert(str(i) + '-' + str(j))
        for i in range(4):
            next_dir = (i + dir) % 4
            newx, newy = x + self.dirs[next_dir][0], self.dirs[next_dir][1]
            if not visited[str(newx) + '-' + str(newy)] and robot.move():
                # if next position is not visited and can move over there
                self.dfs(robot, newx, newy, next_dir, visited)
                robot.turnRight()
                robot.turnRight
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnRight()

vector<vector<int>> dirs{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    void cleanRoom(Robot& robot) {
        unordered_set<string> visited;
        helper(robot, 0, 0, 0, visited);
    }
    void helper(Robot& robot, int x, int y, int dir, unordered_set<string>& visited) {
        robot.clean();
        visited.insert(to_string(x) + "-" + to_string(y));
        for (int i = 0; i < 4; ++i) {
            int cur = (i + dir) % 4, newX = x + dirs[cur][0], newY = y + dirs[cur][1];
            if (!visited.count(to_string(newX) + "-" + to_string(newY)) && robot.move()) {
                helper(robot, newX, newY, cur, visited);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnLeft();
                robot.turnLeft();
            }
            robot.turnRight();
        }
    }

# Test Cases
if __name__ == "__main__":
    solution = Solution()
