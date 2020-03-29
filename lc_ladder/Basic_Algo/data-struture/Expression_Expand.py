#!/usr/bin/python

# http://lintcode.com/en/problem/expression-expand/

# s = abc3[a] return abcaaa
# s = 3[abc] return abcabcabc
# s = 4[ac]dy, return acacacacdy
# s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz
"""
Algo: stack
D.S.: array

Solution:

Corner cases:
1. use while loop not "for i in range(len(s))" loop
    while loop can control the move of i
    for loop cannot reset i position inside the loop
2. pattern "xx[substr]"
    xx is digits for multiplier, can be more than 1
    substring
    2 brackets
3.
"""

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        if s is None or len(s) == 1:
            return s

        stack = [] # keep track of '[' position
        i = 0
        # DO NOT USE for i in s: loop, i's step not controlled in side loop
        while i < len(s):
            if s[i] == '[':
                stack.append(i)
            if s[i] == ']':
                startIdx = stack.pop()
                endIdx = i

                # find all multiplier digit
                # This loop is really tricky
                # j denominate position of first digit of multiplier
                j = startIdx - 1
                while j >= 0:
                    if s[j] <= '9' and s[j] >= '0':
                        j -= 1
                    else:
                        break
                # when exit while 1) j = -1 or 2) j is not a number
                # either way, j need ++ to reset to first number position
                j += 1
                multiplier = int(s[j : startIdx])

                # replace
                subStr = s[startIdx + 1 : endIdx]
                newStr = multiplier * subStr
                #
                s = s[0 : j] + newStr + s[i + 1:]

                # important, re-adjust i's position
                # x2[a]... i at '['
                # xaa...   i at 'a' (2nd)
                i += (len(newStr) - (endIdx - j + 1))
            i += 1
        return s

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    test = [
        "abc3[a]",
        "3[abc]",
        "4[ac]dy",
        "3[2[ad]3[pf]]xyz",
        "1[lintcode]4[abcAhj]4[wer]0[peer]",
        "5[10[abcd]Ac20[abcde]]"
    ]
    for t in test:
        print("Solution: %s" %(solution.expressionExpand(t)))
