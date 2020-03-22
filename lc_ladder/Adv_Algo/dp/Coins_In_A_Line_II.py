#! /usr/local/bin/python3

# https://www.lintcode.com/problem/coins-in-a-line-ii/description
# Example
# There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.
#
# Could you please decide the first player will win or lose?
#
# Example
# Given values array A = [1,2,2], return true.
#
# Given A = [1,2,4], return false.

"""
Algo: DP 记忆化搜索
D.S.:
Time O(n), Space O(n)
Solution1: 针对先手一个player来分析状态

A(first-hand)  （5，2，1，10）
        take 5 /        \ take 5，2
              /          \
B         （2，1，10）  （1，10）
    take 2 / \take 2,1 1 /  \ take 1, 10
          /   \         /    \
A     （1，10）  10    10      0

如果A选择取1，要保证B无论取1还是取2，A都赢；同理于A取2
只要A取1或取2有一个能保证赢，A就可以赢

1. 状态
f[i]: 先手A，面对有i个剩余硬币时的输赢状态
2. 方程
f[i] = max(
        min(f(i - 2), f(i - 3)) + values[len(values) - i], #取倒数第i个
        min(f(i - 3), f(i - 4)) + values[len(values) - i] + values[len(values) - i + 1] #取倒数第i个 倒数第（i+1）个
    )
f[i - 2] --> 先1后1， 共减少2个
f[i - 3] --> 先1后2 或 先2后1， 共减少3个
f[i - 4] --> 先2后2， 共减少4个

3. 初始化
因为有f[i - 4]所以要i从4开始循环，初始从0->3
f[0] = 0
f[1] = value[n - 1]
f[2] = value[n - 1 + 1] + value[n - 1]
f[3] = value[n - 1 + 1] + value[n - 1]

4. 答案
return f[n] > sum(value) / 2

Corner cases:
"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        f = [None] * (n + 1) # f[n] : with n ele in values left, best firstWillGet
        ttl = sum(values)
        firstBestValue = self.search(n, f, values)
        if ttl < 2 * firstBestValue:
            return True
        else:
            return False

    def search(self, i, f, values):
        if f[i] != None:
            return f[i]
        if i == 0:
            f[0] = 0
        elif i == 1:
            f[1] = values[len(values) - 1]
        elif i == 2:
            f[2] = values[len(values) - 1] + values[len(values) - 2]
        elif i == 3:
            f[3] = values[len(values) - 2] + values[len(values) - 3]
        else:
            f[i] = max(
                    min(self.search(i - 2, f, values), self.search(i - 3, f, values)) + values[len(values) - i],
                    min(self.search(i - 3, f, values), self.search(i - 4, f, values)) + values[len(values) - i] + values[len(values) - i + 1]
                )
        return f[i]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
