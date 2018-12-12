#!/usr/local/bin/python3

# https://www.lintcode.com/problem/heart-beat/description?_from=ladder&&fromId=8
# Example

# 在Master-Slave结构模式中，slave端会每隔k秒向master端发送ping请求表示自己还在运行。如果master端在 2 * k 秒内没有接收到任何来自slave的ping请求，那么master端会向管理员发送一个警告(比如发送一个电子邮件)。
#
# 现在让我们来模拟master端，你需要实现以下三个功能：
# 1.initialize(slaves_ip_list, k)，slaves_ip_list是所有slaves的ip地址列表，k为一个定值。
# 2.ping(timestamp, slave_ip)，这个方法在master端从slave端收到ping请求时执行，timestamp指当前的时间戳，slave_ip代表当前发送请求的slave端的ip地址
# 3.getDiedSlaves(timestamp)，这个方法会定期的(两次执行之间的时间间隔不确定)执行，timestamp代表当前的时间戳，此方法需要返回不再运行的slave端的所有ip地址列表，如果没有发现则返回空集合。
#
# 你可以假设当master端开始运行的时候时间戳为0，所有的方法都会根据全局的增长的时间戳来运行。
#
# 样例
# initialize(["10.173.0.2", "10.173.0.3"], 10)
# ping(1, "10.173.0.2")
# getDiedSlaves(20)
# \>> ["10.173.0.3"]
# getDiedSlaves(21)
# \>> ["10.173.0.2", "10.173.0.3"]
# ping(22, "10.173.0.2")
# ping(23, "10.173.0.3")
# getDiedSlaves(24)
# \>> []
# getDiedSlaves(42)
# \>> ["10.173.0.2"]


"""
Solution:
这个设计不用想太复杂
不需要用heap来维护很久以前的heart beat
发送的heart beat 请求很可能多于机器数量所以只需要遍历一下所有的机器就行了

Corner cases:
"""

class HeartBeat:

    def __init__(self):
        self.k = None
        self.id_map = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        self.k = k
        for id in slaves_ip_list:
            self.id_map[id] = 0
    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        if slave_ip not in self.id_map:
            return
        self.id_map[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        res = []
        for id, ts in self.id_map.items():
            if timestamp - ts >= self.k * 2:
                res.append(id)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
