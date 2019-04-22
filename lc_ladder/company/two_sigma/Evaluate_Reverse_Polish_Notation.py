#! /usr/local/bin/python3

# https://www.lintcode.com/problem/evaluate-reverse-polish-notation/description
# Example
# 求逆波兰表达式的值。
#
# 在逆波兰表达法中，其有效的运算符号包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰计数表达。
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 样例 1:
#
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ["2", "1", "+", "3", "*"] -> (2 + 1) * 3 -> 9
# 样例 2:
#
# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: ["4", "13", "5", "/", "+"] -> 4 + 13 / 5 -> 6
"""
Algo: stack
D.S.: stack

Solution:
remember there are -1

3 / (-2) = -1.5  -> // returns -2 while this question prefers -1 which is int( op1 / op2 )

Corner cases:
"""

class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # assume valid expression
        stack = []
        for tk in tokens:
            if tk not in ['+', '-', '*', '/']:
                stack.append(int(tk))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                val = None
                if tk == '+':
                    val = op1 + op2
                if tk == '-':
                    val = op1 - op2
                if tk == '*':
                    val = op1 * op2
                if tk == '/':

                    val = int(op1 / op2)
                stack.append(val)

        return stack[0]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
