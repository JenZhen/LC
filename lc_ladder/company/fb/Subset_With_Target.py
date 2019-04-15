#! /usr/local/bin/python3

# Excel_Sheet_Column_Title.py
# Example

"""
Algo: subset and two-pointers
D.S.:

Solution:
Solution1:
Time: O(n ^ 2) + O(nlogn)
Space: O(1)

- Sort nums first
- [1,2,3,4,5] target 6,
l, r 2个pointer从左右向中间能找到一对对的upper bound & lower bound
例子：1 - 4, 1的最大上限时4， 同时1 -2 1-3 是可行区间，所以不断挪上限靠近下限，不断计算有几个subsets
- 固定l, r中间的元素可选可不选有 2 ^ (r - l - 1) 个解法
找到所有可行的取件有 n ^ 2 计算是O（1）

这个不断枚举可行区间的算法可以用位运算代替，上下限 [i， j]总共可以有 1<<(j - 1) 个解 （包括一个元素的情况）

Solution2:
Time: O(n) + O(nlogn)
Space: O(1)

Corner cases:
"""


class Solution1:
    """
    @param nums: the array
    @param target: the target
    @return: the number of subsets which meet the following conditions
    """
    def subsetWithTarget(self, nums, target):
        # Write you code here
        if not nums:
            return 0

        res = 0
        nums.sort()
        print(nums)
        # check if pick only one element, for only one number
        # [n], n is smallest and largest at same time
        # it needs to satisty n + n < target
        for n in nums:
            if n * 2 < target:
                res += 1

        # check a range
        # i is lower bound, j is upper bound
        i = 0
        j = len(nums) - 1
        while nums[i] < target:
            # fix i, j moving from right to left to find a proper range
            while nums[i] + nums[j] >= target:
                j -= 1
            print(i, j)
            if j <= i:
                break
            else:
                high_end = j
                while i < high_end:
                    res += 2 ** (high_end - i - 1)
                    high_end -= 1
                i += 1
        return res


class Solution_2:
    """
    @param nums: the array
    @param target: the target
    @return: the number of subsets which meet the following conditions
    """
    def subsetWithTarget(self, nums, target):
        # Write you code here
        if not nums:
            return 0

        res = 0
        nums.sort()
        print(nums)

        # check a range
        # i is lower bound, j is upper bound
        i = 0
        j = len(nums) - 1
        while nums[i] < target:
            # fix i, j moving from right to left to find a proper range
            while nums[i] + nums[j] >= target:
                j -= 1
            print(i, j)
            if j <= i:
                break
            else:
                res += (1<<(j - i))
                i += 1
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
