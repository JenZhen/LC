#! /usr/local/bin/python3

# https://www.lintcode.com/problem/nested-list-weight-sum
# Example
# 给一个嵌套的整数列表, 返回列表中所有整数由它们的深度加权后的总和. 每一个元素可能是一个整数或一个列表(其元素也可能是整数或列表)
#
# 样例
# 给出列表 [[1,1],2,[1,1]], 返回 10. (4个'1'的深度是 2, 1个'2'的深度是1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
# 给出列表 [1,[4,[6]]], 返回 27. (1个 '1' 的深度是1, 1个 '4' 的深度是2, 以及1个 '6'的深度是3, 1 + 4 * 2 + 6 * 3 = 27)

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

import types
class Solution1(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        return self.helper(nestedList, 1)

    def helper(self, li, level):
        if not li:
            return 0
        sum = 0
        for ele in li:
            if ele.isInteger():
                sum += ele.getInteger() * level
            else:
                sum += self.helper(ele.getList(), level + 1)
        return sum

class Solution2(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0
        res = 0
        from collections import deque
        q = deque([])
        for ele in nestedList:
            q.append((ele, 1))

        while len(q):
            curEle = q.popleft()
            if curEle[0].isInteger():
                res += curEle[0].getInteger() * curEle[1]
            else:
                for ele in curEle[0].getList():
                    q.append((ele, curEle[1] + 1))
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
