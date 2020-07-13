#! /usr/local/bin/python3

# https://leetcode.com/problems/brace-expansion/
# Example
# A string S represents a list of words.
# Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.
# If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].
#
# For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
# Return all words that can be formed in this manner, in lexicographical order.
#
# Example 1:
#
# Input: "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
# Example 2:
#
# Input: "abcd"
# Output: ["abcd"]
#
# Note:
#
# 1 <= S.length <= 50
# There are no nested curly brackets.
# All characters inside a pair of consecutive opening and ending curly brackets are different.
"""
Algo: DFS, Combination
D.S.:

Solution:
DFS find all combination
same as https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Corner cases:
"""
class Solution:
    def expand(self, S: str) -> List[str]:
        if not S: return []
        word_list = self.reorg(S)
        print(word_list)

        n = len(word_list)
        self.res = []
        self.dfs(word_list, 0, '')
        return self.res

    def dfs(self, word_list, start_idx, path):
        if len(path) == len(word_list):
            self.res.append(path[:])
            return

        chars = word_list[start_idx]
        for c in chars:
            self.dfs(word_list, start_idx + 1, path + c)

    def reorg(self, S):
        word_list = []
        in_group = False
        for c in S:
            if c == '{':
                in_group = True
                tmp = ''
            elif c == '}':
                tmp = sorted(list(set(tmp)))
                word_list.append(tmp)
                in_group = False
            elif c == ',':
                continue
            else:
                if in_group:
                    tmp += c
                else:
                    word_list.append([c])
        return word_list

# Test Cases
if __name__ == "__main__":
    solution = Solution()
