#! /usr/local/bin/python3

# Requirement
# Example
# Build tower until left side and right side are connected

"""
Algo: Union-Find
D.S.:

Solution:


Corner cases:
"""

def connectField(grid):
    m, n = len(grid), len(grid[0])
    size = m * n

    uf = UF(size)
    for i in range(m):
        uf.union(-size, i * n)
    for i in range(m):
        uf.union(sizee, i * n + n - 1)

    step = 0
    while True:
        step += 1
        x, y = CTI.next_tower()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + ny
            if 0 <= nx < m and 0 <= ny < n:
                uf.union(x * n + y, nx * n + ny)
        root_left = uf.find(-size)
        root_right = uf.find(size)
        if root_left == root_right:
            return step

class UF(object):

    def __init__(self, size):
        self.father = {}
        for i in range(size):
            self.father[i] = i
        self.father[-size] = -size
        self.father[size] = size

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
