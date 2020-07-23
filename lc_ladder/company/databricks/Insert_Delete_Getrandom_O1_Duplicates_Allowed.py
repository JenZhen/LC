#! /usr/local/bin/python3

# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Example
# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements.
# The probability of each element being returned is linearly related to the number of same value the collection contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);
#
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
"""
Algo: map, random
D.S.:

Solution:
Time: O(1)
Space: O(n)
注意很多很多细节
注意要考虑到 最后一个数 和要删除的数相同

Corner cases:
"""
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.val2idx = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        idx = len(self.arr)
        self.arr.append(val)
        if val not in self.val2idx:
            self.val2idx[val] = set()
        self.val2idx[val].add(idx)
        # 判断这val 是否重复的条件 有几个idx
        return len(self.val2idx) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.val2idx or not self.val2idx[val]:
            return False

        to_remove_idx, last_val = self.val2idx[val].pop(), self.arr[-1]
        self.arr[to_remove_idx] = last_val
        # 添加新的IDX
        self.val2idx[last_val].add(to_remove_idx)
        # 删除之前在最后的IDX
        self.val2idx[last_val].remove(len(self.arr) - 1)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rand_idx = random.randint(0, len(self.arr) - 1)
        return self.arr[rand_idx]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
