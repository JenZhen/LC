#! /usr/local/bin/python3

# https://www.lintcode.com/problem/intersection-of-arrays/description
# Example
# 给出多个数组，求它们的交集。输出他们交集的大小。
#
# 样例
# Example 1:
# 	Input:  [[1,2,3],[3,4,5],[3,9,10]]
# 	Output:  1
#
# 	Explanation:
# 	Only '3' in all three array.
#
# Example 2:
# 	Input: [[1,2,3,4],[1,2,5,6,7][9,10,1,5,2,3]]
# 	Output:  2
#
# 	Explanation:
# 	The set is [1,2].
# 注意事项
# The total number of all array elements is not more than 500000.
# There are no duplicated elements in each array.

"""
Algo:
D.S.: map, count

Solution:
Time: O(n) -- 所有的元素都要过一遍
Space: O(n) -- 所有出现的元素都有个map

因为要求指明，同一数组中没有重复，所有可以根据出现次数来判断是否每个数组中都出现

Corner cases:
"""

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        mp = {}
        cnt_arr = len(arrs)
        for arr in arrs:
            for ele in arr:
                if ele not in mp:
                    mp[ele] = 1
                else:
                    mp[ele] += 1
        res = 0
        for key, val in mp.items():
            if val == cnt_arr:
                res += 1
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
