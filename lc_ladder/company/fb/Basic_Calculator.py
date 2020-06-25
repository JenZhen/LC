#! /usr/local/bin/python3

# https://leetcode.com/problems/basic-calculator/submissions/
# Example
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
"""
Algo:
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        for i in range(len(s) - 1, -1, -1):
            # calculate backwards
            c = s[i]

            if c.isdigit():
                operand = (10 ** n * int(c)) + operand
                n += 1

            elif c != ' ': # is '(' ')' or operator
                if n: # if operand
                    stack.append(operand)
                    n, operand = 0, 0
                if c == '(':
                    # if closing (
                    res = self.evaluate_expr(stack)
                    # pop ')'
                    stack.pop()
                    stack.append(res)
                else:
                    # if operator or starting ')'
                    stack.append(c)
        if n:
            stack.append(operand)
        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack):
        # pop a number
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
