#! /usr/local/bin/python3

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Example
# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.
#
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]
"""
Algo:
D.S.: map

Solution:
首先统计好每个数字出现的次数

从最小的数字开始, 假设当前数字为num

先看看有没有数组以num - 1结尾, 有的话直接把num放过去, 然后以num - 1结尾的数组个数减1, 以num为结尾的数组的个数加1, num的频率减1, 继续下一个数字
如果以num - 1结尾的数组个数不够了, 说明需要建立新的数组, 就要看num + 1和num + 2是否还有, 有的话就建立新的数组,
此时多了一个以num + 2结尾的数组, 所以num + 2结尾的数组个数加1, 同时num + 1, num + 2的频率减1, 最后num的频率也减1, 继续...
以上两点都不满足的话, 说明当前数字放不到任意一个已有的数组末尾, 并且也不能建立新的长度大于等于3的数组了, 返回False
时间: O(n)
空间: O(n)



Corner cases:
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False
        freq_map = {} # key: num, val: freq
        tail_as_map = {} # key: num of array (3 or longer) ended with key, val: cnt
        # count number frequency
        for n in nums:
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
            tail_as_map[n] = 0
        for n in nums:
            if freq_map[n] == 0: continue
            if n - 1 in tail_as_map and tail_as_map[n - 1] > 0:
                # need to add after tail_as_map n - 1
                tail_as_map[n - 1] -= 1
                tail_as_map[n] += 1
            elif (n + 1 in freq_map and freq_map[n + 1] > 0) and (n + 2 in freq_map and freq_map[n + 2] > 0):
                freq_map[n + 1] -= 1
                freq_map[n + 2] -= 1
                tail_as_map[n + 2] += 1
            else:
                return False
            freq_map[n] -= 1
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
