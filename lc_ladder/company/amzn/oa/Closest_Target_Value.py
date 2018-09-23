#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
Time O(nlogn) + O(n)


Corner cases:
"""
class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        if target is None or not array or len(array) < 2:
            return -1
        import sys
        res = -sys.maxsize
        array.sort()
        l, r = 0, len(array) - 1
        while l < r:
            ttl = array[l] + array[r]
            print("get ttl: %s" %ttl)
            if ttl < target:
                res = max(res, ttl)
                l += 1
            elif ttl == target:
                return ttl
            else:
                r -= 1
        return -1 if res == -sys.maxsize else res

# Test Cases
if __name__ == "__main__":
    testCase = [
        {"target": 0,
         "array": [5,-15,15,7,6,5,-3,-1,11,15,12,17,-5,15]
        }
    ]
    solution = Solution()
    for t in testCase:
        target = t["target"]
        array = t["array"]
        res = solution.closestTargetValue(target, array)
        print("res: %s" %res)
