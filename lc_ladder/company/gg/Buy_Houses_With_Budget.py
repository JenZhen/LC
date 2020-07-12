#! /usr/local/bin/python3

# Requirement
# Example
# 给一个数组代表一排房子的价格，给定budget，房子必须连着买，问能买到最多的房子，
# 返回subarray的第一个index以及能购买房子数。比如给出[2，3，5，8，2，4]，budget是5，那么返回<0,2>。

"""
Algo: two pointers, sliding window
D.S.: 

Solution:
Time: O(n)
Space: O(1)

Corner cases:
"""

def buyHouseInbudget(nums, budget):
    n = len(nums)
    i = 0 # i right end of the range
    j = 0 # j left end of the range
    res = 0

    count = 0
    while i < n:
        count += nums[i]
        while count > budget:
            count -= nums[j]
            j += 1

        res = max(res, i - j + 1)
    return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
