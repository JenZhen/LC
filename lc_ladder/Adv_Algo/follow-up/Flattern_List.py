#! /usr/local/bin/python3

# https://lintcode.com/problem/flatten-list/description
# Example
# Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

# Example
# Given [1,2,[1,2]], return [1,2,1,2].

# Given [4,[3,[2,[1]]]], return [4,3,2,1].

# Challenge
# Do it in non-recursive.

# Notice
# If the element in the given list is a list, it can contain list too.

"""
Algo: Recursion, stack
D.S.:

Solution:
Time: O(n), Space: O(n)

Solution1:
Recursion

Solution2:
Iteration using stack

Corner cases:
Invalid test case: nestedList is number 10 not [10]
"""

class Solution1(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, list):
            return self.helper(nestedList)
        else:
            return self.helper([nestedList])
    def helper(self, nestedList):
        res = []
        for ele in nestedList:
            if isinstance(ele, list):
                res.extend(self.flatten(ele))
            else:
                res.append(ele)
        return res

class Solution2(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        res = []
        st = [nestedList]
        while st:
            top = st.pop()
            if isinstance(top, list):
                for ele in reversed(top):
                    st.append(ele)
            else:
                res.append(top)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
