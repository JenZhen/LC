#! /usr/local/bin/python3

# https://www.lintcode.com/problem/digital-coverage/description
# Example
#
# 给出一些区间，问覆盖次数最多的数是多少，如果有多个，输出最小的那个数。
#
# Example
# 样例 1：
#
# 输入：intervals = [(1,7),(2,8)]
# 输出：2
# 解释：2被覆盖了2次，且是覆盖2次中最小的数。
# 样例2：
#
# 输入：intervals = [(1,3),(2,3),(3,4)]
# 输出：3
# 解释：3被覆盖了3次。
# Notice
# 区间的个数不大于10^5。
#
# 区间的左右端点大于0小于等于10^5。

"""
Algo:
D.S.: Sweep line

Solution:
solution1:
Time: O(n), Space: O(max range)
得益于:  区间的左右端点大于0小于等于10^5
建立区间 [0, maxRange + 1]  注意要去到idx = maxRange + 1 的位置
扫描区间赋值，但是最后一定要做cumulation

solution2:
Time: O(nlogn + n)
Space: O(1)


Corner cases:
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        maxOccur = 0
        maxIdx = 0
        maxRange = 0
        for it in intervals:
            maxRange = max(maxRange, it.end)
        li = [0 for _ in range(maxRange + 2)]
        for it in intervals:
            li[it.start] += 1
            li[it.end + 1] -=1
        ttl = 0
        for i in range(len(li)):
            ttl += li[i]
            if ttl > maxOccur:
                maxIdx = i
                maxOccur = ttl
        return maxIdx


class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        if not intervals:
            return None
        maxOccur = 0
        maxIdx = -1
        intvs = []
        for it in intervals:
            intvs.append((it.start, True))
            intvs.append((it.end, False))
        intvs = sorted(intvs, key = lambda x: (x[0], -x[1]))
        print(intvs)
        cnt = 0
        for it in intvs:
            if it[1]:
                cnt += 1
                if cnt > maxOccur:
                    maxOccur = cnt
                    maxIdx = it[0]
            else:
                cnt -= 1
        return maxIdx

# Test Cases
if __name__ == "__main__":
    solution = Solution()
