#! /usr/local/bin/python3

# Union-Find template

class UnionFind(object):
    def __init__(self, n):
        # init a group of isolated nodes
        self.count = n
        self.father = [0] * n # father mapping n empty slot
        for i in range(n):
            self.father[i] = i

    def find(self, node):
        if self.father[node] == node:
            return node
        newFather = self.find(self.father[node])
        self.father[node] = newFather
        return newFather

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def diagFatherRelation(self):
        print("[")
        for i in range(len(self.father)):
            print("{Father: %s, Son: %s}" %(self.father[i], i))
        print("]")

if __name__ == "__main__" :
    uf = UnionFind(3)
    uf.diagFatherRelation()
    uf.find(0)
    print("Group#: %s" %uf.count)
    uf.union(1, 2)
    uf.diagFatherRelation()
    print("Group#: %s" %uf.count)
    uf.union(0, 1)
    uf.diagFatherRelation()
    print("Group#: %s" %uf.count)
