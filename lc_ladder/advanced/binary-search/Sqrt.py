#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: Binary Search
D.S.:

Solution:
1. 找到可行解的范围 0 -- x
2. 猜答案 （二分）(0 -- x) // 2
3. 检验条件，来判断答案应该在哪一侧
4. 调整搜索范围
特征：find **the last number** such that number ** 2 <= x
Time: O(logx)

Corner cases:
"""
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        l, r = 0, x
        while l + 1 < r:
            mid = (l + r) // 2
            if mid ** 2 < x:
                l = mid
            elif mid ** 2 > x:
                r = mid
            else:
                return mid
        if r ** 2 <= x:
            return r
        else:
            return l

# Test Cases
if __name__ == "__main__":
    testCases = [
    1, 4, 8, 9, 10
    ] # 1, 2, 2, 3, 3
    s = Solution()
    for x in testCases:
        res = s.sqrt(x)
        print("res; %s" %res)
