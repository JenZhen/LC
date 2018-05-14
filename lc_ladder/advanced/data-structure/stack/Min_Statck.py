#! /usr/local/bin/python3

# https://lintcode.com/en/old/problem/min-stack/
# 实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
# 你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
# Example

"""
Algo:
D.S.: Stack

Solution:

Corner cases:
"""
class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minList = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if len(self.minList) == 0:
            self.minList.append(number)
        else:
            self.minList.append(min(self.minList[-1], number))
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.minList.pop()
        print("pop value: %s" %self.stack[-1])
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        print("Get min: %s" %self.minList[-1])
        return self.minList[-1]

# Test Cases
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.pop()   # return 1
    minStack.push(2)
    minStack.push(3)
    minStack.min()   # return 2
    minStack.push(1)
    minStack.min()   # return 1
