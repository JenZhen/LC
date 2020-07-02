#! /usr/local/bin/python3

# https://leetcode.com/problems/hand-of-straights/
# Example
# Alice has a hand of cards, given as an array of integers.
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
# Return true if and only if she can.
#
# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
# Constraints:
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
# Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""
Algo:
D.S.: TreeMap, counter, map, ordered map

Solution:
Time: O(nlogn)

Corner cases:
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = {} #key: card, val: counter
        for card in hand:
            cnt = counter.get(card, 0)
            counter[card] = cnt + 1

        for card in sorted(set(hand)):
            if counter[card]:
                # card 是顺子最小的牌
                cnt = counter[card]
                for i in range(W):
                    if card + i not in counter:
                        return False
                    counter[card + i] -= cnt
                    if counter[card + i] < 0:
                        return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
