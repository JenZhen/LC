#! /usr/local/bin/python3

# https://www.lintcode.com/problem/convert-expression-to-polish-notation/description
# Example
# 给定一个表达式字符串数组，返回该表达式的波兰表达式。（即去掉括号）
#
# 样例
# 对于 [(5 − 6) * 7] 的表达式（该表达式可表示为 ["(", "5", "−", "6", ")", "*", "7"]），
# 其对应的波兰表达式为 [ - 5 6 7]*（其返回的数值为["*", "−", "5", "6", "7"]）。
#
# 说明
# 波兰表达 的定义:
#
# http://en.wikipedia.org/wiki/Polish_notation
# http://baike.baidu.com/view/7857952.htm

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
    @return: The Polish notation of this expression
    """
    def convertToPN(self, expression):
        # write your code here
        prefix = []
        stack = []
        string_tmp = []
        for s in expression[::-1]:
            if s == '(':
                string_tmp.append(')')
            elif s == ')':
                string_tmp.append('(')
            else:
                string_tmp.append(s)

        for s in string_tmp:
            if s.isdigit():
                prefix = [s] + prefix
            else:
                while len(stack)  and self.opOrder(stack[-1], s):
                    op = stack.pop()
                    prefix = [op] + prefix
                if len(stack) == 0 or s != ')':
                    stack.append(s)
                else:
                    stack.pop()
        if len(stack):
            prefix = stack + prefix

        return prefix

    def opOrder(self, op1,op2):
        order_dic = {'*':4, '/':4, '+':3, '-':3}
        if op1 == '(' or op2 == '(':
            return False
        elif op2 == ')':
            return True
        else:
            if order_dic[op1] <= order_dic[op2]:
                return False
            else:
                return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
