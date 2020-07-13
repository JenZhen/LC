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

Solution2:
套用expression计算模板
lc_ladder/Adv_Algo/data-structure/stack/Expression_Evaluation.py
Time: O(n)
Space: O(n)

Corner cases:
"""

class Solution1:
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


class Solution2_Standard:
    def calculate(self, s: str) -> int:

        parsed_list = self.parse(s)
        st_num = []
        st_op = []
        for ele in parsed_list:
            if ele.isdigit():
                st_num.append(int(ele))
            else:
                if ele == ')':
                    while st_op and st_op[-1] != '(':
                        op = st_op.pop()
                        if len(st_num) < 2:
                            raise "Invalid input"
                        n2 = st_num.pop()
                        n1 = st_num.pop()
                        st_num.append(self.calc(n1, n2, op))
                    if st_op[-1] == '(':
                        st_op.pop()
                elif ele == '(':
                    st_op.append(ele)
                elif ele == '+' or ele == '-':
                    while st_op and st_op[-1] != '(':
                        op = st_op.pop()
                        if len(st_num) < 2:
                            raise "Invalid input"
                        n2 = st_num.pop()
                        n1 = st_num.pop()
                        st_num.append(self.calc(n1, n2, op))
                    st_op.append(ele)

        while st_op:
            op = st_op.pop()
            if len(st_num) < 2:
                raise "Invalid input"
            n2 = st_num.pop()
            n1 = st_num.pop()
            st_num.append(self.calc(n1, n2, op))
        return st_num[-1]

    def calc(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2

    def parse(self, s):
        n = len(s)
        i = 0
        res = []
        while i < n:
            c = s[i]
            if c.isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                res.append(s[i:j])
                i = j
            elif c == '+' or c == '-' or c == '(' or c == ')':
                res.append(c)
                i += 1
            elif c == ' ':
                i += 1
                continue
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
