#!/usr/local/bin/python3

# https://www.lintcode.com/problem/tiny-url/description?_from=ladder&&fromId=8
# Example
# 给出一个长网址，返回一个短网址。简单起见，忽视掉域名。
#
# 你需要实现两个方法：
#
# longToShort(url). 把一个长网址转换成一个短网址
# shortToLong(url). 把一个短网址转换成一个以http://tiny.url/开头的长网址
# 你可以任意设计算法，评测只关心两件事：
#
# 1、短网址的key的长度应该等于6 （不算域名和反斜杠）。 可以使用的字符只有 [a-zA-Z0-9]. 比如: abcD9E
# 2. 任意两个长的url不会对应成同一个短url，反之亦然。
#
# 样例
# 给定 url = http://www.lintcode.com/faq/?id=10, 给出下列答案（或者其它类似的）：
#
# short_url = longToShort(url) // 可能返回 http://tiny.url/abcD9E
# long_url = shortToLong(short_url) // 返回 http://www.lintcode.com/faq/?id=10
# 你返回的应该是以 http://tiny.url/开头的key为6个字符的唯一的短网址. 比如 "http://tiny.url/abcD9E" 或者其它的.

"""
Solution:

Corner cases:
"""

CH_LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
SHORT_URL_PREFIX = "http://tiny.url/"
SCALE = 56800235584L
class TinyUrl:
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def __init__(self):
        # mapping is the table for short/long url mapping
        # key: autoincreased key
        # vaue: longUrl
        self.mapping = {}

    def idToShortKey(self, id):
        s = ""
        while id > 0:
            s = CH_LIST[id % 62] + s
            id /= 62
        while len(s) < 6:
            s = 'a' + s
        return s

    def getShortKey(self, url):
        return url[-6:]

    def longToShort(self, url):
        # write your code here
        id = 0
        for a in url:
            id = (id * 256 + ord(a)) % SCALE

        while id in self.mapping and self.mapping[id] != url:
            id = (id + 1) % SCALE
        # ans is a new key or ans-url pair already in mapping
        self.mapping[id] = url
        return SHORT_URL_PREFIX + self.idToShortKey(id)

    def shortkeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        # write your code here
        short_key = self.getShortKey(url)
        return self.mapping[self.shortkeyToid(short_key)]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
