#! /usr/local/bin/python3

# https://www.lintcode.com/problem/relative-ranks/description?_from=ladder&&fromId=18
# Example
# 根据N名运动员的得分，找到他们的相对等级和获得最高分前三名的人，他们将获得奖牌：“金牌”，“银牌”和“铜牌”。
#
# 样例
# 例子 1:
#
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 说明：前三名运动员获得前三名最高分，因此获得“金牌”，“银牌”和“铜牌”。
# 对于右边两名运动员，你只需要根据他们的分数输出他们的相对等级。
# 注意事项
# N是正整数，并且不超过10,000。
# 所有运动员的成绩都保证是独一无二的。

"""
Algo: sorting
D.S.: map, idx etc

Solution:
Time: O(nlogn) Space: O(n)

Corner cases:
"""

class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        if not nums:
            return []

        res = [None for _ in range(len(nums))]
        ll = []
        for i in range(len(nums)):
            ll.append((nums[i], i))
        sortedList = sorted(ll, key = lambda x : -x[0])
        print(sortedList)
        for i in range(len(sortedList)):
            if i == 0:
                res[sortedList[i][1]] = 'Gold Medal'
            elif i == 1:
                res[sortedList[i][1]] = 'Silver Medal'
            elif i == 2:
                res[sortedList[i][1]] = 'Bronze Medal'
            else:
                # remember use i + 1 not idx value i
                res[sortedList[i][1]] = str(i + 1)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
