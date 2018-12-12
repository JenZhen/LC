#!/usr/local/bin/python3

# https://www.lintcode.com/problem/counting-bloom-filter/description?_from=ladder&&fromId=8
# Example
# 实现一个计数型布隆过滤器, 支持一下方法:
# add(string). 往布隆过滤器中加入一个字符串.
# contains(string). 检查一个字符串是否在布隆过滤器中.
# remove(string). 从布隆计数器中删除一个字符串.
#
# 样例
# CountingBloomFilter(3)
# add("lint")
# add("code")
# contains("lint") // return true
# remove("lint")
# contains("lint") // return false

"""
Solution:
和standard bloom filter 类似，改变在slot的value 记录次数
注意点：
对于remove操作，如果remove了一个不曾被加进去的值，应该如何操作
remove1: 发现hash value 不在slotmap中，要revert之前的加入操作
    缺点，slotmap只是计数，即使数值大于1也不能确定这个值之前是被加进去的（可能是别的值的hash value)
remove2： 不管这个数是不是之前加进去过，如果key存在就加-1，其他情况一律减1
Lintcode 2中方法都能过

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
            res += res * self.seed + ord(c)
            res %= self.cap
        return res

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.hashFuncs = []
        self.slots = {} # key: position, val: int counters

        # init all k functions
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
            if position not in self.slots:
                self.slots[position] = 1
            else:
                self.slots[position] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove_I(self, word):
        for hf in self.hashFuncs:
            position = hf.hash(word)
            if position not in self.slots: #remove a word not added before
                # revert previous operation
                for f in self.hashFuncs:
                    pos = f.hash(word)
                    if pos in self.slots:
                        self.slots[pos] += 1
                    else:
                        break # break inner loop
                break # break outer loop
            self.slots[position] -= 1

    def remove_II(self, word):
        for hf in self.hashFuncs:
            position = hf.hash(word)
            if position not in self.slots:
                self.slots[position] = -1
            else:
                self.slots[position] -= 1
    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for hf in self.hashFuncs:
            position = hf.hash(word)
            if position not in self.slots or self.slots[position] <= 0:
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
