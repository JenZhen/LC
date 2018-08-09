#! /usr/local/bin/python3

# https://lintcode.com/problem/wood-cut/
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

# Example
# For L=[232, 124, 456], k=7, return 114.

"""
Algo:
D.S.:

Solution1: Binary Search
Same as lc_ladder/binary-search/Wood_Cut.py
Analysis: see lc_ladder/binary-search/Wood_Cut.py
这个题类似于copy book 但是没有DP解法

Time: O(nlog(max(L)))

Important:
sum([l // mid for l in L]) different from sum(L) // mid

1. 找到可行解的范围: 1 to max(L)
2. 猜答案 （二分）: (l + r ) // 2
3. 检验条件，来判断答案应该在哪一侧 if sum([wood // len for wood in L]) >= k 说明每个小段长度可以更长
把所有木头切成长度为len的小段，能有多少个? 如果多于目标k, 说明每个小段长度可以更长
4. 调整搜索范围
特征：**biggest** length that can get >=k pieces

Corner cases:
"""
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if L is None or k is None or len(L) == 0 or sum(L) < k:
            return 0

        lo, hi = 1, max(L)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            numPieces = sum([l // mid for l in L])
            if numPieces >= k:
                lo = mid
            else:
                hi = mid
        if sum([l // hi for l in L]) >= k:
            return hi
        else:
            return lo

# Test Cases
if __name__ == "__main__":
    s = Solution()
