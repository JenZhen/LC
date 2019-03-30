#! /usr/local/bin/python3

# https://www.lintcode.com/problem/word-ladder-ii/description
# Example
# 给出两个单词（start和end）和一个字典，找出所有从start到end的最短转换序列。
#
# 变换规则如下：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
# 样例
# 给出数据如下：
#
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
#
# 返回
#
# [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
# ]
# 注意事项
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution1:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        distance = {} # key: node, val: distance to end, end to end is 0
        self.bfs(end, start, distance, dict)
        path = [start]
        res = []
        self.dfs(start, end, distance, dict, path, res)
        return res

    def bfs(self, from_word, to_word, distance, dict):
        from collections import deque
        distance[from_word] = 0
        q = deque([from_word])
        while q:
            cur_word = q.popleft()
            next_words = self._get_next_words(cur_word, dict)
            for word in next_words:
                if word not in distance:
                    # same check as if word not visited
                    distance[word] = distance[cur_word] + 1
                    q.append(word)

    def dfs(self, from_word, to_word, distance, dict, path, res):
        if from_word == to_word:
            res.append(path[:])
            return
        for word in self._get_next_words(from_word, dict):
            if distance[word] < distance[from_word]:
                path.append(word)
                self.dfs(word, to_word, distance, dict, path, res)
                path.pop()

    def _get_next_words(self, word, dict):
        res = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                # str is not mutable, cannot modify on word
                next_word = word[:i] + char + word[i + 1:]
                if next_word in dict:
                    res.append(next_word)
        return res

class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        distance = {} # key: node, val: distance to end, end to end is 0
        self.bfs(end, start, distance, dict)
        path = [start]
        res = []
        self.dfs(start, end, distance, dict, path, res)
        return res

    def bfs(self, from_word, to_word, distance, dict):
        from collections import deque
        distance[from_word] = 0
        q = deque([from_word])
        while q:
            cur_word = q.popleft()
            next_words = self._get_next_words(cur_word, dict)
            for word in next_words:
                if word not in distance:
                    # same check as if word not visited
                    distance[word] = distance[cur_word] + 1
                    q.append(word)
                if to_word in distance and distance[word] > distance[to_word]:
                    return

    def dfs(self, from_word, to_word, distance, dict, path, res):
        if from_word == to_word:
            res.append(path[:])
            return
        for word in self._get_next_words(from_word, dict):
            if word in distance and distance[word] < distance[from_word]:
                path.append(word)
                self.dfs(word, to_word, distance, dict, path, res)
                path.pop()

    def _get_next_words(self, word, dict):
        res = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                # str is not mutable, cannot modify on word
                next_word = word[:i] + char + word[i + 1:]
                if next_word in dict:
                    res.append(next_word)
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
