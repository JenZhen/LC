#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# Example
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
#
# Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:
#
# Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.
#
#
#
# Example 1:
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
# Example 2:
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.
#
#
# Note:
#
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.

"""
Algo:
D.S.: heap, sort

Solution:
根据描述任何一个合法的pay group里面任意两个worker之间 quality1/quality2 = wage1/wage2，转化一下 wage1/quality1 = wage2 / quality2，
即所有的工人他们的paid wage和他们的quality的比值都应该是一样的，根据这个性质，我们每一个合法的pay group只能取最大的wage/quality当作所有工人的pay ratio。

假如我们不取最大的，选择的ratio为w1/q1，而且存在一个工人的wagei/qualityi > w1/q1，转换一下很容易得到 wagei > quaility * w1/q1，
即表示该工人的最低工资大于了他实际得到的工资，和题意不符合。

所以有了以上性质后，直接根据ratio排序，然后又需要每个group的pay最小，每个group的总工资计算方法（q1+q2+q3+...+qk）* ratio，
所以就是需要quality的sum最小，那每次我们加入了一个新的ratio就把quality最大worker踢出group，这样每次group的pay可以保证是新ratio下的最小pay。遍历数组，记录所有ratio中出现的pay最小值即可。

Time: O(nlogn) + O(nlogK)

Corner cases:
"""

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from heapq import heappush, heappop
        workers = []
        for i in range(len(wage)):
            workers.append([wage[i] / quality[i], quality[i]])
        workers = sorted(workers)
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            if len(heap) == K:
                qsum += heappop(heap)
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
