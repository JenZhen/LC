#! /usr/local/bin/python3

# https://lintcode.com/problem/bomb-enemy/description?_from=ladder&&fromId=18
# Example
# 给一个二维矩阵, 每一个格子都可能是一堵墙 W, 一个敌人 E 或者空 0 (数字 '0'), 返回你可以用一个炸弹杀死的最大敌人数. 炸弹会杀死所有在同一行和同一列没有墙阻隔的敌人, 因为墙比较坚固难以摧毁.
#
# 样例
# 给一个矩阵:
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# 返回 3.(在（1, 1）处放炸弹可以杀死 3 个敌人)

注意事项
你只能在空的地方放置炸弹.

"""
Algo: DP
D.S.:

Solution:
# 0 E 0 0
# E 0 W E
# 0 E 0 0

注意这个题只能所在行和所在列，不能扩展到其他行和列（bfs, union-find解法)
思路：
遍历整个表格
- 固定一行，从左向右遍历每一列，找能连在一起最多有几个E
    - 是否重新计数的条件 （是否是第一列，是做左边是w， 同理对于列计数，是不是第一行，上面一个是不是W）
- 因为列是变的，所以可以用一个array 来记录上次计算这一列有几个E （如果不满足重新计数条件就不用重新算了）
- 可能解的位置 grid[i][j] = "0"
- 为了简单也给'w' 计数，但是不会考虑算入结果

Corner cases:
"""

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        rowcnt = 0
        colcnt = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                # rowcnt re-count or not
                if j == 0 or grid[i][j - 1] == 'W':
                    rowcnt = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rowcnt += 1
                # colcnt re-count or not
                if i == 0 or grid[i - 1][j] == 'W':
                    colcnt[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            colcnt[j] += 1
                # update res
                if grid[i][j] == '0' and res < rowcnt + colcnt[j]:
                    print("row: %s, col: %s" %(rowcnt, colcnt[j]))
                    res = rowcnt + colcnt[j]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
