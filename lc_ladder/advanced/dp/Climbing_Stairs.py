#! /usr/local/bin/python3

# https://www.lintcode.com/problem/climbing-stairs/description
# Example
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example
# Given an example n=3 , 1+1+1=2+1=1+2=3
# return 3

"""
Algo: DP， 滚动数组
D.S.:

Solution:
Time：O(n) Space O(1)

DP 分析
1. 状态
f[i]: 到第i个台阶，有几种方式， i 从0开始
2. 方程
f[i] = f[i - 1] + f[i - 2] #可以%2
f[i]的值可以来自f[i - 1] 和 f[i - 2]

3. 初始化
f[0] = 1 # 到台阶0，1种方式
f[1] = 1 # 到台阶1，1种方式
4. 答案
f[n]

Corner cases:
n = 0, return 0
"""

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n is None or n <= 0:
            return 0

        f = [1, 1] # init with level 0, level 1 with 1, 1
        for i in range(2, n + 1):
            f[i % 2]  = f[(i - 1) % 2] + f[(i - 2) % 2]
        return f[n % 2]



# Test Cases
if __name__ == "__main__":
    solution = Solution()
