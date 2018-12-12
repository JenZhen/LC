#!/usr/local/bin/python3

# https://www.lintcode.com/problem/load-balancer/description?_from=ladder&&fromId=8
# Example
# 为网站实现一个负载均衡器，提供如下的 3 个功能：
#
# 添加一台新的服务器到整个集群中 => add(server_id)。
# 从集群中删除一个服务器 => remove(server_id)。
# 在集群中随机（等概率）选择一个有效的服务器 => pick()。
# 样例
# 最开始时，集群中一台服务器都没有。
#
# add(1)
# add(2)
# add(3)
# pick()
# >> 1         // 返回值是随机的，这里是 1 或者 2 或者 3 都正确。
# pick()
# >> 2
# pick()
# >> 1
# pick()
# >> 3
# remove(1)
# pick()
# >> 2
# pick()
# >> 3
# pick()
# >> 3

"""
Solution:
O(1) for all operation

Corner cases:
"""
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.id_pos = {}
        self.id_list = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id not in self.id_pos:
            self.id_list.append(server_id)
            self.id_pos[server_id] = len(self.id_list) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.id_pos:
            return
        rmPos = self.id_pos[server_id]
        del self.id_pos[server_id]

        lastId = self.id_list[-1]
        self.id_pos[lastId] = rmPos
        self.id_list[rmPos] = lastId
        self.id_list.pop()


    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        if len(self.id_list) == 0:
            return None
        import random
        pickid = random.randrange(len(self.id_list))
        return self.id_list[pickid]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
