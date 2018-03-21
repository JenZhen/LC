#!/usr/bin/python

# http://lintcode.com/en/problem/rehashing/
# Example
# Given [null, 21->9->null, 14->null, null],
# return [null, 9->null, null, null, null, 21->null, 14->null,
# int hashcode(int key, int capacity) {
#     return key % capacity;
# }

"""
Algo:
D.S.:

Solution:

Corner cases:
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def hashFunc(self, key, cap):
        return key % cap

    def reHashTable(self, keys, cap):
        reHashTable = [None for i in range(cap)]
        for key in keys:
            hashVal = self.hashFunc(key, cap)
            if reHashTable[hashVal] is None:
                reHashTable[hashVal] = ListNode(key)
            else:
                ptr = reHashTable[hashVal]
                while ptr.next:
                    ptr = ptr.next
                ptr.next = ListNode(key)
        return reHashTable
    def rehashing(self, hashTable):
        # write your code here
        # get the size of hashTable
        keys = []
        cap = 0
        for head in hashTable:
            cap += 1
            pointer = head
            while pointer:
                keys.append(pointer.val)
                pointer = pointer.next
        if len(keys) >= cap / 10:
            # need to rehash
            cap = cap * 2
            return self.reHashTable(keys, cap)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
