#! /usr/local/bin/python3

# https://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation/description
# Example
# 给定一个表达式字符串数组，返回该表达式的逆波兰表达式（即去掉括号）。
#
# 样例
# 对于 [3 - 4 + 5]的表达式（该表达式可表示为["3", "-", "4", "+", "5"]），返回 [3 4 - 5 +]（该表达式可表示为 ["3", "4", "-", "5", "+"]）。
"""
Algo:
D.S.: 单调栈

Solution:
# TODO: 

Corner cases:
"""

class Solution:
    """
    @param expression: A string array
    @return: The Reverse Polish notation of this expression
    """
    def convertToRPN(self, expression):
        # write your code here
        RPN = []
        cal = []
        for s in expression:
            if s == "(":
                cal.append(s)
            elif s == ")":
                while cal and cal[-1] != "(":
                    RPN.append(cal[-1])
                    cal.pop()
                cal.pop()
            elif s.isdigit():
                RPN.append(s)
            else:
                if cal:
                    if cal[-1] != "(":
                        while self.getLevel(cal[-1]) >= self.getLevel(s):
                            RPN.append(cal[-1])
                            cal.pop()
                            if not cal:
                                break
                cal.append(s)

        while cal:
            RPN.append(cal[-1])
            cal.pop()

        return RPN

    def getLevel(self, s):
        if s == "+" or s == "-":
            return 1
        if s == "*" or s == "/":
            return 2

        return 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
