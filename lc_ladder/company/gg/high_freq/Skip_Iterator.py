#! /usr/local/bin/python3

# Requirement
# Example
# 实现一个iterator class, input是正常的iterator, 这个class可以实现hasNext(), next(), skip(element), skip(element)会跳过正常iterator里next
# occurence of the given element。如果skip call n times, 就跳过下面 n个given element，iterator里的elements可以有重复。这题看起来简单其实还是有些corner case的

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class SkipIterator1:
    def __init__(self, arr):
        self.it = 0
        self.arr = arr
        self.len = len(arr)
        # key: skip value, val: number of skip
        self.skip_map = {}

    def hasNext():
        # has main logic
        while not self._check_valid() and self.it < self.len:
            self.it += 1
        if self.it < self.len:
            return True
        else:
            return False

    def next():
        if self.hasNext():
            return self.arr[self.it]
        else:
            raise "No valid value"

    def skip(self, num):
        if num not self.skip_map:
            self.skip_map[num] = 0
        self.skip_map[num] += 1

    def _check_valid(self):
        key = self.arr[self.it]
        if key not in self.skip_map:
            return True
        else:
            self.skip_map[key] -= 1
            if self.skip_map[key] == 0:
                del self.skip_map[key]
            return False

# Test Cases
if __name__ == "__main__":
    s1 = Solution1()
