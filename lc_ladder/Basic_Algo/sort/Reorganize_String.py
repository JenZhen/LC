#!/usr/local/bin/python3

# https://leetcode.com/problems/reorganize-string/submissions/
# Example
# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].

"""
Algo:
D.S.:

Solution1:
heap 存频率和字符
每次拿出来频率最高的两个字符，频率减1，再放回heap
Time: O（n AlogA) -> n 是S 的长度，A是总共有多少种字符

Solution2：
Greedy
把频率字符map总结出来，从高频到低频排序
开辟len(S) 的数组，先填偶数位置，再填奇数位置
Time: O(N AlogA)

Corner cases:
"""

from heapq import heappush, heappop
class Solution1_heap:
    def reorganizeString(self, S: str) -> str:
        freq_list = [0] * 256
        for c in S:
            freq_list[ord(c)] += 1

        if max(freq_list) > (len(S) + 1) // 2:
            return ""

        h = []
        for i in range(len(freq_list)):
            if freq_list[i] > 0:
                heappush(h, (-freq_list[i], chr(i)))

        res = []
        while len(h) >= 2:
            f1, ch1 = heappop(h)
            f2, ch2 = heappop(h)

            res.append(ch1)
            res.append(ch2)

            if f1 < -1:
                heappush(h, (f1 + 1, ch1))
            if f2 < -1:
                heappush(h, (f2 + 1, ch2))

        if len(h) > 0:
            f, ch = heappop(h)
            res.append(ch)
        return "".join(res)

class Solution2_Greedy:
    def reorganizeString(self, S: str) -> str:
        freq_list = [0] * 256
        for c in S:
            freq_list[ord(c)] += 1

        if max(freq_list) > (len(S) + 1) // 2:
            return ""
        li = []
        for i in range(len(freq_list)):
            if freq_list[i] != 0:
                li.append((freq_list[i], chr(i)))
        li.sort(key = lambda x: (-x[0]))

        res = [None] * len(S)
        cur = 0
        for i in range(len(li)):
            cnt, char = li[i][0], li[i][1]
            for _ in range(cnt):
                if cur < len(S):
                    res[cur] = char
                    cur += 2
                else:
                    cur = 1
                    res[cur] = char
                    cur += 2
        return "".join(res)



# Test Cases
if __name__ == "__main__":
    solution = Solution()
