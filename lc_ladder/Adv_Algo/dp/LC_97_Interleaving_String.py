#! /usr/local/bin/python3

# https://www.lintcode.com/problem/interleaving-string/description
# Example
# 给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。
#
# 样例
# 样例 1：
#
# 输入:
# "aabcc"
# "dbbca"
# "aadbbcbcac"
# 输出:
# true
# 样例 2：
#
# 输入:
# ""
# ""
# "1"
# 输出:
# false
# 样例 3：
#
# 输入:
# "aabcc"
# "dbbca"
# "aadbbbaccc"
# 输出:
# false
# 挑战
# 要求时间复杂度为O(n2)或者更好


"""
Algo: DP 匹配
D.S.:

Solution:

dp[i][j]代表由s1的前i个字母和s2的前j个字母是否能构成当前i+j个字母。
然后状态转移即可。（看第i+j+1个是否能被s1的第i+1个构成或被s2的第j+1个构成
Time: O(n1 * n2)
Space: O(n1 * n2)
Corner cases:
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # s1 is row, s2 is col
        f = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        f[0][0] = True
        # init first col, s3 not containing s2
        for i in range(1, n1 + 1):
            if s1[i - 1] == s3[i - 1] and f[i - 1][0] == True:
                f[i][0] = True
        # init first row, s3 not containing s1
        for j in range(1, n2 + 1):
            if s2[j - 1] == s3[j - 1] and f[0][j - 1] == True:
                f[0][j] = True

        # state transfer
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if (s3[i + j - 1] == s1[i - 1] and f[i - 1][j] == True) or\
                    (s3[i + j - 1] == s2[j - 1] and f[i][j - 1] == True):
                    f[i][j] = True
        return f[n1][n2]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
