#! /usr/local/bin/python3

# https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/
# Example
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#
#
# Note:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.

"""
Algo: Comparison
D.S.:

Solution:
- Given order, convert to map, key: char, value: order for quick lookup
- compare two at one time:
    - 从左至右，直到不一样的字符，如果顺序正确，结束这对比较，去下一对比较
    - 如果不一样字符且顺序不对，直接返回false，结束算法
    - 一定要考虑一个corner case，如果一个长一个短，长的要在短的后面
Time: O(n * L) -- n is # of words to compare, L is length of words
Space: O(1)

Corner cases:
前缀一样 长短不一样的情况
“app", "application" True
"application", "app" False

"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not order:
            return False
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i

        for i in range(1, len(words)):
            front = words[i - 1] + " "
            back = words[i] + " "
            for j in range(min(len(front), len(back)) + 1):
                # 一定要先考虑 ’ ’ 的情况，否则order_map[' '] 是invalid key
                if front[j] == " ":
                    break
                if back[j] == " ":
                    return False
                if front[j] == back[j]:
                    continue
                if front[j] != back[j]:
                    if order_map[back[j]] > order_map[front[j]]:
                        break
                    else:
                        return False
        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_mp = {}
        for i in range(len(order)):
            ord_mp[order[i]] = i

        for i in range(1, len(words)):
            w1 = words[i - 1] + ' '
            w2 = words[i] + ' '
            for k in range(min(len(w1), len(w2))):
                c1, c2 = w1[k], w2[k]
                # 第一个条件，比较是否到词尾，要先考虑这个，因为‘ ’不在order_mp中
                # if w1到词尾，break 表示这一组成立
                if c1 == ' ': break
                # elif w2词尾，表示w1没有到词尾，返回错
                elif c2 == ' ': return False

                # 第二个条件，字符比较
                # 如果w1 比w2靠后，直接返回错
                # 如果w1 比w2靠后，这组成立，break 去查下一组词
                if ord_mp[c1] > ord_mp[c2]: return False
                elif ord_mp[c1] < ord_mp[c2]: break
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
