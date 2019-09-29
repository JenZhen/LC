#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
1. DFS
2. DP

Corner cases:
"""
def dfs(sodas, lo, hi, target_low, target_high, memo):
    key = str(lo) + '-' + str(hi)
    if key in memo:
        return memo[key]
    if lo >= target_low and hi <= target_high:
        memo[key] = True # optional
        return True
    if hi > target_high:
        memo[key] = False
        return False
    for soda in sodas:
        if dfs(sodas, lo + soda[0], hi + soda[1], target_low, target_high, memo):
            newkey = str(lo + soda[0]) + '-' + str(hi + soda[1]) # optional
            return True
    memo[key] = False
    return False

def vendor_machine(sodas, target_low, target_high):
    # key: range, val: true or false
    memo = {}
    return dfs(sodas, 0, 0, target_low, target_high, memo)

# def vendor_machine(sodas, target_low, target_high):
#
#     def dfs(curr_low, curr_high, memo={}):
#         if (curr_low, curr_high) in memo:
#             return memo[curr_low, curr_high]
#         if curr_high > target_high:
#             return False
#         if target_low <= curr_low and curr_high <= target_high:
#             return True
#
#         for low, high in sodas:
#             if dfs(curr_low + low, curr_high + high):
#                 memo[curr_low, curr_high] = True
#                 return True
#         memo[curr_low, curr_high] = False
#         return False
#
#     return dfs(0, 0)
#
# import unittest
#
# class TestVendorMachine(unittest.TestCase):
#     def test_1(self):
#         sodas = [[100, 120], [200, 240], [400, 410]]
#         target_low, target_high = 100, 110
#         assert vendor_machine(sodas, target_low, target_high) == False
#         target_low, target_high = 90, 120
#         assert vendor_machine(sodas, target_low, target_high) == True
#         target_low, target_high = 300, 360
#         assert vendor_machine(sodas, target_low, target_high) == True
#         target_low, target_high = 310, 360
#         assert vendor_machine(sodas, target_low, target_high) == False
#         target_low, target_high = 1, 9999999999
#         assert vendor_machine(sodas, target_low, target_high) == True

if __name__ == "__main__":
    unittest.main()


# Test Cases
if __name__ == "__main__":
    solution = Solution()
