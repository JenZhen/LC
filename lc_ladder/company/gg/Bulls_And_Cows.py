#! /usr/local/bin/python3

# https://leetcode.com/problems/bulls-and-cows/submissions/
# Example
# You are playing the following Bulls and Cows game with your friend: You write down a number and
# ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.
#
# Please note that both secret number and friend's guess may contain duplicate digits.
#
# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
#
# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
#
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
# Note: You may assume that the secret number and your friend's guess only contain digits,
# and their lengths are always equal.

"""
Algo:
D.S.:

Solution:
Find intersection
Time: O(n)
Space: O(n)

Corner cases:
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # secret could be longer than guess
        if not secret or not guess: return '0A0B'

        cnt_A = 0
        idx_set = set()
        for i in range(min(len(secret), len(guess))):
            if secret[i] == guess[i]:
                cnt_A += 1
                idx_set.add(i)

        s_list = [0] * 10
        for i in range(len(secret)):
            if i in idx_set:
                continue
            s_list[int(secret[i])] += 1
        cnt_B = 0
        for i in range(len(guess)):
            if i in idx_set:
                continue
            if s_list[int(guess[i])] > 0:
                cnt_B += 1
                s_list[int(guess[i])] -= 1

        return str(cnt_A) + 'A' + str(cnt_B) + 'B'
# Test Cases
if __name__ == "__main__":
    solution = Solution()
