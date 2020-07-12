#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Example
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that
# there are no 2 jobs in the subset with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
#
# Example 1:
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
# Example 2:
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
# Example 3:
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
# Constraints:
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
"""
Algo: DP + Binary Search
D.S.:

Solution:
Time: O(nlogn)
Space: O(n)

- 整理数据为（开始时间，结束时间，利润）
[(1,3,50), (2,4,10), (3,5,40), (3,6,70)]
- 根据结束时间sort
[(1,3,50), (2,4,10), (3,5,40), (3,6,70)]
- 求在每个结束时间点 能得到的最大profit
因为结束时间 是不连续的，用Map来记录 当时的最大profit
维护一个结束时间list, 用于二分法 找到 能和前面 哪个job 共存
end_ts = [3, 4, 5, 6]
例子；
插入（2，4，10）的时候，开始时间 2 bisect_right pos = 0 说明前面没有区间 可以共存
插入（3，5，40）的时候，开始时间 3 bisect_right pos = 1 说明 可以跟结束时间 end_ts[-1] = 3 共存

当前最大profit = max（
    拿当前profit + 前面可共存 结束时间的 profit (如果有的话)，
    不拿当前profit，aka 去前一个结束时间的 profit
）

Corner cases:
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ts = []
        for i in range(len(startTime)):
            ts.append((startTime[i], endTime[i], profit[i]))
        # sort by end time ascendingly
        ts.sort(key=lambda x: x[1])

        end_ts = []
        profit_mp = {} #key: endtime, val: maxprofit at this endtime
        # put the fisrt interval in
        end_ts.append(ts[0][1])
        profit_mp[ts[0][1]] = ts[0][2]

        for i in range(1, len(ts)):
            start = ts[i][0]
            end = ts[i][1]
            profit = ts[i][2]
            last_profit = profit_mp[end_ts[-1]]
            pos = bisect.bisect_right(end_ts, start)
            if pos == 0:
                # cannot take it with previous
                profit_mp[end] = max(profit, last_profit)
            else:
                # can take current with prev_profit, or not take it but take last_profit
                prev_end = end_ts[pos - 1]
                prev_profit = profit_mp[prev_end]
                profit_mp[end] = max(profit + prev_profit, last_profit)
            end_ts.append(end)

        return profit_mp[end_ts[-1]]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
