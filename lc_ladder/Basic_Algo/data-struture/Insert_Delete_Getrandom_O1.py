#!/usr/local/bin/python3

# https://www.lintcode.com/problem/insert-delete-getrandom-o1/description
# Example
# Design a data structure that supports all following operations in average O(1) time.
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

"""
Algo:
D.S.: list and set

Solution:
important to know how to delete: swap with the last element

Corner cases:
"""

class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        # key: val, val: idx in array
        self.pool = {}
        self.list = []

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.pool:
            return False
        self.list.append(val)
        self.pool[val] = len(self.list) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.pool:
            return False
        idx = self.pool[val]
        lastEle = self.list[-1]
        self.list[idx] = lastEle
        self.pool[lastEle] = idx
        self.list.pop()
        del self.pool[val]
        return True
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        from random import randint
        return self.list[randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
