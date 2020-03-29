#! /usr/local/bin/python3

# https://www.lintcode.com/problem/nuts-bolts-problem/description
# Example
# 给定一组 n 个不同大小的 nuts 和 n 个不同大小的 bolts. nuts 和 bolts 一一匹配.
#
# 不允许将 nut 之间互相比较, 也不允许将 bolt 之间互相比较. 也就是说, 只许将 nut 与 bolt 进行比较, 或将 bolt 与 nut 进行比较. 我们会提供一个比较函数, 用于nut和bolt的比较.
#
# 利用我们提供的函数, 你需要将 nuts 或者 bolts 重新排列, 使得它们按照顺序一一匹配.
#
# 样例
# 给出 nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC']
#
# 你的程序应该找出bolts和nuts的匹配.
#
# 根据比较函数, 一组可能的返回结果是：
#
# nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG']
#
# 如果我们给你另外的比较函数，可能返回的结果是：
#
# nuts = ['ab','bc','dd','gg'], bolts = ['BC','AB','DD','GG']
#
# 因此的结果完全取决于比较函数，而不是字符串本身。因为你必须使用比较函数来进行排序。
#
# 各自的排序当中nuts和bolts的顺序是无关紧要的，只要他们一一匹配就可以。

"""
Algo: quick_sort template
D.S.:

Solution:
# TODO:
Time: ?
Space: O(n)

nuts和bolts数组内的元素是一一对应的. 并且元素之间是有大小关系的.

题意可以这么理解: nuts是一个排列, bolts也是一个排列, 需要把它们变成同一个排列(不一定是升序排列或降序),

但是我们仅仅可以比较nuts的某个元素和bolts的某个元素.

我们同时将两个数组都排成升序以让它们满足按照顺序一一对应的关系.

排序的过程类似快速排序.

定义 quickSort(nuts, bolts, l, r, compare)为将两个数组的[l, r]区间排好序

选取比如nuts[l]作为pivot, 将bolts数组根据pivot做好划分(比它小的在左边, 比它大的在右边)
因为只能借助对方数组的元素进行比较, 所以此时借用bolts内的该值对nuts再进行一次划分
递归处理左右子区间
关键在于2, 如果没有这一步, 那么nuts不会变成有序的. 最终也无法按照顺序一一对应.

Corner cases:
"""
"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        self.quick_sort(nuts, bolts, 0, len(nuts) - 1, compare.cmp)

    def quick_sort(self, nuts, bolts, start, end, cmp):
        if start >= end:
            return

        left, right = start, end

        index = self.partition(bolts, left, right, nuts[(left + right) // 2], cmp)
        self.partition(nuts, left, right, bolts[index], cmp)

        self.quick_sort(nuts, bolts, start, index - 1, cmp)
        self.quick_sort(nuts, bolts, index + 1, end, cmp)

    def partition(self, arr, start, end, pivot, cmp):
        left, right = start, end

        for i in range(left, right + 1):
            if cmp(arr[i], pivot) == 0 or cmp(pivot, arr[i]) == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                break

        while left <= right:
            while left <= right and (cmp(arr[left], pivot) == -1 or cmp(pivot, arr[left]) == 1):
                left += 1
            while left <= right and (cmp(arr[right], pivot) == 1 or cmp(pivot, arr[right]) == -1):
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1

        arr[start], arr[right] = arr[right], arr[start]
        return right

# Test Cases
if __name__ == "__main__":
    solution = Solution()
