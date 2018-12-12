#!/usr/local/bin/python3

# https://www.lintcode.com/problem/inverted-index/description?_from=ladder&&fromId=8
# Example
# 创建给定文档的反向索引
#
# 样例
# 给出一个包括id与内容的文档list(我们提供了document类)
#
# [
#   {
#     "id": 1,
#     "content": "This is the content of document 1 it is very short"
#   },
#   {
#     "id": 2,
#     "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
#   },
# ]
# 返回一个反向索引(hashmap的key是单词, value是文档的id).
#
# {
#    "This": [1, 2],
#    "is": [1, 2],
#    ...
# }
# 注意事项
# 确保数据不包含标点符号


"""
Solution:
暴力直白的解法

Corner cases:
如果有如下情况
keyword: [1,2,3,3]
输出
keyword: {1,2,3} # set 的形式
"""

'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        res = {} # key string, value list of id
        for doc in docs:
            id = doc.id
            words = self.splitString(doc.content)
            for w in words:
                if w not in res:
                    res[w] = [id]
                else:
                    res[w].append(id)
        return res

    def splitString(self, content):
        res = set()
        tmpStr = ""
        for c in content:
            if c == " ":
                if tmpStr != "":
                    res.add(tmpStr)
                    tmpStr = ""
            else:
                tmpStr += c
        if tmpStr != "":
            res.add(tmpStr)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
