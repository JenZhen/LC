#!/usr/local/bin/python3

# https://www.lintcode.com/problem/word-count-map-reduce/description?_from=ladder&&fromId=8
# solution: https://www.jiuzhang.com/solutions/word-count/#tag-highlight-lang-python
# Example

# 使用 map reduce 来计算单词频率
# https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html#Example%3A+WordCount+v1.0
#
# 样例
# chunk1: "Google Bye GoodBye Hadoop code"
# chunk2: "lintcode code Bye"
#
#
# Get MapReduce result:
#     Bye: 2
#     GoodBye: 1
#     Google: 1
#     Hadoop: 1
#     code: 2
#     lintcode: 1

"""
Solution:
注意1: 要用yield 的方式
注意2: line.split() VS line.split(" ")
default seperator is whitespace
" " 只按照一个空格来slice
“bye    bb": split() -> ["bye", "bb"], split(" ") -> ["bye", "  ", "bb"]

Corner cases:
"""

class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        for word in line.split():
            print(word)
            yield word, 1


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        yield key, sum(values)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
