#!/usr/bin/python

# http://lintcode.com/en/problem/russian-doll-envelopes/
# Example
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
# the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

"""
Algo:
D.S.:

DP Solution:
After sorted by x[0] then x[1]
- State: f[i]: at position i (refer an envelope) how many layers it has at most
- Function: f[i] = max(f[i], f[j] + 1) where j = 0 -> i - 1
- Initialization:  f[] = [1] * length
- Answer: max(f)

Solution1: Sequence DP
Time: O(n ^ 2) -- loop within loop, will took too long
Space: O(n)

Solution2: TODO
Time: O(nlogn)
Space: O(n)

Corner cases:
"""

class Solution1:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        if not envelopes:
            return 0

        # sort by w (first element)
        envelopes.sort(key = lambda x : x[0])
        length = len(envelopes)
        f = [1] * length
        for i in range(1, length):
            for j in range(i):
                listI = envelopes[i]
                listJ = envelopes[j]
                if listI[0] > listJ[0] and listI[1] > listJ[1]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

class Solution2:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # Write your code here
        height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp, length = [0] * len(height), 0
        print("dp: %s" %repr(dp))
        import bisect
        for h in height:
            i = bisect.bisect_left(dp, h, 0, length)
            print("i: %s" %(i))
            dp[i] = h
            if i == length:
                length += 1
                print("length: %s" %(length))
        return length

# Test Cases
if __name__ == "__main__":
    testCases = [
        [[5,4],[6,4],[6,7],[2,3]],
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    for envelopes in testCases:
        res1 = solution1.maxEnvelopes(envelopes)
        res2 = solution2.maxEnvelopes(envelopes)
        print("res1: %s" %res1)
        print("res2: %s" %res2)
