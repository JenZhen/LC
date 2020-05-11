#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-consecutive-sequence/
# Example
# FB interview variation
# Given an unsorted array of integers, find all longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
#
# Example:
# Input: [103,4,200,102,1,3,2, 101,104, 201]
# Output: [[103, 102, 101, 104], [4, 3, 2, 1]]
# Explanation: The longest consecutive
"""
Algo:
D.S.:

Solution: freq map
Time: O(n)
Space: O(n)
Corner cases:
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        len_map = {}
        res_list = [[]]

        # prep len_map
        for n in nums:
            if n not in len_map:
                len_map[n] = 1
            else:
                len_map[n] += 1

        # calc length
        for n in nums:
            tmp_res = []
            if n not in len_map:
                continue
            tmp_res.append(n)
            if len_map[n] == 1:
                del len_map[n]
            else:
                len_map[n] -= 1

            l = n - 1
            r = n + 1

            while l in len_map:
                tmp_res.append(l)
                if len_map[l] == 1:
                    del len_map[l]
                else:
                    len_map[l] -= 1
                l -= 1

            while r in len_map:
                tmp_res.append(r)
                if len_map[r] == 1:
                    del len_map[r]
                else:
                    len_map[r] -= 1
                r += 1

            cur_max = len(res_list[-1])
            if len(tmp_res) == cur_max:
                res_list.append(tmp_res)
            elif len(tmp_res) > cur_max:
                res_list = [tmp_res]
        return res_list

# Test Cases
if __name__ == "__main__":
    solution = Solution()
