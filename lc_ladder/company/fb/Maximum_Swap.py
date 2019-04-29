#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-swap/description
# Example
# 给定一个非负整数, 你可以选择交换它的两个数位. 返回你能获得的最大的合法的数.
#
# 样例
# 样例1:
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7.
# 样例2:
#
# 输入: 9973
# 输出: 9973
# 解释: 不用交换.
# 注意事项
# 给定的数字在 [0, 10^8] 范围内


"""
Algo: swap array
D.S.:

Solution:
Time: O(n)
Space: O(1)

- 如果严格递减 - 无须改动
- 如果有上升 - 说明后面比较大的就有可能挪到前面来。
 - 先找有没有上升的地方，包括一开始就递增的情况
 - 从上升的位置开始往后找最大值，并记录他的index，如果有多个最大值，记录最后面那个，因为要尽量保证较高位的大值不被swap 成小值
 - 从最左端找第一个比最大值小的数，swap, (找第一个因为在最高位)

Corner cases:
"""


class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        if not num:
            return num

        num = [i for i in str(num)]
        asc = False
        minidx, minval = 0, num[0]
        maxidx, maxval = None, None
        for i in range(1, len(num)):
            if num[i] < minval:
                minval = num[i]
                minidx = i
            else:
                asc = True
                maxidx, maxval = i, num[i]
                break
        if asc == False:
            return int(''.join(num))

        for i in range(maxidx, len(num)):
            # look for the last position of largest value
            if maxval <= num[i]:
                maxval = num[i]
                maxidx = i

        for i in range(maxidx):
            if num[i] < maxval:
                num[i], num[maxidx] = num[maxidx], num[i]
                break
        return int(''.join(num))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
