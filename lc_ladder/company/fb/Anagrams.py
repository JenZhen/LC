#! /usr/local/bin/python3

# https://www.lintcode.com/problem/anagrams/description
# Example
# 给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。
#
# 样例
# 样例1:
#
# 输入:["lint", "intl", "inlt", "code"]
# 输出:["lint", "inlt", "intl"]
# 样例 2:
#
# 输入:["ab", "ba", "cd", "dc", "e"]
# 输出: ["ab", "ba", "cd", "dc"]
# 挑战
# 什么是Anagram？
#
# 如果在更改字符顺序后它们可以相同，则两个字符串是anagram。
# 注意事项
# 所有的字符串都只包含小写字母

"""
Algo: python string sort, hashmap
D.S.:

Solution:
Be careful that pythong string has no sort() method
To sort use, sorted(string) -> return ['a', 'a', 'b']
then join with "" to a string.
sorted is usable for all python iterables including string

Time: O(n)
Space: O(n)

Corner cases:
"""

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        if not strs:
            return []
        anaMap = {}
        for s in strs:
            # this is how to sort a string not to use str.sort()
            sortedstr = "".join(sorted(s))
            if sortedstr not in anaMap:
                anaMap[sortedstr] = [s]
            else:
                anaMap[sortedstr].append(s)
        res = []
        for key, val in anaMap.items():
            if len(val) > 1:
                res.extend(val)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
