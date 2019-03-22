#! /usr/local/bin/python3

# https://www.lintcode.com/problem/intersection-of-two-arrays/description
# Example
# 给出两个数组，写出一个方法求出它们的交集
#
# 样例
# 例1:
#
# 输入: nums1 = [1, 2, 2, 1], nums2 = [2, 2],
# 输出: [2].
# 例2:
#
# 输入: nums1 = [1, 2], nums2 = [2],
# 输出: [2].
# 挑战
# 可以用三种不同的方法实现吗？
#
# 注意事项
# -结果中的每个元素必须是唯一的。
# -结果可以是任意顺序的。

"""
Algo: sort, two-pointers, binary
D.S.: set, hash

Solution:
需要多解且熟练分析数据结构复杂度

Corner cases:
"""

class Solution1:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        nums1 = list(sorted(set(nums1)))
        nums2 = list(sorted(set(nums2)))
        print(nums1)
        print(nums2)
        l1, l2 = 0, 0
        res = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res
class Solution2:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        res = []
        for num in nums2:
            if num in set1:
                res.append(num)
                set1.remove(num)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
