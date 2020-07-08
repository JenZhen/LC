#! /usr/local/bin/python3

# Requirement
# Given a dictionary of valid words, write a function isTypoBecauseStuckKey()
# that accepts a string to determine if the string has a typo that is strictly caused by a stuck key.
#
# Example:
# Input:
# Dictionary: { hello, cat, world, dog, bird, grass, green, help, greet, great }
# String: bbbirrrdddd
# Output: True
# Explanation: The character's 'b', 'r', & 'd' all repeat. Assuming their keys got stuck, we can form the word 'bird', which exists in the dictionary.
#
# Example:
# Input:
# Dictionary: { hello, cat, world, dog, bird, grass, green, help, greet, great }
# String: gggraasssa
# Output: False
# Explanation: The a at the end is not the result of a stuck key, and thus it is impossible for it to exist in the dictionary.


"""
Algo: two pointers
D.S.:

Solution:
two pointers

Corner cases:
"""

def helper(word, text):
    # print('word: ', word)
    # print('text: ', text)
    i, j = 0, 0 # i, j for word and text respectively
    while i < len(word) and j < len(text):
        if word[i] == text[j]:
            i += 1
            j += 1
        else:
            while 0 < j < len(text) and text[j] == text[j - 1]:
                j += 1
            if j == 0 or j == len(text) or word[i] != text[j]:
                return False

    if i < len(word):
        return False
    while j < len(text):
        if text[j] != text[-1]:
            return False
        j += 1
    return True

def checkStuckWords(words, text):
    if not words or not text:
        return False

    for word in words:
        if helper(word, text):
            return True
    return False

# Test Cases
if __name__ == "__main__":
    # solution = Solution()
    words = ["hello", "cat", "world", "dog", "bird", "grass", "green", "help", "greet", "great"]
    texts = ['bbbirrrdddd', 'gggraasssa', 'ddo', 'grras']

    for text in texts:
        print(checkStuckWords(words, text))
