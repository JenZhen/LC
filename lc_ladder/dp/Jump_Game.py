#!/usr/bin/python

# http://lintcode.com/en/problem/jump-game/
# Example
# 给出一个非负整数数组，你最初定位在数组的第一个位置。　　　
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　
# 判断你是否能到达数组的最后一个位置。
# 这个问题有两个方法，一个是贪心和 动态规划。
# 贪心方法时间复杂度为O（N）。
# 动态规划方法的时间复杂度为为O（n^2）。
#
# 我们手动设置小型数据集，使大家可以通过测试的两种方式。这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。
# 如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。

"""
Algo: Sequence DP
D.S.:

Solution:
- State: f[i]: True/False, if position i can be reached
- Function: When at i, checking range A[i], if position is reachable f[j] = True
            If at i, f[i] is False, then all after i will be False, return False
            If at i, reachale to last element, return True directly.
- Initialization: f[i] = False f[0] = True
- Answer: f[length - 1]

Solution1: DP
Time: O(n ^ 2)
Space: O(n)

Solution2: Greedy
Time: O(n)
Corner cases:
"""

class Solution1_DP:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        length = len(A)
        # init f an array of length, f[0] = True, else False
        f = [False] * length
        f[0] = True

        # Iterate to update f value
        for i in range(length):
            if f[i] == False:
                return False
            # if from i can reach out the position length - 1, return True
            if A[i] >= length - 1 - i:
                return True
            for j in range(1, A[i] + 1):
                f[i + j] = True
        # return f[length - 1] This will not be executed


def repr(arr):
    joinArr = ", ".join([str(ele) for ele in arr])
    print("[%s]" %(joinArr))


class Solution2_Greedy:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        length = len(A)

        farthestPos = A[0]
        for i in range(1, length):
            if i <= farthestPos:
                # see if farthest to be updated
                farthestPos = max(farthestPos, A[i] + i)
            else:
                # i is not reachable
                return False
        return farthestPos >= length - 1


# Test Cases
if __name__ == "__main__":
    testCases = [
        [2,3,1,1,4], # True
        [3,2,1,0,4], # False
        [0,8,2,0,9], # False
        [1,1,0,1],   # False
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    for A in testCases:
        res1 = solution1.canJump(A)
        print("res1: %s" %res1)

        res2 = solution2.canJump(A)
        print("res2: %s" %res2)
