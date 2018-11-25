#!/usr/bin/python

# http://lintcode.com/en/problem/jump-game-ii/
# Example
# 给出一个非负整数数组，你最初定位在数组的第一个位置。
#
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)

"""
Algo: Sequence DP
D.S.:

Solution:
Same as Jump Game 1
- State:
- Function:
- Initialization:
- Answer:

Solution1: DP
Time: O(n ^ 2)
Space: O(n)

Solution2: Greedy
Time: O(n)

Corner cases:
"""

class Solution_DP:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A or len(A) == 1:
            return 0
        length = len(A)
        f = [0] * length
        for i in range(1, length):
            for j in range(i):
                if A[j] < i - j:
                    # not reachable
                    continue
                else:
                    if f[i] == 0:
                        f[i] = f[j] + 1
                    else:
                        f[i] = min(f[i], f[j] + 1) # 之前怎么用几步跳来的就重要了，只保留最小的就行
        return f[length - 1]

# Greedy -- not obvious
class Solution2_Greedy:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A or len(A) == 1:
            return 0
        length = len(A)
        start, end, jump = 0, 0, 0
        while (end < length - 1):
            jump += 1
            farthest = end
            for i in range(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i
            start = end + 1
            end = farthest
        return jump
# Test Cases
if __name__ == "__main__":
    solution = Solution()
