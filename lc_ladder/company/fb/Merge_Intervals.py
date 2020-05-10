#! /usr/local/bin/python3

# https://leetcode.com/problems/merge-intervals/solution/
# Example

"""
Algo: Sort
D.S.:

Solution:
法1， 把res 前一个 Pop出来 合并再放回去
法2。 直接修改 res[-1] 的起止点
Time: O(nlogn)
Space: O(n)

FB Follow-Up:
Merge interval stream
https://leetcode.com/problems/merge-intervals/discuss/21452/Share-my-interval-tree-solution-no-sorting

Corner cases:
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if res[-1][1] < s:
                res.append(intervals[i])
            else:
                res[-1][0] = min(res[-1][0], s)
                res[-1][1] = max(res[-1][1], e)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
