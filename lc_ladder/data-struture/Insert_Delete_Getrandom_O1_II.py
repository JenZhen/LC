#!/usr/local/bin/python3

# https://www.lintcode.com/problem/insert-delete-getrandom-o1-duplicates-allowed/description
# Example
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
# Notice
# Duplicate elements are allowed.
#
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

"""
Algo:
D.S.:

Solution:
Important to know how to delete: swap with the last element.
In the map/dict, val should be set not list.
To init an empty set, use set() not {}, {} init an empty dict

Corner cases:
"""

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.list.append(val)
        if val not in self.pool:
            self.pool[val] = {len(self.list) - 1}
            return True
        else:
            self.pool[val].add(len(self.list) - 1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pool:
            return False
        lastVal = self.list.pop()
        lastIdx = len(self.list)
        self.pool[lastVal].remove(lastIdx)
        if val != lastVal:
            # swap place for val and lastVal
            valIdx = self.pool[val].pop()
            self.list[valIdx] = lastVal
            self.pool[lastVal].add(valIdx)
        if len(self.pool[val]) == 0:
            del self.pool[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        from random import randint
        return self.list[randint(0, len(self.list) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
