#! /usr/local/bin/python3

# https://www.lintcode.com/problem/candy/description
# # Example
# 有 N 个小孩站成一列。每个小孩有一个评级。给定数组 ratings 代表这些小孩的评级。
#
# 现在你需要按照以下要求，给小孩们分糖果：
#
# 每个小孩至少得到一颗糖果。
#
# 评级越高的小孩可以比他相邻的两个小孩得到更多的糖果。
#
# 你最少要准备多少糖果？
#
# 样例
# Example 1:
#
# Input: [1, 2]
# Output: 3
# Explanation: Give the first child 1 candy and give the second child 2 candies.
# Example 2:
#
# Input: [1, 1, 1]
# Output: 3
# Explanation: Give every child 1 candy.
# Example 3:
#
# Input: [1, 2, 2]
# Output: 4
# Explanation:
#     Give the first child 1 candy.
#     Give the second child 2 candies.
#     Give the third child 1 candy.
# 注意事项
# 数据保证评级的范围是[0,2000]
"""
Algo: Two-Side
D.S.:

Solution:
两边夹
这个题略偶歧义
一个例子：
[1, 2, 2] -> 4
因为candy 分配是[1, 2, 1] 

Corner cases:
"""

class Solution:
    """
    @param ratings: Children's ratings
    @return: the minimum candies you must give
    """
    def candy(self, ratings):
        # write your code here
        if not ratings: return 0
        arr = [1] * len(ratings)
        # from left
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and arr[i] <= arr[i + 1]:
                arr[i] = arr[i + 1] + 1
        return sum(arr)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
