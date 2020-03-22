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
Time: O(n) Space O(n)
TODO: more practice, try use array strucure of union-fine instead of dictionary structure

Corner cases:
"""
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        if not accounts or len(accounts) == 1:
            return accounts

        self.init(len(accounts))
        # email_to_ids -- key: email, val: [ids]
        email_to_ids = self.get_email_to_ids(accounts)
        # union
        for email, ids in email_to_ids.items():
            root_id = ids[0] # a email mapps to n ids, use first one as root_id
            for id in ids[1:]:
                self.union(id, root_id) # merge other id to root_id

        # id_to_email_set -- key: id, val: {emails}
        id_to_email_set = self.get_id_to_email_set(accounts)
        print("set: %s" %repr(id_to_email_set))

        merged_accounts = []
        for id, email_set in id_to_email_set.items():
            merged_accounts.append([
                accounts[id][0],
                *sorted(email_set)
            ])
        return merged_accounts

    def get_email_to_ids(self, accounts):
        # key: email, val: [ids]
        email_to_ids = {}
        for id, account in enumerate(accounts):
            # i : 0 -> n, i denotes id for user, a user may have more than one id
            for email in account[1:]:
                email_to_ids[email] = email_to_ids.get(email, [])
                email_to_ids[email].append(id)
        return email_to_ids

    def get_id_to_email_set(self, accounts):
        id_to_email_set = {}
        for id, account in enumerate(accounts):
            root_id = self.find(id)
            email_set = id_to_email_set.get(root_id, set())
            for email in account[1:]:
                email_set.add(email)
            id_to_email_set[root_id] = email_set
        return id_to_email_set

    def init(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i

    def union(self, id, root_id):
        # find id's father and root_id's father
        # id's father's father is root_id's father
        self.father[self.find(id)] = self.find(root_id)

    def find(self, id):
        path = []
        while id != self.father[id]:
            path.append(id)
            id = self.father[id]
        # compress all
        # all nodes in the path should have the same father
        for node in path:
            self.father[node] = id
        return id
# Test Cases
if __name__ == "__main__":
    s = Solution()
