#!/usr/local/bin/python3

# https://www.lintcode.com/problem/standard-bloom-filter/description?_from=ladder&&fromId=8
# Example
# 实现一个标准型布隆过滤器, 支持一下方法:
# StandardBloomFilter(k), 构造方法, 你需要创建k个hash方法
# add(string). 往布隆过滤器中加入一个字符串.
# contains(string). 检查字符串是否在过滤器中
#
# 样例
# StandardBloomFilter(3)
# add("lint")
# add("code")
# contains("lint") // return true
# contains("world") // return false

"""
Solution:
要点：
1. 实现k个hashfunction的方式**
2. 用map来记录是否hash到。 只记录position是否被taken不用查是被那些word占用的
如果没有被占用，position就不在map中

Corner cases:
"""

import random
class HashFunction:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
    def hash(self, word):
        res = 0
        for c in word:
            res += self.seed * res + ord(c)
            res = res % self.cap
        return res

class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.hashFuncs = []
        self.slots = {} # key position, val: bool taken or not

        # init all hash functions
        for i in range(k):
            cap = random.randint(10000, 20000)
            seed = i * 2 + 3
            self.hashFuncs.append(HashFunction(cap, seed))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for hf in self.hashFuncs:
            position = hf.hash(word)
            self.slots[position] = True

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for hf in self.hashFuncs:
            if hf.hash(word) not in self.slots:
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
