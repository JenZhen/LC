#! /usr/local/bin/python3

# https://www.lintcode.com/problem/judge-route-circle/?_from=ladder&&fromId=18
# Example
# 最初，机器人位于(0, 0)处。 给定一系列动作，判断该机器人的移动轨迹是否是一个环，这意味着它最终会回到原来的位置。
#
# 移动的顺序由字符串表示。 每个动作都由一个字符表示。 有效的机器人移动是R（右），L（左），U（上）和D（下）。 输出应该为true或false，表示机器人是否回到原点。
#
# 样例
# 样例1:
#
# 输入: "UD"
# 输出: true
# 样例2:
#
# 输入: "LL"
# 输出: false

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        dx, dy = 0, 0
        for i in moves:
            if i == 'U':
                dy += 1
            if i == 'D':
                dy -= 1
            if i == 'L':
                dx -= 1
            if i == 'R':
                dx += 1
        return dx == 0 and dy == 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
