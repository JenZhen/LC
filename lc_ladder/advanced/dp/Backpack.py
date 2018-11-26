#! /usr/local/bin/python3

# https://lintcode.com/problem/backpack/description
# Example
# Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

# If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

# You function should return the max size we can fill in the given backpack.

# Challenge
# O(n x m) time and O(m) memory.

# O(n x m) memory is also acceptable if you do not know how to optimize memory.

# Notice
# You can not divide any item into small pieces.

"""
Algo: 背包dp, 滚动数组DP
D.S.:

Solution1, 2: 滚动数组DP
Time: O(n ^ 2) Space: O(n)
f[i][j]: 拿前i个物品，能否正好填到体积j
因为是考虑前i 个物品，所以要有Padding f[0][i] 应该都是False 除了f[0][0], f[i][0]都是 True

DP 分析
1. 状态
f[i][j]：拿前i个物品，能否正好填到体积j
2. 方程
f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
倒着考虑有2种拿法：
f[i - 1][j] -- 拿前i-1个物品正好有体积i, 就不用拿第i个了
f[i - 1][j - A[i - 1]] -- 拿了第i个物品正好有体积j,说明拿i-1的时候正好有体积j-1,
    前提是j - A[i - 1] >= 0， 应为物品没有根据大小来排序

考虑滚动数组 Space O(size_of_backpack)

3. 初始化
f[i][0] = True, #第一列，取前i个物品，能达到体积0 only if A[i] <= backpackSize
f[0][j] = False #第一行, 除了f[0][0] = True
考虑滚动数组，只需要init first row, 每行循环要init 第一列的元素
4. 答案
find the max j such as, f[n][j] = True, where n is the count of items

Solution3:
TODO: 分析明白
so far the best solution
Time: O(nlogn)

Follow-up:
[1， 24， 5， 6], 分成2组，使得2组之和尽量相同（尽量平分为2组）
1. 不需要排序
2. 要学会分析出来背包 和背包大小
sum = 1+24+5+6 = 36
理想的平分 每组有18
题目转化为，如何从1，24，5，6中来填满大小为18的背包

Corner cases:
"""

class Solution1:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        # init first row False, first col True, f[0][0] = True
        for j in range(m + 1):
            f[0][j] = False
        for i in range(n + 1):
            f[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]
        for j in range(m, -1, -1):
            if f[i][j]:
                return j
        return 0

class Solution2:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        n = len(A)
        f = [[False] * (m + 1), [False] * (m + 1)]

        f[0][0] = True
        for i in range(1, n + 1):
            f[i % 2][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i % 2][j] = f[(i - 1) % 2][j] or f[(i - 1) % 2][j - A[i - 1]]
                else:
                    f[i % 2][j] = f[(i - 1) % 2][j]

        for i in range(m, -1, -1):
            if f[n % 2][i]:
                return i
        return 0

class Solution_Followup:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        A.sort()
        intervals = [[0, 0]]
        for item in A:
            new_intervals = []
            for interval in intervals:
                new_intervals.append([interval[0] + item, interval[1] + item])

            intervals = self.merge_intervals(intervals, new_intervals)

        max_size = 0
        for interval in intervals:
            if interval[0] <= m <= interval[1]:
                return m
            if interval[0] > m:
                break
            max_size = max(max_size, interval[1])
        return max_size

    def merge_intervals(self, list1, list2):
        i, j = 0, 0
        intervals = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                self.push_to_intervals(intervals, list1[i])
                i += 1
            else:
                self.push_to_intervals(intervals, list2[j])
                j += 1

        while i < len(list1):
            self.push_to_intervals(intervals, list1[i])
            i += 1

        while j < len(list2):
            self.push_to_intervals(intervals, list2[j])
            j += 1

        return intervals

    def push_to_intervals(self, intervals, interval):
        if not intervals or intervals[-1][1] + 1 < interval[0]:
            intervals.append(interval)
            return

        intervals[-1][1] = max(intervals[-1][1], interval[1])

# Test Cases
if __name__ == "__main__":
    solution = Solution()
