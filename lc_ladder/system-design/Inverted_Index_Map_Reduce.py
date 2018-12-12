#!/usr/local/bin/python3

# https://www.lintcode.com/problem/inverted-index-map-reduce/description?_from=ladder&&fromId=8
# Example 使用 map reduce 来实现一个倒排索引
# test input: [{"id":1,"content":"This is the content of document1"}, {"id":2,"content":"This is the content of document2"}]


"""
Solution:

Corner cases:
"""
'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        for word in value.content.split():
            yield word, value.id

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        # for all values of a key,
        # put in a set (remove dup), then a list, then sort the list
        yield key, sorted(list(set(values)))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
