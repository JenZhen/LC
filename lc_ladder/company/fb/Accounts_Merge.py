#! /usr/local/bin/python3

# https://www.lintcode.com/problem/accounts-merge/description
# Example
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
# Example
# Given
#
# [
#   ["John", "johnsmith@mail.com", "john00@mail.com"],
#   ["John", "johnnybravo@mail.com"],
#   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#   ["Mary", "mary@mail.com"]
# ]
# Return
#
# [
#   ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#   ["John", "johnnybravo@mail.com"],
#   ["Mary", "mary@mail.com"]
# ]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
#
# You could return these lists in any order, for example the answer
#
# [
#   ['Mary', 'mary@mail.com'],
#   ['John', 'johnnybravo@mail.com'],
#   ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
# ]
# is also acceptable.
#
# Notice
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

"""
Algo:
D.S.: Union-Find

Solution:
Time: O(nlogn) -- 最后有个排序
Space O(n)
TODO: more practice, try use array strucure of union-fine instead of dictionary structure

Corner cases:
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts or len(accounts) == 1:
            return accounts

        uf = UnionFind(len(accounts))

        # build em to id_list
        # key: em, val: [list of account ids]
        em_to_ids = self._build_em_to_id_list(accounts)
        print(em_to_ids)
        # union account
        for em, ids in em_to_ids.items():
            root_id = ids[0]
            for id in ids[1:]:
                uf.union(id, root_id)
        print(uf.father)
        # build id to em set from accounts
        # key: acct_id, val: set(emails)
        id_to_ems = self._build_id_to_ems(accounts, uf)
        # print(id_to_ems)
        # organized id_to_ems to result
        return self.reorg(id_to_ems, accounts)


    def _build_em_to_id_list(self, accounts):
        em_to_ids = {}
        for i, acct in enumerate(accounts):
            for em in acct[1:]:
                em_to_ids[em] = em_to_ids.get(em, [])
                em_to_ids[em].append(i)
        return em_to_ids

    def _build_id_to_ems(self, accounts, uf):
        id_to_ems = {}
        for i, acct in enumerate(accounts):
            root_id = uf.find(i)
            em_set = id_to_ems.get(root_id, set())
            for em in acct[1:]:
                em_set.add(em)
            id_to_ems[root_id] = em_set
        return id_to_ems

    def reorg(self, id_to_ems, accounts):
        res = []
        for id, ems in id_to_ems.items():
            name = accounts[id][0]
            em_list = sorted(ems)
            res.append([name] + em_list)
        return res

class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def union(self, a, b):
        # a's root union under b's root
        # 注意 这里是 self.find(a) 找root不是self.father[a]
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])

# Test Cases
if __name__ == "__main__":
    s = Solution()
