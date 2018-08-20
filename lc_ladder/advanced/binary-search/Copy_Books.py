#! /usr/local/bin/python3

# https://lintcode.com/problem/copy-books/description
# Example
# Given array A = [3,2,4], k = 2.
# Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )

"""
Algo: Binary Search
D.S.:

Solution1:
Same as lc_ladder/binary-search/Copy_Books.py

1. 找到可行解的范围: max(pages) to sum(pages)
2. 猜答案 （二分）: (l + r ) // 2
3. 检验条件，来判断答案应该在哪一侧 if self.numCopier(pages, mid) <= k
用最多mid时间，需要多少个copier
4. 调整搜索范围
特征：**smallest** time that can copy k books

Time: O(nlog(sum(pages) - max(pages)))

Solution2: DP
# TODO:

Corner cases:
"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages or not k:
            return 0

        l = max(pages)
        r = sum(pages)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.numCopier(pages, mid) <= k:
                r = mid
            else:
                l = mid
        if self.numCopier(pages, l) <= k:
            return l
        else:
            return r
    def numCopier(self, pages, timeLimit):
        num, sumPages = 1, pages[0]
        for i in range(1, len(pages)):
            # important: below line is > not >=
            if sumPages + pages[i] > timeLimit:
                num += 1
                sumPages = 0
            sumPages += pages[i]
        return num


# Test Cases
if __name__ == "__main__":
    s = Solution()
