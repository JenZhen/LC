#! /usr/local/bin/python3

# https://leetcode.com/problems/stone-game-iii/
# LT;DR:
# A, B两人轮流取石碓
# 每人每次可以从 1 or 2 or 3 堆
# 目标 最后总和数最大
# 返回 谁能赢，还是平局，return ’A' or 'B' or 'Tie' 注意这里可以有负数 所以不是拿越多越好

# Alice and Bob continue their games with piles of stones. There are several stones arranged in a row,
# and each stone has an associated value which is an integer given in the array stoneValue.
#
# Alice and Bob take turns, with Alice starting first.
# On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.
# The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.
#
# The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie.
# The game continues until all the stones have been taken.
#
# Assume Alice and Bob play optimally.
# Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.
#
#
# Example 1:
# Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
# Example 2:
# Input: values = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
# Remember that both play optimally so here Alice will choose the scenario that makes her win.
# Example 3:
# Input: values = [1,2,3,6]
# Output: "Tie"
# Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
# Example 4:
# Input: values = [1,2,3,-1,-2,-3,7]
# Output: "Alice"
# Example 5:
# Input: values = [-1,-2,-3]
# Output: "Tie"
#
# Constraints:
#
# 1 <= values.length <= 50000
# -1000 <= values[i] <= 1000
"""
Algo: DP
D.S.:

Solution:
Same as stone game ii

self.memo - start from idx i, best most can take
dfs(stonevalue, start_idx) -- 从start_idx开始 能赢多少

Time: O(n) n * 3
Space: O(n)

Corner cases:
"""

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # start from idx i, best most can take
        self.memo = [None for _ in range(n)]
        self.dfs(stoneValue, 0)
        print(self.memo)
        if self.memo[0] > 0:
            return 'Alice'
        elif self.memo[0] == 0:
            return 'Tie'
        else:
            return 'Bob'

    def dfs(self, stoneValue, start_idx):
        if start_idx >= len(stoneValue):
            return 0

        if start_idx == len(stoneValue) - 1:
            # 只能拿最后一个
            self.memo[start_idx] = stoneValue[start_idx]
            return self.memo[start_idx]
        if self.memo[start_idx] is not None:
            return self.memo[start_idx]

        best = -sys.maxsize
        cur = 0
        for k in [1, 2, 3]:
            if start_idx + k - 1 >= len(stoneValue):
                break
            cur += stoneValue[start_idx + k - 1]
            best = max(best, cur - self.dfs(stoneValue, start_idx + k))
        self.memo[start_idx] = best
        return self.memo[start_idx]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
