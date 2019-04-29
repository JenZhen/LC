#! /usr/local/bin/python3

# https://www.lintcode.com/problem/decode-ways-ii/description
# Example

"""
Algo: DP
D.S.:

Solution:
非常多细节
要考虑 0， 1-9， 和* 的情况
以及前面一个字符分别是 0， 1， 2， 3-9， 和*的情况

注意* 代表 1- 9， 所以 x* 就排除了10， 20的可能

Time: O(n)
Space: O(n) -- 可以滚动数组

Corner cases:
"""

class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        # write your code here
        if not s or len(s) == 0:
            return 0

        df = [0] * (len(s) + 1)

        df[0] = 1
        if s[0] == '0':
            df[1] = 0
        elif s[0] == '*':
            df[1] = 9
        else:
            df[1] = 1

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    df[i + 1] += df[i - 1]
                if s[i - 1] == '*':
                    df[i + 1] += df[i - 1] * 2
            elif s[i] == '*':
                if s[i - 1] == '0':
                    df[i + 1] += df[i] * 9
                elif s[i - 1] == '1':
                    df[i + 1] += df[i - 1] * 9
                    df[i + 1] += df[i] * 9
                elif s[i - 1] == '2':
                    df[i + 1] += df[i] * 9
                    df[i + 1] += df[i - 1] * 6 # note 0 not included
                elif '3' <= s[i - 1] <= '9':
                    df[i + 1] += df[i] * 9
                else:
                    df[i + 1] += df[i] * 9
                    df[i + 1] += df[i - 1] * 15
            else:
                # s[i] == 1 - 9
                df[i + 1] += df[i]
                if s[i - 1] != '*' and s[i - 1] != '0':
                    if 1 <= int(s[i - 1: i + 1]) <= 26:
                        df[i + 1] += df[i - 1]
                if s[i - 1] == '*':
                    if '1' <= s[i] <= '6':
                        df[i + 1] += df[i - 1] * 2
                    else:
                        df[i + 1] += df[i - 1]
        print(df)
        return df[len(s)] % 1000000007

# Test Cases
if __name__ == "__main__":
    solution = Solution()
