#! /usr/local/bin/python3

# https://www.lintcode.com/problem/find-substring/description?_from=ladder&&fromId=62
# Example

"""
Algo: Brutal
D.S.:

Solution:
Note: 每一个substring内部都没有重复的字符
Time: O(n * k)

Corner cases:
"""

class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        if not str or not k or k > 26:
            return 0
        stringSet = set()
        for i in range(k, len(str) + 1):
            wordSet = set()
            noDup = True
            for j in range(i - k, i):
                if str[j] not in wordSet:
                    wordSet.add(str[j])
                else:
                    noDup = False
                    break
            if noDup:
                sub = str[(i - k) : i]
                if sub not in stringSet:
                    stringSet.add(sub)
        return len(stringSet)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
