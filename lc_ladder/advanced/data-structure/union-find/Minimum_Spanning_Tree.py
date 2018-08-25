#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-spanning-tree/description
# Example

"""
Algo:
D.S.: Union-Find

Solution:
Time: O(nlogn) + O(n) Space: O(n)

Corner cases:
"""
# Python2.x version comparator working
'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
def comp(a, b):
    if a.cost != b.cost:
        return a.cost - b.cost

    if a.city1 != b.city1:
        if a.city1 < b.city1:
            return -1
        else:
            return 1

    if a.city2 == b.city2:
        return 0
    elif a.city2 < b.city2:
        return -1
    else:
        return 1

class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections.sort(cmp=comp)
        hash = {}
        n = 0
        for connection in connections:
            if connection.city1 not in hash:
                n += 1
                hash[connection.city1] = n

            if connection.city2 not in hash:
                n += 1
                hash[connection.city2] = n

        father = [0 for _ in xrange(n + 1)]

        results = []
        for connection in connections:
            num1 = hash[connection.city1]
            num2 = hash[connection.city2]

            root1 = self.find(num1, father)
            root2 = self.find(num2, father)
            if root1 != root2:
                father[root1] = root2
                results.append(connection)

        if len(results)!= n - 1:
            return []
        return results

    def find(self, num, father):
        if father[num] == 0:
            return num
        father[num] = self.find(father[num], father)
        return father[num]


# Python3 version -- not working at city1 sort
'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        from functools import cmp_to_key
        def cmptor(a, b):
            if a.cost != b.cost:
                return a.cost - b.cost
            if a.city1 != b.city1:
                if a.city1 < b.city1:
                    return -1
                else:
                    return 1
            if a.city2 == b.city2:
                return 0
            elif a.city2 < b.city2:
                return -1
            else:
                return 1
        sorted(connections, key=cmp_to_key(cmptor))
        dict = {}
        n = 0
        for cnnt in connections:
            if cnnt.city1 not in dict:
                n += 1
                dict[cnnt.city1] = n
            if cnnt.city2 not in dict:
                n += 1
                dict[cnnt.city2] = n

        # init father all to 0
        father = [0 for i in range(n + 1)]
        res = []
        for cnnt in connections:
            num1 = dict[cnnt.city1]
            num2 = dict[cnnt.city2]

            root1 = self.find(num1, father)
            root2 = self.find(num2, father)
            if root1 != root2:
                father[root1] = root2
                res.append(cnnt)
        if len(res) != n - 1:
            return []
        return res

    def find(self, id, father):
        if father[id] == 0:
            return id # return its self
        father[id] = self.find(father[id], father)
        return father[id]

# Test Cases
if __name__ == "__main__":
    s = Solution()
