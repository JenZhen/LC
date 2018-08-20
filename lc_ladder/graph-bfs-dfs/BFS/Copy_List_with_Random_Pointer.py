#! /usr/local/bin/python3

# https://lintcode.com/problem/copy-list-with-random-pointer/description
# Example

"""
Algo:
D.S.:

Solution:
Same with lc_ladder/linkedlist_array/Copy_List_with_Random_Pointer.py
1. 2 round of traverse
    - copy next node (save to hashmap)
    - copy the random node (if random is not None, check hashMap)
Time Complexity: O(2 * N)
Space Compelxity: O(N)

2. 1 round of travese (same as solution1)
    - Copy next node and random node at same time
    - for next and random check hashMap if exist then connects

3. 1 -> 2 -> 3 -> 4
   1 -> 1'-> 2 -> 2'-> 3 -> 3'-> 4- > 4', then split

Key parts:
- Iterate linked list, it's useful to have a dummy before head, then return dummy.next
- seperate head == None and else, handle head before iteration is easier

Corner cases:
"""

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution1:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None

        dummy = RandomListNode(0)
        p1 = head
        p2 = RandomListNode(p1.label)
        dummy.next = p2
        mapper = {}
        mapper[p1] = p2
        # copy nodes and next pointer
        while p1:
            if p1.next:
                p2.next = RandomListNode(p1.next.label)
                mapper[p1.next] = p2.next
            p1 = p1.next
            p2 = p2.next

        # reset p1, p2
        # copy random pointers
        p1 = head
        p2 = dummy.next
        while p1:
            if p1.random:
                p2.random = mapper[p1.random]
            p1 = p1.next
            p2 = p2.next
        return dummy.next

class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def copyNext(self, head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self, head):
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

    def splitList(self, head):
        # the most difficult part
        newHead = head.next
        while head:
            copyNode = head.next
            head.next = copyNode.next
            head = head.next
            if head:
                copyNode.next = head.next
        return newHead

# Test Cases
if __name__ == "__main__":
    solution = Solution()
