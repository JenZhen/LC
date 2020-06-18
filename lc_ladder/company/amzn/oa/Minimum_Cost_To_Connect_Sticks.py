#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-cost-to-connect-sticks/my-submissions
# Example
# 为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
# 如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。
# 返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序
#
# 样例
# 样例 1:
#
# 输入：
#  [2,4,3]
# 输出：14
# 解释：先将 2 和 3 连接成 5，花费 5；再将 5 和 4 连接成 9；总花费为 14
# 样例 2:
#
# 输入：
#  [1,8,3,5]
# 输出：30
"""
Algo: Heap
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def MinimumCost(self, sticks):
        from heapq import heapify, heappush, heappop
        # write your code here
        if not sticks: return 0
        if len(sticks) == 1:
            return sticks[0]
        res = 0
        h = sticks
        heapify(h)
        while len(h) >= 2:
            s1 = heappop(h)
            s2 = heappop(h)
            res += (s1 + s2)
            heappush(h, (s1 + s2))
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
