#! /opt/bb/bin/python3

#######
# List
#######

# Features
# 1. Mutable
# 2. Index access
# 3. Linear complexity

# Examples
# - Create
myList = [1, 3, 2]
print(myList)
# - Swap
myList[1], myList[2] = myList[2], myList[1]
print(myList)

# - Access a range of data
tempList = myList[0 : 2] # include 0, not include 2
print(myList[-1]) # last element
print(myList[-1:]) # list contains only last element

# - Remove an element
ele = myList.pop(0) # return and pop the index 0 element

# - append an element 
myList.append(1) # append at the end of list

# - Sorting O(nlogn)
print("Before Sorting: %s " %myList)
myList.sort()
print("After Sorting: %s " %myList)

# - Join
# This only applies for list of strings, need to do type conversion
joinedList = \
    "->".join([str(ele) for ele in myList])
print("Joined list: %s" %joinedList)

# - Iteration
print("Iterate through list: ")
for ele in myList:
    print(ele)

print("\n")

########
# Queue
########

# Features: 
# - FIFO
# - Main functions: 1) size(), 2) isEmpty(), 3) push(x), 4) pop() (Raise exception on exhaustion)
#                   5) Fixed-size queue delete oldest-added on extra push(x)

# 1. Implmented using "List"
# queue = []                            // right most data are newly added
# queue.size()    - len(queue)
# queue.isEmpty() - len(queue) == 0
# queue.push(x)   - queue.append(x)
# queue.front()   - queue[0]            // Get the leftmost element of list, not delete it
# queue.pop()     - queue.pop(0)        // Pop the leftmost element of list, i.e. the oldest added
#                                       // Note that in python list.pop(x) remove and "return" the value, c++ return none
# Example
import sys
class Queue_List(object):
    def __init__(self, maxSize = sys.maxsize, dfltList = []):
        self.maxSize = maxSize
        self.queue_container = dfltList

    def _isFull(self):
        return len(self.queue_container) == self.maxSize

    def size(self):
        return len(self.queue_container)

    def isEmpty(self):
        return len(self.queue_container) == 0

    def push(self, value):
        # if queue is full, remove the oldest
        if self._isFull():
            self.queue_container.pop(0)
        self.queue_container.append(value)

    def front(self):
        return self.queue_container[0]

    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self.queue_container.pop(0)

    def __repr__(self):
        return "[" + ", ".join([str(ele) for ele in self.queue_container]) + "]"

# Test Usage
qList = Queue_List(4, [1, 2, 3])
print(qList) # [1, 2, 3]
qList.push(4)
print(qList) # [1, 2, 3, 4]
qList.push(5); qList.push(6)
print(qList) # [3, 4, 5, 6]

print(qList.front()) # 3
print(qList.pop())  # 3
qList.pop(); qList.pop(); qList.pop(); 
print(qList.isEmpty()) # True
# qList.pop(); # Exception

print("\n")

# 2. Using import queue (in python2.x import Queue)
# queue = queue.Queue(10)               // maxsize is 10
# queue.qsize()
# queue.empty()                         // similarly queue.full() return boolean
# queue.put(x)                          // if full and block=False, will raise queue.Full exception
#                                       // NOT kick out the oldeest element
# queue.get()                           // Pop the leftmost element of list, i.e. the oldest added
#                                       // Note that in python list.pop(x) remove and "return" the value, c++ return none
# Example
import queue # Queue is for FIFO Queue
q = queue.Queue(4)
q.put(1); q.put(2); q.put(3)
print("Queue size: %s" %q.qsize()) # 3
q.put(4)
print("Queue is full: %s" %q.full()) # True
try:
    q.put(5, block=False) # no block will raise queue.Full Exception
except queue.Full as exc:
    print("Queue is full.")
print("Get the oldest: %s. Queue size is now: %s" %(q.get(), q.qsize())) # 1, 3

print("\n")

# 3. Implmented using "collections.deque" -- two-ended deck
# Essentially a list 
# d = deque([], maxlen=3)               // Init an empty deck/list/queue with max length of 3
# len(d)                                // For queue.size(), queue.isEmpty()
# d.append(x)                           // For queue.push(x), add on the rightmost element, when full leftmost element will be removed
# d.pop()                               // Remove the "rightmost" element, can be used for stack(rightside side is new data)                       
# d.appendleft(x)                       
# d.popleft()                           // Remove the "leftmost" element, can be used for queue(leftside data is old data)
# Example
from collections import deque
d = deque([], maxlen=2)
d.append(1); d.append(2);
print(d) # [1, 2]
d.append(3)
print(d) # [2, 3]
print("Pop the oldest: %s. Now d is: %s" %(d.popleft(), d))

print("\n")

########
# Stack
########

# Features: 
# - LIFO
# - Main functions: 1) size(), 2) isEmpty(), 3) push(x), 4) pop() (Raise exception on exhaustion)
#                   5) Fixed-size stack delete oldest-added on extra push(x)

# 1. Implmented using "List"
# stack = []                            // right most data are newly added
# stack.size()    - len(stack)
# stack.isEmpty() - len(stack) == 0
# stack.push(x)   - stack.append(x)
# stack.top()     - stack[-1]           // Get the rightmost element of list, not delete it
# stack.pop()     - stack.pop(-1)       // Pop the leftmost element of list, i.e. the oldest added
#                                       // Note that in python list.pop(x) remove and "return" the value, c++ return none
# Example
class Stack_List(object):
    def __init__(self, maxSize = sys.maxsize, dfltList = []):
        self.maxSize = maxSize
        self.stack_container = dfltList

    def _isFull(self):
        return len(self.stack_container) == self.maxSize

    def size(self):
        return len(self.stack_container)

    def isEmpty(self):
        return len(self.stack_container) == 0

    def push(self, value):
        # if queue is full, remove the oldest
        if self._isFull():
            self.stack_container.pop(-1)
        self.stack_container.append(value)

    def top(self):
        return self.stack_container[-1]

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty.")
        return self.stack_container.pop(-1)

    def __repr__(self):
        return "[" + ", ".join([str(ele) for ele in self.stack_container]) + "]"

# Test Usage
sList = Stack_List(4, [1, 2, 3])
print(sList) # [1, 2, 3]
sList.push(4)
print(sList) # [1, 2, 3, 4]
sList.push(5); sList.push(6)
print(sList) # [1, 2, 3, 6]

print(sList.top()) # 6
print(sList.pop())  # 6
sList.pop(); sList.pop(); sList.pop(); 
print(sList.isEmpty()) # True
try:
    sList.pop()
except IndexError:
    print ("Too many pops")

print("\n")

# 2. Implmented using "collections.deque" -- two-ended deck
# Essentially a list 
# stack = []    - d = deque([], maxlen=3)           // Init an empty deck/list/stack with max length of 3
# stack.size()  - len(d) 
# stack.push(x) - d.append(x) or d.appendleft(x)    // When stack is full, append(x) will remove the leftmost element;
#                                                   // appendleft(x) will remove the rightmost elemnt. Inconsistent wiht stack feature
#                                                   // Need to manually check d.maxlen with len(d) to remove newest element
# stack.top()   - d[-1]
# stack.pop()   - d.pop()


######################
# Heap/Priority Queue
######################

# Documentation:
# https://docs.python.org/3.6/library/heapq.html
# Featuers: min/max heap
# Main functions 
# - heapify:
# - heappush: add a new value to a heap
# - heappop: return the min value in heap, and "will be removed"

###########
# Min Heap
###########
# Python module heapq implements a "MIN HEAP" using list

# Test Usage
import heapq
# init an empty list heap will be used as heap
heap = []
MAX_SIZE = 5 # Define a maxSize for this min heap
# Transform a list into a heap
heapq.heapify(heap)
for i in range(5):
    heapq.heappush(heap, i)
print("check heap size: %s" %len(heap))
print("Pop the minimun in heap: %s" %(heapq.heappop(heap)))
print("check heap size: %s" %len(heap))

for i in range(5, 10): # starting from 5 till 9
    if len(heap) == MAX_SIZE:
        popMin = heapq.heappop(heap)
        print("Reach max size, pop min: %s" %popMin)
    heapq.heappush(heap, i)
print("check heap size: %s" %len(heap))

print("\n")

###########
# Max Heap
###########
# Implment using module heapq, a "MIN HEAP".

class MaxHeap(object):
    def __init__(self, maxsize = None, dfltList = []):
        # Important: here dfltList * (-1) = [] multiplier won't work this way
        self.heap = [ele * -1 for ele in dfltList]
        heapq.heapify(self.heap)
        self.maxSize = maxsize

    def size(self):
        return len(self.heap)

    def isFull(self):
        return self.size() == self.maxSize

    def isEmpty(self):
        return self.size() == 0

    def heappush(self, value):
        if self.isFull():
            popped = (-1) * heapq.heappop(self.heap)
            print("Max heap full, pop %s first." % popped)
        heapq.heappush(self.heap, value * (-1))

    def heappop(self):
        if self.isEmpty():
            print("Cannot pop more, max heap is empty.")
            return
        return heapq.heappop(self.heap) * (-1)

    def repr(self):
        # present heap from largest to smallest
        eles = ", ".join([str(ele) for ele in self.heap])
        print("Diag heap: [%s]" %eles)


# Example
maxHeap1 = MaxHeap(5, [8, 9])
print("size: %s" %maxHeap1.size())
maxHeap1.repr()
for i in range(5):
    maxHeap1.heappush(i)
print("size %s" %maxHeap1.size())
maxHeap1.repr()

print("\n")

# Interview Usage
# 1. Given a stream of numbers, find the nth largest
#   -- min heap of size n, when heap full, pop the min away, keeping the large ones
#   eventually pop the top one, which is the nth largest (all larger ones are in heap)
#
# 2. Given a stream of numbers, find the nth smallest
#   -- max heap of size n + 1, when heap full, pop the largest, always keep n in heap
#   eventually pop the max in heap is the nth smallest (all smaller ones are in heap)

# Example for #1, min heap of size N
class NthLargest(object):
    def __init__(self, NthLargest):
        self.maxSize = NthLargest
        self.heap = []
        heapq.heapify(self.heap)

    def size(self):
        return len(self.heap)
    def isFull(self):
        return self.size() == self.maxSize
    def heappush(self, value):
        if self.isFull():
            heapq.heappop(self.heap)
        heapq.heappush(self.heap, value)
    def heappop(self):
        if self.size() == 0:
            print("Heap is empty. Cannot pop!")
            return
        return heapq.heappop(self.heap)
    def repr(self):
        eles = ", ".join([str(ele) for ele in self.heap])
        print("Diag heap: [%s]" %eles)

    def findNthLargest(self, arr):
        self.heap = []
        if not arr: 
            print("Invalid input!")
            return
        for ele in arr:
            self.heappush(ele)
        if self.size() < self.maxSize:
            # heap is not full, no nth Largest data
            self.repr()
            print("There is no Nth largest data.")
        else:
            self.repr()
            res = self.heappop()
            print("The Nth largest is: %s." %(res))

# Test
nLargest = NthLargest(5)
nLargest.findNthLargest([1,2,4,3,6,5]) #2
nLargest.findNthLargest([]) # error msg "invalid input"
nLargest.findNthLargest([1,4,3,2]) # error message "no nth largest data"

print("\n")

# Example for #2, max heap of size N + 1
class NthSmallest(object):
    def __init__(self, NthSmallest):
        self.maxSize = NthSmallest + 1
        self.heap = []
        heapq.heapify(self.heap)

    def size(self):
        return len(self.heap)
    def isFull(self):
        return self.size() == self.maxSize
    def heappush(self, value):
        # Before push, heap will never be full, at most has n elements
        heapq.heappush(self.heap, value * (-1))
        if self.isFull():
            return heapq.heappop(self.heap) * (-1)
    def heappop(self):
        if self.size() == 0:
            print("Heap is empty. Cannot pop!")
        return heapq.heappop(self.heap) * (-1)

    def repr(self):
        eles = ", ".join([str(ele) for ele in self.heap])
        print("Diag heap: [%s]" %eles)

    def findNthSmallest(self, arr):
        self.heap = []
        if not arr:
            print("Invalid input!")
            return
        for ele in arr:
            self.heappush(ele)
        if self.size() < self.maxSize - 1:
            print("There is no Nth smallest data.")
        else:
            res = self.heappop()
            print("The Nth largest is: %s." %(res))

# Test
nSmallest = NthSmallest(3)
nSmallest.findNthSmallest([1,2,4,3,6,5]) #3
nSmallest.findNthSmallest([]) # error msg "invalid input"
nSmallest.findNthSmallest([1,2]) # error message "no nth largest data"

print("\n")

# 3. Heap element could be tuple, This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked
