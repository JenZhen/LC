#! /usr/local/bin/python3

# https://leetcode.com/problems/goat-latin/submissions/
# Example
# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
# The rules of Goat Latin are as follows:
#
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
#
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
#
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.
#
# Example 1:
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example 2:
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#
# Notes:
# S contains only uppercase, lowercase and spaces. Exactly one space between each word.
# 1 <= S.length <= 150.
"""
Algo:
D.S.:

Solution:
Time: O(n)
Space: O(n)
Corner cases:
"""

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return S
        word_list = S.split()
        res_list = []
        for i in range(len(word_list)):
            word = self._process_word(word_list[i], i + 1)
            res_list.append(word)
        return ' '.join(res_list)

    def _process_word(self, word, seq):
        # 注意要涵盖 大小写
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = ''
        if word[0] in VOWELS:
            res = word + 'ma'
        else:
            res = word[1:] + word[0] + 'ma'
        res += 'a' * seq
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
