#! /usr/local/bin/python3

# https://www.lintcode.com/problem/the-barycentre-of-the-trees/description?_from=ladder&&fromId=29
# Example
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
Algo: DFS, DP
D.S.: Tree, Graph, tree dp

Solution:
树形 DP 的代表题型
题解

随意选择一个点作为树的根节点，比如 1 结点。
dp[i] 代表以 i 为根的子树的结点个数，dp[i] = sum(dp[j]) + 1。
则以 i 为根的子树的最大结点个数为 max(max(dp[j]), n - dp[i])。
在 DFS 的过程中维护答案即可。

时间复杂度为建图和两次DFS，O(N)。空间复杂度O(N)
Corner cases:
"""

class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    ansNode, ansSize = 0, 0
    def getBarycentre(self, x, y):
        # Write your code here
        n = len(x) + 1
        g = [ [] for i in range(n + 1) ]
        dp = [ 0 for i in range(n + 1) ]
        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
        self.ansNode = 0
        self.ansSize = n +1
        from_node = 0
        to_node =  1
        self.dfs(to_node, from_node, n, dp, g)
        print(dp)
        return self.ansNode

    def dfs(self, to_node, from_node, n, dp, g):
        dp[to_node] = 1
        maxSubtree = 0
        for i in g[to_node]:
            if(i == from_node):
                continue
            self.dfs(i, to_node, n, dp, g)
            dp[to_node] += dp[i]
            maxSubtree = max(maxSubtree, dp[i])
        maxSubtree = max(maxSubtree, n - dp[to_node])
        if((maxSubtree < self.ansSize) or (maxSubtree == self.ansSize and to_node < self.ansNode)):
            self.ansNode, self.ansSize = to_node, maxSubtree

# Test Cases
if __name__ == "__main__":
    solution = Solution()
