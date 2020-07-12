#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/
# Example
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
# Note:
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

"""
Algo: DP, Binary Search
D.S.:

Solution1: DP matching
Time: O(mn)
Space: O(mn)
注意
A[i - 1] == B[j - 1] f[i][j] = f[i - 1][j - 1] + 1
A[i - 1] != B[j - 1] f[i][j] = 0 只能是0， 因为subarray 必须是连续的

如果不是连续的可以考虑findLength_2 的写法
这个写法在这题目下是不成立的


Solution2:
Binary Search (Suggested, can pass OJ)
Time: O((m + n) * log(min(m, n)))
Space: O(min(m, n))

binary search 尝试max length的情况
拿到A， B中去看是否满足
在A中存所有长度为L的subarray, B中找所有长度为L的subarray 跟set 比较是否存在
思路很简单，但是要写对


Corner cases:
"""

class Solution1:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        res = 0
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = 0
                res = max(res, f[i][j])
        return res



    def findLength_2(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                f[i][j] = max(f[i][j], f[i - 1][j], f[i][j - 1])
        return f[-1][-1]

class Solution2:
    def findLength(self, A: List[int], B: List[int]) -> int:
        l, r = 0, min(len(A), len(B))
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.valid(mid, A, B):
                l = mid
            else:
                r = mid
        if self.valid(r, A, B):
            return r
        return l

    def valid(self, length, A, B):
        if not length:
            return True
        s = set()
        for i in range(len(A) - length + 1):
            s.add(tuple(A[i:(i + length)]))
        for i in range(len(B) - length + 1):
            if tuple(B[i:(i + length)]) in s:
                return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
