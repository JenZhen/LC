#! /usr/local/bin/python3

# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Example

"""
Algo: array + map
D.S.:

Solution:
Time: O(1)
Space: O(n)

注意：
处理delete 要记着更新MAP & ARRAY

Corner cases:
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {} #key: val, val, idx
        self.slot = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        # put in slot
        self.slot.append(val)
        # insert to map
        self.map[val] = len(self.slot) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        rm_idx = self.map[val]
        last_idx = len(self.slot) - 1
        last_val = self.slot[last_idx]
        self.slot[rm_idx] = last_val
        self.map[last_val] = rm_idx
        del self.map[val]
        self.slot.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # Note randint range is inclusive at both end
        random_idx = random.randint(0, len(self.slot) - 1)
        return self.slot[random_idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
