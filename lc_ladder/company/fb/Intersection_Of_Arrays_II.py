#! /usr/local/bin/python3

# https://www.lintcode.com/problem/intersection-of-two-arrays-ii/description
# Example
# 给定两个数组，计算两个数组的交集
#
# 样例
# 样例1
#
# 输入:
# nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# 输出:
# [2, 2]
# 样例2
#
# 输入:
# nums1 = [1, 1, 2], nums2 = [1]
# 输出:
# [1]
# 挑战
# -如果给定的数组已经排序了怎么办?如何优化算法?
# -如果nums1的大小比num2的小怎么办?哪种算法更好?
# -如果nums2的元素存储在磁盘上，并且内存受到限制，以至于不能一次将所有元素加载到内存中，该怎么办?
#
# 注意事项
# 每个元素出现次数得和在数组里一样
# 答案可以以任意顺序给出


"""
Algo: two pointers
D.S.: map, counter

Solution:
用map维护前一个数组中每个值出现的次数
然后遍历第二个数组，对于每个遍历到的数，在map中将这个数出现的次数-1
Time: O(n)
Space: O(n)

Follow-up1: sorted, 可以用双指针，不用额外空间
Follow-up2: 把较小的那个放入map, 节省空间
Follow-up3: 

Corner cases:
"""


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        mp = {}
        for i in nums1:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        res = []
        for i in nums2:
            # 注意要查这个条件
            if i in mp and mp[i] > 0:
                res.append(i)
                mp[i] -= 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
