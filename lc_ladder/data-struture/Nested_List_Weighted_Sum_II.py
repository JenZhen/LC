#!/usr/local/bin/python3

# https://leetcode.com/problems/nested-list-weight-sum-ii/
# Example
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e.,
# the leaf level integers have weight 1, and the root level integers have the largest weight.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: 8
# Explanation: Four 1's at depth 1, one 2 at depth 2.
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: 17
# Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

"""
Algo: DFS, BFS
D.S.: queue

Solution1: DFS
和nested-list-weight-sum 解法相同，但是第一步先去找最深的层数，然后倒着算weight

Solution2: BFS
Solution3: BFS not using extra space to save level sum

Corner cases:
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution1:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        maxDepth = self.get_max_depth(nestedList, 1)
        print(maxDepth)
        return self.get_weighted_sum(nestedList, maxDepth)

    def get_max_depth(self, nestedList, depth):
        tmp = depth
        for ele in nestedList:
            if ele.isInteger():
                tmp = max(tmp, depth)
            else:
                tmp = max(tmp, self.get_max_depth(ele.getList(), depth + 1))
        return tmp

    def get_weighted_sum(self, nestedList, depth):
        sum = 0
        for ele in nestedList:
            if ele.isInteger():
                sum += ele.getInteger() * depth
            else:
                sum += self.get_weighted_sum(ele.getList(), depth - 1)
        return sum

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution2:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque
        if not nestedList or len(nestedList) == 0:
            return 0
        sumStack = []
        q = deque([])
        q.append(nestedList)
        print(len(q))
        while q:
            size = len(q)
            curLevelSum = 0
            # 遍历每一层，把层内的整数拿出来求和，放在sumStack中
            for _ in range(size):
                sub_list = q.popleft()
                for ele in sub_list:
                    if ele.isInteger():
                        curLevelSum += ele.getInteger()
                    else:
                        q.append(ele.getList())
            sumStack.append(curLevelSum)

        sum = 0
        maxLevel = len(sumStack)
        # sumStack 的元素个数就是层数，第一个数就是第一层的整数和
        for level in range(maxLevel):
            sum += sumStack[level] * (maxLevel - level)
        return sum


class Solution3:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque
        if not nestedList or len(nestedList) == 0:
            return 0
        sumStack = []
        q = deque([])
        q.append(nestedList)
        res = 0
        cumres = 0
        while q:
            size = len(q)
            for _ in range(size):
                sub_list = q.popleft()
                for ele in sub_list:
                    if ele.isInteger():
                        cumres += ele.getInteger()
                    else:
                        q.append(ele.getList())
            res += cumres
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
