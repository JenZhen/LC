#! /usr/local/bin/python3

# https://leetcode.com/problems/design-search-autocomplete-system/
# Example
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
#
# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# Your job is to implement the following functions:
#
# The constructor function:
#
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.
#
# Now, the user wants to input a new sentence. The following function will provide the next character the user types:
#
# List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
#
#
# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
#
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
#
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".
#
# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".
#
# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
#
#
# Note:
#
# The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
# Please use double-quote instead of single-quote when you write test cases even for a character input.
# Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.

"""
Algo: DFS + Trie
D.S.:
和TYPE AHEAD 一样
重要！！！非常好的题
Solution:
- ADD 用trie 树， 在词尾节点记录频率
- GET 先循环找PREFIX， 在从prefix 去DFS找所有的词， 记录频率 并排序

技巧
1. 处理 “ ” 当做第27个字符

Corner cases:
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 27
        self.freq = 0

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add_freq(self, word, freq):
        cur = self.root
        for c in word:
            pos = 26 if (c == " ") else (ord(c) - ord("a"))
            if cur.children[pos] is None:
                cur.children[pos] = TrieNode(c)
            cur = cur.children[pos]
        cur.freq += freq

    def get_top_freq(self, prefix, top_k):
        res = [] # list of tuple [(freq, word)]
        cur = self.root
        for c in prefix:
            pos = 26 if (c == " ") else (ord(c) - ord("a"))
            if cur.children[pos] is None:
                return []
            cur = cur.children[pos]
        self.dfs(prefix, cur, res)
        print(res)
        res.sort(key = lambda x: (-x[0], x[1]))
        ans = []
        for i in range(min(top_k, len(res))):
            ans.append(res[i][1])
        return ans

    def dfs(self, prefix, node, res):
        if node.freq > 0:
            res.append((node.freq, prefix))
        for i in range(27):
            if node.children[i] is not None:
                if i == 26:
                    self.dfs(prefix + " ", node.children[26], res)
                else:
                    char = chr(ord("a") + i)
                    self.dfs(prefix + char, node.children[i], res)         


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.TOP_K = 3
        self.cur_prefix = ""
        self.trie = TrieTree()
        for i in range(len(sentences)):
            self.trie.add_freq(sentences[i], times[i])


    def input(self, c: str) -> List[str]:
        if c == "#":
            # 查找结束后 添加一个新的词频， 并将cur_prefix归“”
            self.trie.add_freq(self.cur_prefix, 1)
            self.cur_prefix = ""
        else:
            self.cur_prefix += c
            return self.trie.get_top_freq(self.cur_prefix, self.TOP_K)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# Test Cases
if __name__ == "__main__":
    s = Solution()
