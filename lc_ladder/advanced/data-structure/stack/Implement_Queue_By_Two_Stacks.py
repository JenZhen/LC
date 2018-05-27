#! /usr/local/bin/python3

# https://www.lintcode.com/problem/implement-queue-by-two-stacks/description
# Example

"""
Algo:
D.S.: stack

Solution:
Time O(N)
Similar "/data-structure/Impment_Stack_by_Two_Queue.py"

Corner cases:
"""
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = [] # use as queue
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        self.from2To1()
        return res

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        res = self.stack2[-1]
        self.from2To1()
        return res

    def from2To1(self):
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())



# Test Cases
if __name__ == "__main__":
    s = Solution()
