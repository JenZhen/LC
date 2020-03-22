#!/usr/bin/python

# http://www.jiuzhang.com/solution/implement-stack-by-two-queues/#tag-highlight-lang-python
# Example

"""
Algo: queue and stack
D.S.:

Solution:
in python3 use library queue.Queue() for FIFO queue

Corner cases:
"""

import queue
# in python2 this module is called
# import Queue
class Stack(object):
    def __init__(self):
        self.q1 = queue.Queue() # queue to mainly hold data
        self.q2 = queue.Queue() # queue to tmp hold data when top/pop

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        poppedItem = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        poppedItem = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return poppedItem

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.q1.empty()

# Test Cases
if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.pop()
    print(s.top()) # 3
    print(s.isEmpty())
