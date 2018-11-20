#!/usr/local/bin/python3

# https://www.lintcode.com/problem/consistent-hashing-ii/description?_from=ladder&&fromId=8
# Example
# 在 Consistent Hashing I 中我们介绍了一个比较简单的一致性哈希算法，这个简单的版本有两个缺陷：
#
# 增加一台机器之后，数据全部从其中一台机器过来，这一台机器的读负载过大，对正常的服务会造成影响。
# 当增加到3台机器的时候，每台服务器的负载量不均衡，为1:1:2。
# 为了解决这个问题，引入了 micro-shards 的概念，一个更好的算法是这样：
#
# 将 360° 的区间分得更细。从 0~359 变为一个 0 ~ n-1 的区间，将这个区间首尾相接，连成一个圆。
# 当加入一台新的机器的时候，随机选择在圆周中撒 k 个点，代表这台机器的 k 个 micro-shards。
# 每个数据在圆周上也对应一个点，这个点通过一个 hash function 来计算。
# 一个数据该属于那台机器负责管理，是按照该数据对应的圆周上的点在圆上顺时针碰到的第一个 micro-shard 点所属的机器来决定。
# n 和 k在真实的 NoSQL 数据库中一般是 2^64 和 1000。
#
# 请实现这种引入了 micro-shard 的 consistent hashing 的方法。主要实现如下的三个函数：
#
# create(int n, int k)
# addMachine(int machine_id) // add a new machine, return a list of shard ids.
# getMachineIdByHashCode(int hashcode) // return machine id
# 样例
# create(100, 3)
# addMachine(1)
# >> [3, 41, 90]  => 三个随机数
# getMachineIdByHashCode(4)
# >> 1
# addMachine(2)
# >> [11, 55, 83]
# getMachineIdByHashCode(61)
# >> 2
# getMachineIdByHashCode(91)
# >> 1
# 注意事项
# 当 n 为 2^64 时，在这个区间内随机基本不会出现重复。
# 但是为了方便测试您程序的正确性，n 在数据中可能会比较小，所以你必须保证你生成的 k 个随机数不会出现重复。
# LintCode并不会判断你addMachine的返回结果的正确性（因为是随机数），只会根据您返回的addMachine的结果判断你getMachineIdByHashCode结果的正确性。

"""
Solution:

Corner cases:
"""

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.ids = {}
        solution.machines = {}
        solution.n = n
        solution.k = k
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        # write your code here
        ids = []
        import random
        for i in range(self.k):
            index = random.randint(0, self.n - 1)
            while index in self.ids:
                index = random.randint(0, self.n - 1)

            ids.append(index)
            self.ids[index] = machine_id

        ids.sort()
        self.machines[machine_id] = ids
        return ids

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        machine_id = -1
        distance = self.n + 1

        for key, value in self.machines.items():
            import bisect
            index = bisect.bisect_left(value, hashcode) % len(value)
            d = value[index] - hashcode
            if d < 0:
                d += self.n

            if d < distance:
                distance = d
                machine_id = key

        return machine_id

# Test Cases
if __name__ == "__main__":
    solution = Solution()
