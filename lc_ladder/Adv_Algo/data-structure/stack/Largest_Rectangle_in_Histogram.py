#! /usr/local/bin/python3

# https://www.lintcode.com/problem/largest-rectangle-in-histogram/description
# Example
# Given height = [2,1,5,6,2,3],
# return 10.

"""
Algo:
D.S.: Monotonous Stack -- maintain an ascending Monotonous Stack

Solution:
Time: O(N) -- N in input height length

Idea: from 0 to 6 using each height, how wide the range could be ?
    -- finding the left side first smaller and right side first smaller height
    -- this is the key feature of *monotonous stack*
Trick: can use -1 at both end as sentinel. Or not, use len(stack) to decide stack size
index: -1, 0, 1, 2, 3, 4, 5, 6, 7
array: -1, 2, 1, 5, 6, 2, 3, 3, -1
dist:      1, 7, 2, 1, 5, 2, 3,
1. Solution1 is more straight-forward; Solution2 is a neat way of implementing
2. Be careful about the same value scenario


Corner cases:
"""
class Solution1:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0
        stack = [] # len(height) + 2
        rangeArr = [[-1, -1] for i in range(len(height))] # len(height)
        stack.append(-1)
        height.append(-1)
        for i in range(len(height)):
            if i == 0:
                rangeArr[i][0] = stack[-1]
                stack.append(i)
            if height[i] > height[stack[-1]]:
                rangeArr[i][0] = stack[-1]
                stack.append(i)
            elif height[i] < height[stack[-1]]:
                while height[stack[-1]] > height[i]:
                    rangeArr[stack[-1]][1] = i
                    stack.pop()
                if i == len(height) - 1:
                    break
                rangeArr[i][0] = stack[-1]
                stack.append(i)
            else: # ==
                rangeArr[i][0] = rangeArr[stack[-1]][0]
                stack.append(i)

        print("rangeArr")
        print(rangeArr)

        res = 0
        for i in range(len(rangeArr)):
            dist = rangeArr[i][1] - rangeArr[i][0] - 1
            res = max(res, dist * height[i])
        return res

class Solution2:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height) + 1):
            curHeight = -1 if (i == len(height)) else height[i]
            while len(stack) and curHeight <= height[stack[-1]]:
                h = height[stack.pop()]
                w = i if (len(stack) == 0) else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

# Test Cases
if __name__ == "__main__":
    testCases = [
        [2,1,5,6,2,3], # 10
    ]
    s1 = Solution1()
    s2 = Solution2()
    for height in testCases:
        res1 = s1.largestRectangleArea(height)
        print("res1: %s" %res1)
        res2 = s2.largestRectangleArea(height)
        print("res2: %s" %res2)
