#!/usr/local/bin/python3

# https://www.lintcode.com/problem/memcache/description?_from=ladder&&fromId=8
# Example

# 实现下列几个方法：
# 1.get(curtTime, key). 得到key的值，如果不存在返回2147483647
# 2.set(curtTime, key, value, ttl). 设置一个pair(key,value)，有效期从curtTime到curtTime + ttl -1 , 如果ttl为0，则一直存在
# 3.delete(curtTime, key). 删除这个key
# 4.incr(curtTime, key, delta). 给key的value加上delta，并且返回 如果不存在返回 2147483647。
# 5.decr(curtTime, key, delta). 给key的value减去delta，并且返回 如果不存在返回 2147483647。
#
# 样例
# get(1, 0)
# >> 2147483647
# set(2, 1, 1, 2)
# get(3, 1)
# >> 1
# get(4, 1)
# >> 2147483647
# incr(5, 1, 1)
# >> 2147483647
# set(6, 1, 3, 0)
# incr(7, 1, 1)
# >> 4
# decr(8, 1, 1)
# >> 3
# get(9, 1)
# >> 3
# delete(10, 1)
# get(11, 1)
# >> 2147483647
# incr(12, 1, 1)
# >> 2147483647
# 说明
# Actually, a real memcache server will evict keys if memory is not sufficient, and it also supports variety of value types like string and integer. In our case, let's make it simple, we can assume that we have enough memory and all of the values are integers.
#
# Search "LRU" & "LFU" on google to get more information about how memcache evict data.
#
# Try the following problem to learn LRU cache:
# http://www.lintcode.com/problem/lru-cache


"""
Solution:

Corner cases:
"""

MAX_INT = 2147483647

class Value:
    def __init__(self, value, time):
        self._value = value
        self._expireAt = time

class Memcache:
    def __init__(self):
        # do intialization if necessary
        # in dict, key, value is type of Value, containing
        self.map = dict()

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        # write your code here
        if key not in self.map:
            return MAX_INT
        value = self.map[key]
        if value._expireAt == -1 or curtTime <= value._expireAt:
            return value._value
        else:
            # if expired, return not-found
            return MAX_INT
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        # write your code here
        if ttl:
            value = Value(value, curtTime + ttl - 1)
        else:
            value = Value(value, -1)
        self.map[key] = value

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        # write your code here
        if key not in self.map:
            return
        else:
            del self.map[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        # write your code here
        if self.get(curtTime, key) == MAX_INT:
            return MAX_INT
        else:
            self.map[key]._value += delta
            return self.map[key]._value
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        # write your code here
        if key not in self.map:
            return MAX_INT
        else:
            self.map[key]._value -= delta
            return self.map[key]._value 

# Test Cases
if __name__ == "__main__":
    solution = Solution()
