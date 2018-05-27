#! /usr/local/bin/python3

# https://www.lintcode.com/problem/decode-string/description
# Example
# s = abc3[a] return abcaaa
# s = 3[abc] return abcabcabc
# s = 4[ac]dy, return acacacacdy
# s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

"""
Algo: DFS
D.S.: Stack

Solution:
Same with "/data-structure/Expression_Expand"
1. DFS Recusion O(N^2), may explode memory stack
2. stack O(N)

Corner cases:
Be careful about details
"""
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        for ele in s:
            if ele != ']':
                stack.append(ele)
            else:
                str = ""
                while len(stack) and stack[-1] != "[":
                    str = stack.pop() + str
                stack.pop() # pop '['
                i = 0
                num = 0
                while len(stack) and self.isNumber(stack[-1]):
                    num += (10 ** i) * (ord(stack.pop()) - ord('0'))
                    i += 1
                stack.append(str * num)
        res = ""
        while len(stack):
            res = stack.pop() + res
        return res

    def isNumber(self, ele):
        if len(ele) == 1 and ord('0') <= ord(ele) <= ord('9'):
            return True
        else:
            return False


# Test Cases
if __name__ == "__main__":
    testCases = [
        "3[abc]",
        "4[ac]dy",
        "3[2[ad]3[pf]]xyz",
        "5[10[abcd]Ac20[abcde]]"
    ]
    s1 = Solution()
    for s in testCases:
        res1 = s1.expressionExpand(s)
        print("res1: %s" %res1)
