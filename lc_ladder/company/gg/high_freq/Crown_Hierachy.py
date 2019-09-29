#! /usr/local/bin/python3

# Requirement
# Example
# 有一个king，king会有孩子，孩子还能生孩子。实现几个function：
#
# void birth(String parent, String name) 父亲名字和孩子名字，生个娃
# void death(String name) 此人要死
# List<String> getOrder() 返回当前的继承顺序，string array/list
#
#
# 讨论得知，每个人的名字是唯一的，继承顺序符合如下规律:
#
# 假设王有大皇子二皇子三皇子，大皇子有长子次子三子，那么继承顺序是王->大皇子->大皇子长子->大皇子次子->大皇子三子->二皇子->三皇子
#
# 死掉的人不能出现在继承顺序里，但是如果上面例子中大皇子死了，只需把大皇子移除，原始继承顺序保持不变：王->大皇子长子->大皇子次子->大皇子三子->二皇子->三皇子
#
# 三个function会被反复调用，实现function细节。
#
# getOrder函数的实现。一般大家好像是preorder traversel，但是看到有面试官要求O(1)实现，不知道有没有朋友有O（1）的做法？
# 用树形结构存，然后preOrder来找最先找到的非dead的node返回。如果要实现O(1)查询，可以每次调用dead()的时候把这个node从树里面删除，由它的长子来顶替它的位置，也就是说长子会成为次子的父亲。这样复杂度是amortized O(1)。
#
# https://www.1point3acres.com/bbs ... read&tid=464318
# https://www.1point3acres.com/bbs ... read&tid=429208

"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Person:
    def __init__(self, name, status = "ALIVE"):
        self.name = name
        self.children = []
        self.status = status

class Solution1:
    def __init__(self, king_name):
        self.king = Person(king_name)
        # key: person'a name, val: person's node
        self.map = {king_name: self.king}


    def give_birth(self, father_name, son_name):
        if father_name not in self.map:
            raise "Invalid name"
        father_node = self.map[father_name]
        son_node = Person(son_name)
        self.map[son_name] = son_node
        father_node.children.append(son_node)

    def die(self, name):
        if name not in self.map:
            raise "Invalid person"
        dead_person_node = self.map[name]
        dead_person_node.status = "DEAD" # meaning dead

    def get_order(self):
        res = []
        self._dfs(self.king, res)
        return res

    def _dfs(self, root_node, res):
        if not root_node:
            return
        if root_node.status == "ALIVE":
            res.append(root_node.name)
        for son in root_node.children:
            self._dfs(son, res)

##############################################

class PersonListNode:
    def __init__(self, name, status = "ALIVE"):
        self.name = name
        self.next = None
        self.status = status

class Solution2:
    def __init__(self, king_name):
        self.king_person_node = Person(king_name)
        self.king_list_node = PersonListNode(king_name)
        # key: person'a name, val: (person's node, perosn's ListNode)}
        self.map = {king_name: (self.king, self.king_list_node)}
        self.dummy_head = PersonListNode("DUMMY")

    def give_birth(self, father_name, son_name):
        if father_name not in self.map:
            raise "Invalid name"
        father_person_node, father_list_node = self.map[father_name][0], self.map[father_name][1]
        son_person_node = Person(son_name)
        son_list_node = PersonListNode(son_name)
        # add new son_person_node after father_person_node children
        father_person_node.children.append(son_person_node)
        prev_order = None
        if len(father_person_node.children) == 0:
            prev_order = father_list_node
        else:
            prev_son_name = father_person_node.children[-1].name
            prev_order = self.map[prev_son_name][1]
        # add new son_list_node after prev_order (list node)
        next_node = prev_order.next
        prev_order.next = son_list_node
        son_list_node.next = next_node

    def die(self, name):
        dead_list_node = self.map[name][1]
        dead_list_node.status = "DEAD"

    def get_order(self):
        res = []
        cur = self.dummy.next
        while cur:
            if cur.status == "ALIVE":
                res.append(cur.name)
                cur = cur.next
        return res


# Test Cases
if __name__ == "__main__":
    s1 = Solution1("King")
    ##############
    print("S1 Solution")
    s1.give_birth("King", "P1")
    s1.give_birth("King", "P2")
    s1.give_birth("King", "P3")
    print(s1.get_order())
    s1.give_birth("P1", "S1")
    print(s1.get_order())
    s1.give_birth("P1", "S2")
    s1.give_birth("P1", "S3")
    print(s1.get_order())
    s1.die("P1")
    print(s1.get_order())


    print("S1 Solution")
    s2 = Solution1("King")

    s2.give_birth("King", "P1")
    s2.give_birth("King", "P2")
    s2.give_birth("King", "P3")
    print(s2.get_order())
    s2.give_birth("P1", "S1")
    print(s2.get_order())
    s2.give_birth("P1", "S2")
    s2.give_birth("P1", "S3")
    print(s2.get_order())
    s2.die("P1")
    print(s2.get_order())
