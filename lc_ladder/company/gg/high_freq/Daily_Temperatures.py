#! /usr/local/bin/python3

# https://leetcode.com/problems/daily-temperatures/
# Example
# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
Algo:
D.S.: 单调栈 monotonous stack

Solution1_Suggestd:
单调递减栈
Time: O(n)
Space: O(n)

Corner cases:
"""
class Solution_Suggested:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        res = [0] * len(T)
        st = [] # put monotonous stack decreasing from left, index
        for i in range(len(T)):
            while st and T[i] > T[st[-1]]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        while st:
            res[st[-1]] = 0
            st.pop()
        return res

class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        res = [0]
        stack = [(T[-1], len(T) - 1)] # tuple (temperature, idx)
        for i in range(len(T) - 2, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()

            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)
            stack.append((T[i], i))
        return res[::-1]

class Solution3:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        res = [0]
        maxT = T[-1]
        tmap = {}
        tmap[T[-1]] = len(T) - 1
        for i in range(len(T) - 2, -1, -1):
            if T[i] >= maxT:
                res.append(0)
                maxT = T[i]
            else:
                minDist = len(T)
                for k in range(T[i] + 1, maxT + 1):
                    if k in tmap and tmap[k] - i < minDist:
                        minDist = tmap[k] - i
                res.append(minDist)
            tmap[T[i]] = i
        return res[::-1]



# Test Cases
if __name__ == "__main__":
    solution = Solution()
