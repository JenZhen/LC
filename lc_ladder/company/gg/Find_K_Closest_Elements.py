#! /usr/local/bin/python3

# https://www.lintcode.com/problem/find-k-closest-elements/description?_from=ladder&&fromId=18
# Example
# 给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
#
# 样例
# 如果 A = [1, 2, 3], target = 2 and k = 3, 那么返回 [2, 1, 3].
#
# 如果 A = [1, 4, 6, 8], target = 3 and k = 3, 那么返回 [4, 1, 6].
#
# 挑战
# O(logn + k) 的时间复杂度
#
# 注意事项
# 1.k是一个非负整数，并且总是小于已排序数组的长度。
# 2.给定数组的长度是有意义的,不会超过10 ^ 4
# 3.组中元素的绝对值不会超过10 ^ 4

"""
Algo: Binary search
D.S.: array

Solution:
要点：
1. sorted数组可以二分
2. 不是精准二分，只需要挪到最相近target的位置就可以了
3. 找到最近2个位置然后向数组两头挪动，注意index越界问题，一共走k步

Time complexity: O(logn + k)
Corner cases:
"""

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or target is None or not k:
            return []
        st, end = 0, len(A) - 1

        while st + 1 < end:
            mid = st + (end - st) // 2
            # A[mid] == target 归为左右都可以
            if A[mid] >= target:
                end = mid
            else:
                st = mid
        # terminated with st, end next to each other pointing
        # at 2 values closest to target
        res = []
        for i in range(k):
            if st == -1 and end == len(A):
                return res
            elif st == -1:
                res.append(A[end])
                end += 1
            elif end == len(A):
                res.append(A[st])
                st -= 1
            else:
                if abs(A[st] - target) <= abs(A[end] - target):
                    res.append(A[st])
                    st -= 1
                else:
                    res.append(A[end])
                    end += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
