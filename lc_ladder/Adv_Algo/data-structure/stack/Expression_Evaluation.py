#! /usr/local/bin/python3

# https://www.lintcode.com/problem/expression-evaluation/description?_from=ladder&&fromId=4
# Example
# 给一个用字符串表示的表达式数组，求出这个表达式的值。
#
# 样例
# 对于表达式 (2*6-(23+7)/(1+2)), 对应的数组为：
#
# [
#   "2", "*", "6", "-", "(",
#   "23", "+", "7", ")", "/",
#   "(", "1", "+", "2", ")"
# ],
# 其值为 2
#
# 注意事项
# 表达式只包含整数, +, -, *, /, (, ).

"""
Algo:
D.S.: 单调栈

Solution:
# TODO:
本题需要采用stack的方法来做，两个stack，一个存数字一个存符号。

遇到数字的时候，将数字入栈；

如果遇到符号，有几种情况：

1.当前符号比上一个符号优先级高，比如* 高于+，那么直接进栈

2.当前符号低于上一个，那么就要把所有已经在stack里面优先于当前符号的全算完，再推进当前符号

3.当前符号是“（”，直接push

4.当前符号是“）”，就要把所有“（”以前的符号全部算完

最终的栈顶即为答案。


Corner cases:
"""

class Solution:
    """
    @param expression: a list of strings
    @return: an integer
    """
    def evaluateExpression(self, expression):
        # write your code here
        if len(expression) == 0:
            return 0
        if len(expression) == 1:
            return int(expression[0])

        blocks = self.getBlocks(['+', '-'], expression)
        if len(blocks) == 1:
            blocks = self.getBlocks(['*', '/'], expression)
            if len(blocks) == 1:  # must be ( ... )
                return self.evaluateExpression(expression[1:-1])

        sum = 0
        for opt, exp in blocks:
            val = self.evaluateExpression(exp)
            if opt is None:
                sum = val
            elif opt == '+':
                sum += val
            elif opt == '-':
                sum -= val
            elif opt == '*':
                sum *= val
            elif opt == '/':
                sum //= val
        return sum

    def getBlocks(self, delims, expression):
        paren, lastIndex = 0, 0
        blocks = []
        lastOperator = None
        for index, e in enumerate(expression):
            if e == '(':
                paren += 1
            elif e == ')':
                paren -= 1
            elif e in delims and paren == 0:
                blocks.append((lastOperator, expression[lastIndex: index]))
                lastIndex = index + 1
                lastOperator = e
        blocks.append((lastOperator, expression[lastIndex: len(expression)]))
        return blocks
# Test Cases
if __name__ == "__main__":
    solution = Solution()
