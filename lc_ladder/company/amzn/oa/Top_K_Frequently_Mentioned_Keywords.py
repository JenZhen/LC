#! /usr/local/bin/python3

# https://www.lintcode.com/problem/top-k-frequently-mentioned-keywords/my-submissions
# Example
# 给定一个评论列表reviews，一个关键字列表 keywords 以及一个整数k。
# 找出在不同评论中出现次数最多的前k个关键词，这k个关键词按照出现次数的由多到少来排序。
# 字符串不区分大小写，如果关键字在不同评论中出现的次数相等，请按字母顺序从小到大排序。
#
# 样例
# 示例 1:
# 输入:
# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]
# 输出:
# ["anacell", "betacellular"]
# 解释: "anacell" 在2个不同的评论，"betacellular" 在1个评论中出现。
# 示例 2:
# 输入:
# k = 2
# keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
# reviews = [
#   "I love anacell Best services; Best services provided by anacell",
#   "betacellular has great services",
#   "deltacellular provides much better services than betacellular",
#   "cetracular is worse than anacell",
#   "Betacellular is better than deltacellular.",
# ]
# 输出:
# ["betacellular", "anacell"]
# 解释: "betacellular" 在3个不同的评论中出现了，"anacell" 以及 "deltacellular" 在两个不同的评论中出现了，但是"anacell" 在字典序中最小。
# 注意事项
# K可能大于keywords的长度，那就输出keywords数量的答案
# keywords 的列表长度范围是: [1, 100]
# reviews 的列表长度范围是: [1: 1000]
# kewords[i] 由小写字母组成
# reviews[i] 由大小写字母以及标点符号: [ "[", "\", "!", "?", ",", ";" , ".", "]", " "] 组成

"""
Algo: Heap, string manipulation
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param K: a integer
    @param keywords: a list of string
    @param reviews: a list of string
    @return: return the top k keywords list
    """
    def TopkKeywords(self, K, keywords, reviews):
        from heapq import heappush, heappop, heapify
        symbols = set(["[", "\\", "!", "?", ",", ";", ".", "]"])
        cnt_map = {}
        keywords = set(keywords)
        for r in reviews:
            word_set = set()
            for c in r:
                if c in symbols:
                    r.replace(c, '')
            words = r.split(' ')
            print(words)
            for w in words:
                w = w.lower()
                if w not in keywords:
                    continue
                word_set.add(w)
            for w in word_set:
                if w not in cnt_map:
                    cnt_map[w] = 0
                cnt_map[w] += 1
        # print(cnt_map)
        h = []
        for w, freq in cnt_map.items():
            heappush(h, (-freq, w))
        res = []
        for _ in range(K):
            if len(h) == 0: break
            res.append(heappop(h)[1])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
