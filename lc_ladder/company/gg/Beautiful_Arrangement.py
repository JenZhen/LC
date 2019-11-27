#! /usr/local/bin/python3

# https://lintcode.com/problem/beautiful-arrangement/description?_from=ladder&&fromId=18
# Example
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:
#
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?
# 样例
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# 注意事项
# N is a positive integer and will not exceed 15.

"""
Algo: DFS, Backtracking
D.S.:

Solution:
Time:
Space: O(n)
Similar to subset


Corner cases:
"""

class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def countArrangement(self, N):
        # Write your code here
        if not N:
            return 0

        visited = [0] * (N + 1) #0 as not used, 1 as used
        self.res = 0
        self.dfs(1, N, visited)
        return self.res

    def dfs(self, startPos, N, visited):
        if startPos > N:
            self.res += 1
            return
        # i start from 1, prev may have value put in later index,
        # if not usable, visited[i] = 1
        for i in range(1, N + 1):
            # 如果查完了最后一个数，那么就构成一个可行解
            if i > N:
                self.res += 1
                return
            if visited[i] == 0 and (i % startPos == 0 or startPos % i == 0):
                visited[i] = 1
                # 找到startPos一个值之后，进入下一个递归，去找startPos + 1 的可行值
                self.dfs(startPos + 1, N, visited)
                # 回来之后要reset visited = 0
                visited[i] = 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
