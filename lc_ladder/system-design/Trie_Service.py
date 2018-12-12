#!/usr/local/bin/python3

# https://www.lintcode.com/problem/trie-service/description?_from=ladder&&fromId=8
# Example
# 通过<字符串，值>的集合来建立树结构，每个接单保存前10大的数值。
#
# 样例
# 给出一个< 字符串,值 >的集合
#
# <"abc", 2>
# <"ac", 4>
# <"ab", 9>
# 返回 <a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>> ，代表一下的树结构：
#
#          Root
#          /
#        a(9,4,2)
#       /    \
#     b(9,2) c(4)
#    /
#  c(2)
"""
Solution:

Corner cases:
"""

"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            self.addFreq(cur.top10, frequency)

    def addFreq(self, list, freq):
        list.append(freq)
        list.sort(reverse=True)
        if len(list) > 10:
            list.pop()




# Test Cases
if __name__ == "__main__":
    solution = Solution()
