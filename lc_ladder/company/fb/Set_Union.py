#! /usr/local/bin/python3

# https://www.lintcode.com/problem/set-union/description
# Example

# 有一个集合组成的list，如果有两个集合有相同的元素，将他们合并。返回最后还剩下几个集合。
#
# Example
# 样例1:
#
# 输入：list = [[1,2,3],[3,9,7],[4,5,10]]
# 输出：2 .
# 样例：剩下[1,2,3,9,7]和[4,5,10]这2个集合。
# 样例 2:
#
# 输入：list = [[1],[1,2,3],[4],[8,7,4,5]]
# 输出 ：2
# 解释：剩下[1,2,3]和[4,5,7,8] 2个集合。
# Notice
# 集合数 n <= 1000。
# 每个集合的元素个数 m <= 100。
# 元素一定是非负整数，且不大于 100000。


"""
Algo: Union find
D.S.:

Solution:
当不连续，区间不一定的情况下，不适宜用array index 来表示父子关系，可以用map
这里注意是如何计算group个数的 -- 暴力，直接过一遍所有的father 数set里元素个数

Time: O(n) -- n is total elements in all sets
Space: O(n) -- n is total elements in all sets
Corner cases:
"""

class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        father = {}
        for s in sets:
            first_in_set = s[0]
            for i in s:
                if i not in father:
                    father[i] = first_in_set
                else:
                    father_of_first = self.find(first_in_set, father)
                    father_of_cur = self.find(i, father)
                    if father_of_cur != father_of_first:
                        father[father_of_cur] = father_of_first

        group = set()
        for s in sets:
            for i in s:
                group.add(self.find(i, father))
        return len(group)

    def find(self, node, father):
        if father[node] == node:
            return node
        father[node] = self.find(father[node], father)
        return father[node]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
