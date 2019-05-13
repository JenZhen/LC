#! /usr/local/bin/python3

# https://leetcode.com/problems/guess-the-word/
# Example
# This problem is an interactive problem new to the LeetCode platform.
#
# We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.
#
# You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.
#
# This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.
#
# For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.
#
# Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.
#
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
#
# Explanation:
#
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
#
# We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
# Note:  Any solutions that attempt to circumvent the judge will result in disqualification.

"""
Algo:
D.S.: map

Solution:


Corner cases:
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        dist_map = {}
        for i in range(len(wordlist)):
            # Note: j 要从i开始选取包括自己和自己比较的情况
            # 如果一开始选中secret word要能找到
            for j in range(i, len(wordlist)):
                w1 = wordlist[i]
                w2 = wordlist[j]
                diff = self.diff(w1, w2)
                if w1 not in dist_map:
                    dist_map[w1] = {}
                if diff not in dist_map[w1]:
                    dist_map[w1][diff] = set()
                dist_map[w1][diff].add(w2)
                if w2 not in dist_map:
                    dist_map[w2] = {}
                if diff not in dist_map[w2]:
                    dist_map[w2][diff] = set()
                dist_map[w2][diff].add(w1)
        candidates = set(wordlist)
        guess_word = wordlist[0]
        for i in range(10):
            dist = master.guess(guess_word)
            if guess_word not in dist_map:
                print(guess_word + ' not in map')
            if dist not in dist_map[guess_word]:
                print(str(dist) + ' not in map')
            dist_set = dist_map[guess_word][dist]
            # Note: 一定要把猜过的拿走
            candidates.remove(guess_word)
            candidates = candidates.intersection(dist_set)
            if len(candidates):
                guess_word = list(candidates)[0]
            else:
                return

    def diff(self, w1, w2):
        # 返回有几位是**一样**的
        res = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                res += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
