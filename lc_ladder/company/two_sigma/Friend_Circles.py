#! /usr/local/bin/python3

# Requirement
# Example
# You are given a matrix of Ys and Ns where a Y at (i,j) denotes that persons i and j are friends.
# Friendships are transitive, so if A is a friend of B is a friend of C,
# then A is in the same a friend circle as C even if A doesn't know C directly. How many friend circles are there?

"""
Algo:
D.S.: union-find

Solution:
Time: O(n ^ 2) -- iterate half of square relations grid
Union-find amortized complexity O(1)
Space: O(n) for Union-Find

Corner cases:
"""

class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.father = [0] * n
        # init father as its own
        for i in range(n):
            self.father[i] = i

    def find(self, child):
        if self.father[child] == child:
            return self.father[child]
        self.father[child] = self.find(self.father[child])
        return self.father[child]

    def union(self, child1, child2):
        father1 = self.find(child1)
        father2 = self.find(child2)
        if father1 != father2:
            # link father1 as child of father2
            self.father[father1] = father2
            self.count -= 1
    def getUnionCount(self):
        return self.count

def friend_circles(relations):
    # relations is square and symmetric between diagnal
    # length of edge is the number of friends
    # friends are denoted as 0, 1, 2, 3, 4... n - 1
    # Assume relations input is valid
    n = len(relations)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if relations[i][j] == "Y":
                uf.union(i, j)
    return uf.getUnionCount()


# Test Cases
if __name__ == "__main__":
    testcases = [
        [
            ["Y", "Y", "N"],
            ["Y", "Y", "N"],
            ["N", "N", "Y"],
        ], # 2
        [
            ["Y", "N", "N"],
            ["N", "Y", "N"],
            ["N", "N", "Y"],
        ], # 3
        [
            ["Y", "Y", "N"],
            ["Y", "Y", "Y"],
            ["N", "Y", "Y"],
        ], # 1
    ]
    for relations in testcases:
        print(friend_circles(relations))
