#! /usr/local/bin/python3

# https://lintcode.com/problem/valid-parentheses/description
# Example
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""
Algo:
D.S.: stack

Solution:
Time: O(n)
Space: O(n)

Corner cases:
{}
{}] -- more right half, but stack is empty, return false
"""

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        st = []

        for ele in s:
            if ele == "{" or ele == "(" or ele == "[":
                st.append(ele)
            elif ele == "}" or ele == ")" or ele == "]":
                if len(st) == 0:
                    return False
                prev = st.pop()
                if ele == "}" and prev != "{":
                    return False
                if ele == "]" and prev != "[":
                    return False
                if ele == ")" and prev != "(":
                    return False
            else:
                return False
        return len(st) == 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
