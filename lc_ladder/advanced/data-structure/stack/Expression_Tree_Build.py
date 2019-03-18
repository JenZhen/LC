#! /usr/local/bin/python3

# https://www.lintcode.com/problem/expression-tree-build/description
# Example
# 表达树是一个二叉树的结构，用于衡量特定的表达。所有表达树的叶子都有一个数字字符串值。而所有表达树的非叶子都有另一个操作字符串值。
#
# 给定一个表达数组，请构造该表达的表达树，并返回该表达树的根。
#
# 样例
# 对于 (2*6-(23+7)/(1+2)) 的表达（可表示为 ["2" "*" "6" "-" "(" "23" "+" "7" ")" "/" "(" "1" "+" "2" ")"]).
# 其表达树如下：
#
#                  [ - ]
#              /          \
#         [ * ]              [ / ]
#       /     \           /         \
#     [ 2 ]  [ 6 ]      [ + ]        [ + ]
#                      /    \       /      \
#                    [ 23 ][ 7 ] [ 1 ]   [ 2 ] .
# 在构造该表达树后，你只需返回根节点[-]。
#
# 说明
# 什么是表达树？详见wiki百科：
# 表达树

"""
Algo:
D.S.: Tree, Stack, Ascending stack

Solution:
# TODO:
观察example，可以看出所有叶节点都为数字。如果给每个元素赋予一个优先级，和 ／ 为2， ＋ 和 － 为1， 数字为极大值，然后规定优先级越大的越在下，越小的越在上。这样，这道题就转化为构建*Min Tree，和之前的Max Tree做法类似，只是这里维持的是一个递增栈。同时，当遇见“（”时，提高优先级，遇见“）”时，降低优先级。遍历数组，给每个新来的元素赋予一个val值用以比较优先级。 * 和 ／ 为2， ＋ 和 － 为1， 数字为极大值。此时看栈顶元素（若栈为空则直接加入）。为了维持一个递增栈，若栈顶元素比新来元素val大（或相等），则出栈；若栈顶元素比新来元素val小，则break。若2中栈顶元素出栈，此时若栈为空，则将出栈元素作为新来元素的左节点，并将新来元素加入栈中；若不为空，看新栈顶元素，若新栈顶元素比新来元素val小，则将出栈元素作为新来元素的左孩子，并将新来元素加入栈中；若新栈顶元素比新来元素val大（或相等），则将出栈元素作为新栈顶元素的右节点，重复2-3，直到栈为空或者栈顶元素比新来元素要小，将新来元素加入栈中。tips：在遍历万整个数组后，多加一个值，将其val赋值为极小，这样所有元素都会出栈并构建成完整的树。

作者：程风破浪会有时
链接：https://www.jianshu.com/p/22990628d74e
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

Corner cases:
"""


# Definition of ExpressionTreeNode:
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None

class MyTreeNode:
    def __init__(self, val, s):
        self.left = None
        self.right = None
        self.val = val # priority
        self.exp_node = ExpressionTreeNode(s)

import sys
class Solution:
    """
    @param: expression: A string array
    @return: The root of expression tree
    """
    def build(self, expression):
        # write your code here
        root = self.create_tree(expression)
        return self.copy_tree(root)

    def create_tree(self, expression):
        stack = []
        priority = 0
        for i in range(len(expression)):
            print("consider %s" %expression[i])
            if i != len(expression):
                if expression[i] == '(':
                    if priority != sys.maxsize:
                        priority += 10
                    continue
                elif expression[i] == ')':
                    if priority != sys.maxsize:
                        priority -= 10
                    continue
                val = self.get_val(expression[i], priority)

            node = MyTreeNode(val, expression[i])
            while stack and val <= stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
            self.printStack(stack)
        if not stack:
            return None
        return stack[0]

    def printStack(self, stack):
        st = [ele.val for ele in stack]
        print("stack: %s" %repr(st))

    def get_val(self, a, priority):
        if a == '+' or a == '-':
            if priority == sys.maxsize:
                return priority
            return 1 + priority
        if a == '*' or a == '/':
            if priority == sys.maxsize:
                return priority
            return 2 + priority
        return sys.maxsize

    def copy_tree(self, root):
        if not root:
            return None
        root.exp_node.left = self.copy_tree(root.left)
        root.exp_node.right = self.copy_tree(root.right)
        return root.exp_node

# Test Cases
if __name__ == "__main__":
    testcases = [
        {
            "expression": ["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"]
        },
    ]
    solution = Solution()
    for t in testcases:
        expression = t["expression"]
        solution.build(expression)
