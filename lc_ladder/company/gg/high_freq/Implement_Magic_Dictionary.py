#! /usr/local/bin/python3

# https://leetcode.com/problems/implement-magic-dictionary/
# Example
# Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
Algo:
D.S.: map

Solution:
Solution1: Faster
Time:
Build: O(n) n is number of word when build
Search: O(n * m) search for all n words, when compare its about length of word

Solution2:
Time:
Build: O(n * m) n is number of word when build
Search: O(m) -- m is len(word)

Space: O(mn)

Corner cases:
"""


class MagicDictionary_1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_map = {} # key: word length

    def _dist_equal_one(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                if diff > 1: return False
        return diff == 1

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            if len(w) not in self.word_map:
                self.word_map[len(w)] = set()
            self.word_map[len(w)].add(w)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if len(word) not in self.word_map:
            return False
        words = self.word_map[len(word)]
        for w in words:
            if self._dist_equal_one(w, word):
                return True
        return False



class MagicDictionary_2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_map = {} # key: fuzzy word, val: set of original letters

    def _get_new_word(self, w, i):
        w_list = list(w)
        w_list[i] = '*'
        return ''.join(w_list)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            for i in range(len(w)):
                new_w = self._get_new_word(w, i)
                original_char = w[i]
                if new_w not in self.word_map:
                    self.word_map[new_w] = set()
                self.word_map[new_w].add(original_char)
        # print(self.word_map)
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            new_w = self._get_new_word(word, i)
            original_char = word[i]
            if new_w in self.word_map and \
                (len(self.word_map[new_w]) > 1 or original_char not in self.word_map[new_w]):
                return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
