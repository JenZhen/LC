#!/usr/local/bin/python3

# https://www.lintcode.com/problem/anagram-map-reduce/description?_from=ladder&&fromId=8
# Example
# 用Map来找乱序字符串的列表
#
# 样例
# 输入
# chunk1: "lint lint lnit ln"
# chunk2: "abc litn code deco"
# cunnk3: "ab ba cba"
# 输出
# ["ab","ba"]
# ["abc","cba"]
# ["code","deco"]
# ["lint","lint","litn","lnit"]
# ["ln"]

"""
Solution:

Corner cases:
"""

class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value' here
        # split line into list of words (using default whitespace as delimiter)
        for word in line.split():
            # key: word split into list of chars, sorted, then joined as a new string
            # value: original word
            yield "".join(sorted(list(word))), word


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, values
        # in case of requirement of no dup and sorted, use following method
        # yield key, sorted(list(set(values)))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
