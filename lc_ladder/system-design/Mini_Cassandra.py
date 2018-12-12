#!/usr/local/bin/python3

# https://www.lintcode.com/problem/mini-cassandra/description?_from=ladder&&fromId=8
# Example
# Cassandra is a NoSQL database (a.k.a key-value storage). One individual data entry in cassandra constructed by 3 parts:
#
# row_key. a.k.a hash_key, partition key or sharding_key.
# column_key.
# value
# row_key is used to hash and can not support range query. let's simplify this to a string.
# column_key is sorted and support range query. let's simplify this to integer.
# value is a string. you can serialize any data into a string and store it in value.
#
# implement the following methods:
#
# insert(row_key, column_key, value)
# query(row_key, column_start, column_end) // return a list of entries
# 样例
# insert("google", 1, "haha")
# query("google", 0, 1)
# >> [（1, "haha")]

"""
Solution:

Corner cases:
"""

"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""

from collections import OrderedDict
class MiniCassandra:

    def __init__(self):
        # do intialization if necessary
        self.table = dict()

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        # write your code here
        if raw_key not in self.table:
            self.table[raw_key] = {}
        self.table[raw_key][column_key] = column_value
        self.table[raw_key] = dict(sorted(self.table[raw_key].items(), key=lambda x : x[0]))
    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        # write your code here
        ret = []
        if raw_key not in self.table:
            return ret
        cols = self.table[raw_key]
        for key, value in cols.items():
            if key >= column_start and key <= column_end:
                ret.append(Column(key, value))
        return ret

# Test Cases
if __name__ == "__main__":
    solution = Solution()
