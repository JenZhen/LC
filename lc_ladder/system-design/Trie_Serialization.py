#!/usr/local/bin/python3

# https://www.lintcode.com/problem/trie-serialization/description?_from=ladder&&fromId=8
# Example
# 给你一棵字典树，设计一种序列化的方式，并且同时要能够设计对应的展开方法。
#
# 样例
# str = serialize(old_trie)
# >> str can be anything to represent a trie
# new_trie = deserialize(str)
# >> new_trie should have the same structure and values with old_trie
# 一种样例: trie <a<b<e<>>c<>d<f<>>>>, 表示如下结构
#
#      root
#       /
#      a
#    / | \
#   b  c  d
#  /       \
# e         f
# 注意事项
# 不需要按照样例的方法， 设计自己的方法

"""
Solution:
DFS 序列化trie树
serialize: DFS recursive 遍历一个图
deserialize: DFS iteration 解开一个图

Corner cases:
注意 这个题目中 TrieNode 的定义方式，NODE的值存在父亲节点的map key, 自己不知道

"""

"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""


class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # DFS serialize
        if not root:
            return ""

        data = ""
        for key, node in root.children.items():
            data += key + self.serialize(node)
        return "<" + data + ">"

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        # assume input data format is legit
        if not data:
            return None
        root = TrieNode()
        cur = root
        stack = []
        for c in data:
            if c == "<":
                stack.append(cur)
            elif c == ">":
                stack.pop()
            else:
                curParent = stack[-1]
                cur = TrieNode()
                curParent.children[c] = cur
        return root

# Test Cases
if __name__ == "__main__":
    solution = Solution()
