#! /usr/local/bin/python3

# no access
# Example

# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.
#
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
#
# Return the smallest possible value of D.
#
# Example:
#
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# Note:
#
# stations.length will be an integer in range [10, 2000].
# stations[i] will be an integer in range [0, 10^8].
# K will be an integer in range [1, 10^6].
# Answers within 10^-6 of the true value will be accepted as correct.

"""
Algo: Binary search
D.S.:

Solution:
priority queue -- 超时
DP -- 超空间
Binary Search -- 最好
1. priority queue
greedy，每次都要分当前最大的区间，用heap 记录当前最大区间
取出top，计算之前的长度，在加入一个点，再重新平均分配原先的区间长度
最后放回heap

Time: init heap O(nlogn) + 把k个加油站插入 O(klogn) n is 给定的区间个数
Space: O(n) -- heap size

2. 二分
根据已知加油站位置，知道2头
猜测最小的距离是mid
尝试去分所有的区间 中间要插入的加油站个数是 (dist // guess range) - 1
加总所有的如果小于等于K 说明猜的区间太大，如果大于K说明猜的区间太小

Corner cases:
"""


class Solution_pq:
    def min_dist_to_gas_station(list_station， k):
        from heapq import heappush, heappop
        heap = [] # save (avg_distance, interval_cnt) -- max heap
        # for example two station 10 apart, put 1 station in avg_distance = 5, interval_cnt = 2 (5, 2),
        # interval_cnt - 1 = station cnt in between
        for i in range(1, len(list_station)):
            heappush(heap, (-(list_station[i] - list_station[0]), 1)) # init each interval of only 1 range, 0 station in between

        for i in range(k):
            # get the largest interval, add one more station that evenly split the old range
            -avg_dist, cnt = heappop()
            new_avg_dist = (avg_dist * cnt) / (cnt + 1)
            heappush(-new_avg_dist, cnt + 1)

        return -(heappop()[0])

class Solution_bs:
    def min_dist_to_gas_station(list_station, k):
        list_station.sort()
        l, r = 0, list_station[-1]
        while l + 10 ^ (-6) < r:
            mid = l + (r - l) / 2
            cnt = 0
            for i in range(1, len(list_station)):
                cnt += (list_station[i] - list_station[i - 1]) // mid - 1
            if cnt <= k:
                # mid -- 区间太大
                r = mid
            else:
                l = mid
        return l

# Test Cases
if __name__ == "__main__":
    solution_pq = Solution_pq()
