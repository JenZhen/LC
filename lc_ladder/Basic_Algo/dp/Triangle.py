#!/usr/bin/python

# http://lintcode.com/en/problem/triangle/
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# Notice
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
# Example
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

"""
Algo: DP
D.S.:

Solution:
- State:
- Function:
- Initialization:
- Answer:

Time: O()
Space: O()

Corner cases:
"""

class Solution1:
    """
    Recursion
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    Time: O(2 ^ n) -- n is the number of levels triangle has
        level 1 -- 1 methods
        level 2 -- 2 methods
        level 3 -- 4 methods // 2 ^ n ways to the bottom level
    Space: O(1)
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0
        maxDepth = len(triangle)

        def dfs(i, j):
            if i == maxDepth - 1:
                return triangle[i][j]
            leftSum = dfs(i + 1, j)
            rightSum = dfs(i + 1, j + 1)
            return min(leftSum, rightSum) + triangle[i][j]

        return dfs(0, 0)


class Solution2:
    """
    Recursion
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    Improvement of Solution1:
    Use extra structure to keep track of previously calculated min path value at a node.
    This avoids a lot of redundent calculation.
    Time: O(n ^ 2) -- There are n ^ 2 nodes in total
    Space: O(n ^ 2) -- for hashValue structure to save values
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0
        maxDepth = len(triangle)
        # use hashValue structure, same as triangle to save values
        hashValue = []
        for level in triangle:
            hashValue.append([None] * len(level))

        def dfs(i, j):
            if i == maxDepth - 1:
                return triangle[i][j]
            if hashValue[i][j] is not None:
                return hashValue[i][j]
            leftSum = dfs(i + 1, j)
            rightSum = dfs(i + 1, j + 1)
            hashValue[i][j] = min(leftSum, rightSum) + triangle[i][j]
            return hashValue[i][j]
        res = dfs(0, 0)
        self.reprTriagnle(hashValue)
        return res

    def reprTriagnle(self, triangle):
        print("[")
        for level in triangle:
            print "[" + ", ".join([str(ele) for ele in level]) + "]"
        print("]")


class Solution3:
    """
    DP: Iteration -- Bottom-Up
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    Improvement:
    - State: f[i][j] starting from position i, j shortest path sum to the bottom level
    - Function: f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
    - Initialization: The bottom level has init value, same of the triangle
    - Answer: f[0][0]
    Use DP to avoid redundent computation.
    Time: O(n ^ 2) -- There are n ^ 2 nodes in total
    Space: O(n ^ 2) -- for minPath structure to save values
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0
        n = len(triangle)
        f = []
        for level in range(1, len(triangle) + 1):
            f.append([None] * level)
        # init bottom level of f
        for j in range(n): # if trianle has n levels, the nth level will have n elements
            f[n - 1][j] = triangle[n - 1][j]
        # iterate bottom-up to fill f
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
        # get answer on top
        printTriangle(f)
        return f[0][0]

class Solution4:
    """
    DP: Iteration -- Top-Down
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    Improvement:
    - State: f[i][j], the shortest distance from 0, 0 to position i, j.
            (To i, j, it may come from two shoulders if any)
    - Function: leftShoulder = f[i - 1][j - 1] if exists else maxsize
                rightShoulder = f[i - 1][j] if exists else maxsize
                f[i][j] = min(leftShoulder, rightShoulder) + triangle[i][j]
    - Initialization: f[0][0] = triangle[0][0]
    - Answer: min(f[n - 1][0], f[n - 1][1], ..., f[n - 1][n - 1])
            In python min takes multiple variables

    Use DP to avoid redundent computation.
    Time: O(n ^ 2) -- There are n ^ 2 nodes in total
    Space: O(n ^ 2) -- for minPath structure to save values
    """
    def minimumTotal(self, triangle):
        # write your code here
        import sys
        if triangle is None or len(triangle) == 0:
            return 0

        n = len(triangle)
        f = []
        for level in range(1, len(triangle) + 1):
            f.append([None] * level)
        # init top level of f
        f[0][0] = triangle[0][0]
        # iterate through f
        for i in range(1, n): # i: 1, n - 1
            for j in range(i + 1): # j: 0, i + 2 Buggy, be careful
                # existence check only cares about j
                # leftShoulder non-existence is out of boundry -- -1
                # rightShouler non-existence is out of boundry -- j == len(prevLevel)
                # There cannot be both non-existence
                leftShoulder, rightShoulder = None, None
                if j - 1 == -1: # no leftshoulder
                    leftShoulder = sys.maxsize
                    rightShoulder = f[i - 1][j]
                elif j == len(triangle[i - 1]): # no rightshoulder
                    rightShoulder = sys.maxsize
                    leftShoulder = f[i - 1][j - 1]
                else:
                    leftShoulder = f[i - 1][j - 1]
                    rightShoulder = f[i - 1][j]
                f[i][j] = min(leftShoulder, rightShoulder) + triangle[i][j]
        printTriangle(f)
        return min(f[n - 1])

class Solution5:
    """
    DP: Iteration -- Bottom-Up
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    Improvement of Solution3 to use less extra space
    Observed from solution3 that once a level of f is used to calculated upper level,
    it will never be visited. Hence I can use the bottom level f, and iterate to update it
    each upper level will be shorter. Max extra space needed will be O(n)
    Use DP to avoid redundent computation.
    Time: O(n ^ 2) -- There are n ^ 2 nodes in total
    Space: O(n) -- Only need to keep track of on level of f
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0:
            return 0
        n = len(triangle)
        # init f as the bottom level of triangle
        for j in range(n): # if trianle has n levels, the nth level will have n elements
            f = triangle[n - 1]
        # iterate bottom-up to fill f
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = min(f[j], f[j + 1]) + triangle[i][j]
        # get answer on top
        return f[0]


def printTriangle(triangle):
    print("[")
    for level in triangle:
        print "[" + ", ".join([str(ele) for ele in level]) + "]"
    print("]")


# Test Cases
if __name__ == "__main__":
    testCases = [
        {"triangle":
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        },
        {"triangle":
        [
             [2]
        ]
        },
        {"triangle":
        [
        ]
        },
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    solution3 = Solution3()
    solution4 = Solution4()
    solution5 = Solution5()
    for t in testCases:
        triangle = t["triangle"]
        print("res1: %s" %solution1.minimumTotal(triangle))
        print("res2: %s" %solution2.minimumTotal(triangle))
        print("res3: %s" %solution3.minimumTotal(triangle))
        print("res4: %s" %solution4.minimumTotal(triangle))
        print("res5: %s" %solution5.minimumTotal(triangle))
