#! /usr/local/bin/python3

# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/submissions/
# Example
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
# Example 1:
#
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:
#
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false´
# Explanation: No possible partition.
# Example 3:
#
# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
# Example 4:
#
# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
# Example 5:
#
# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
#
#
# Constraints:
#
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4
"""
Algo: math， GCD
D.S.:

Solution:
分组 求出现频率
找频率的 大公约数 如果有这么一个数 且大于2， 就可以返回True

Corner cases:
[1,1,1,1,2,2,2,2,2,2] x = 2 x 是 4， 6 的最大公约数
[1,1,2,2,2,2] x = 2 x 是 4， 2 的最大公约数
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck: return False
        counter = {}
        for i in deck:
            cnt = counter.get(i, 0)
            counter[i] = cnt + 1

        cnt_list = [cnt for i, cnt in counter.items()]
        min_cnt = min(cnt_list)
        if min_cnt == 1:
            return False

        for i in range(2, min_cnt + 1):
            isGCD = True
            for c in cnt_list:
                if c % i != 0:
                    isGCD = False
                    break # break inner for, next i
            if isGCD:
                return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
