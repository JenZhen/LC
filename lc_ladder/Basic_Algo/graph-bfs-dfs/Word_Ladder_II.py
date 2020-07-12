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
Time: O(n * 26 ^ l), n -- len(words), l -- length of word
Space: O(n + k * l)
Corner cases:
"""

class Solution:
    def findLadders(self, start: str, end: str, words: List[str]) -> List[List[str]]:
        res = []

        # key: vague_word(h*g), val: [origin_word_idx] (hog_idx)
        neigh = defaultdict(list)

        for idx, word in enumerate(words):
            for k in range(len(word)):
                x = word[:k] + '*' + word[k+1:]
                neigh[x].append(idx)

        # key: original_word(hig), val: [parent] (hog) change from hog to hig
        parents = defaultdict(list)
        self.bfs(start, end, neigh, words, parents)

        path = [end]
        # earch from end back to start, then reverse
        self.dfs(parents, res, path, start, end)
        for li in res:
            li.reverse()
        return res

    def bfs(self, start, end, neigh, words, parents):
        q = deque()
        q.append((start, 1))
        visited = defaultdict(tuple)
        res = 0
        while(q):
            word, step = q.popleft()
            for idx, char in enumerate(word):
                vague_word = word[:idx] + '*' + word[idx + 1:]
                for i in neigh[vague_word]:
                    # print('nei: ', neigh[vague_word])
                    if words[i] not in visited:
                        # mark as visited and add step to it, enqueue
                        visited[words[i]] = (True, step + 1)
                        q.append((words[i], step + 1))
                    # add a new parent make sure it's not parent to itself
                    if visited[words[i]][1] == step + 1 and words[i] != word:
                        parents[words[i]].append(word)

    def dfs(self, parents, res, path, start, curr_word):
        if curr_word == start:
            res.append(path[:])
            return
        for parent_word in parents[curr_word]:
            path.append(parent_word)
            self.dfs(parents, res, path, start, parent_word)
            path.pop()
# Test Cases
if __name__ == "__main__":
    solution = Solution()
