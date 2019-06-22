#! /usr/local/bin/python3

# https://www.lintcode.com/problem/task-scheduler/description
# Example
# 给定一个字符串，表示CPU需要执行的任务。 这个字符串由大写字母A到Z构成，不同的字母代表不同的任务。完成任务不需要按照给定的顺序。 每项任务都可以在一个单位时间内被完成。 在每个单位时间，CPU可以选择完成一个任务或是不工作。
#
# 但是，题目会给定一个非负的冷却时间“n”，表示在执行两个“相同的任务”之间，必须至少有n个单位时间，此时CPU不能执行该任务，只能执行其他任务或者不工作。
#
# 您需要返回CPU完成所有给定任务所需的最少单位时间数。
#
# 样例
# 样例1
#
# 输入: tasks = ['A','A','A','B','B','B'], n = 2
# 输出: 8
# 解释:
# A -> B -> idle -> A -> B -> idle -> A -> B.
# 样例2
#
# 输入: tasks = ['A','A','A','B','B','B'], n = 1
# 输出: 6
# 解释:
# A -> B -> A -> B -> A -> B.
# 注意事项
# 任务数量的范围为 [1, 10000].
# 整数 n 的范围为 [0, 100].

"""
Algo: math
D.S.:

Solution:
仔细分析题意可知，最后所消耗的时间主要受制于出现次数最多的那个字母，所以我们可以推导出，所消耗的时间为 count(字母最多出现次数) * k - (其他字母贡献)
"AAABB" , 2 -> 3 A meaning  "A - - A - - A" 3 A with 2 spaces in-between, total cnt (cntA - 1) * (2 + 1)
if other char is of A's length + 1, is less than A's length just take  - space no more

Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        if not tasks or not n:
            return 0

        cntMap = {}
        maxlen = 0
        for ele in tasks:
            if ele not in cntMap:
                cntMap[ele] = 1
            else:
                cntMap[ele] += 1
            maxlen = max(maxlen, cntMap[ele])
        res = (maxlen - 1) * (n + 1)
        for key, val in cntMap.items():
            if val == maxlen:
                res += 1
                # max with len(tasks) 是考虑到 n = 0的情况
        return max(res, len(tasks))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
