# Definition of singly linked list node
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class LinkedList(object):
    def __init__(self, array=None):
        self.array = array
        self.length = None
        self.head = None
        if array:
            dummy = ListNode(-1)
            runner = dummy
            for i in self.array:
                node = ListNode(i)
                runner.next = node
                runner = node
            self.head = dummy.next

    def __repr__(self):
        if self.head is None:
            return "[]"
        arr = []
        runner = self.head
        while runner:
            arr.append(str(runner.val))
            runner = runner.next
        return '->'.join(arr)

    def setHead(self, node):
        self.head = node

    def getHead(self):
        return self.head

    def checkInput(self):
        return '->'.join([str(i) for i in self.array])



