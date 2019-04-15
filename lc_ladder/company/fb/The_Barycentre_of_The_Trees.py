#! /usr/local/bin/python3

# https://www.lintcode.com/problem/the-barycentre-of-the-trees/description?_from=ladder&&fromId=29
# Example
# Details in /advanced/dp
# 对于一棵多叉树，如果有一个结点 R，以R为根，其所有子树的最大子树的结点数最少，则称结点 R 为这棵树的重心。
# 现在给你一棵有 n 个结点的多叉树，求这棵树的重心，如果有多个重心，则返回编号最小的。
# x[i], y[i]代表第 i 条边的两个点。
#
# 样例
# 给出 x = [1], y = [2], 返回 1。
#
# 解释：
# 1 和 2 都可以为重心，但是 1 的编号最小。
# 给出 x = [1,2,2], y = [2,3,4], 返回 2。
#
# 解释：
# 2 为重心。
# 注意事项
# 2 <= n <= 10^5
# 1 <= x[i], y[i] <= n
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
