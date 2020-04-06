#!/usr/bin/python

# http://lintcode.com/en/problem/frog-jump/
# Example
# 一只青蛙正要过河，这条河分成了 x 个单位，每个单位可能存在石头，青蛙可以跳到石头上，但它不能跳进水里。
# 按照顺序给出石头所在的位置，判断青蛙能否到达最后一块石头所在的位置。刚开始时青蛙在第一块石头上，假设青蛙第一次跳只能跳一个单位的长度。
# 如果青蛙最后一个跳 k 个单位，那么它下一次只能跳 k - 1 ，k 或者 k + 1 个单位。注意青蛙只能向前跳。
#
# 石头的个数 >= 2并且 <=  1100。
# 每块石头的位置是一个非负数并且 < 2^31。
# 第一块石头的位置总是 0.
#
# 样例
# 给出石头的位置为 [0,1,3,5,6,8,12,17]
#
# 总共8块石头。
# 第一块石头在 0 位置，第二块石头在 1 位置，第三块石头在 3 位置等等......
# 最后一块石头在 17 位置。
#
# 返回 true。青蛙可以通过跳 1 格到第二块石头，跳 2 格到第三块石头，跳 2 格到第四块石头，跳 3 格到第六块石头，跳 4 格到第七块石头，最后跳 5 格到第八块石头。
#
# 给出石头的位置为 `[0,1,2,3,4,8,9,11]`
# 返回 false。青蛙没有办法跳到最后一块石头因为第五块石头跟第六块石头的距离太大了。

"""
Algo: Sequence DP
D.S.: DP in set

Solution:
- State:
- Function:
- Initialization:
- Answer:


Time: O(n^2)
Space: O(n^2) consider the size of the set

[0,1,3,5,6,8,12,17]
 0,1,2,2,3,3,4, 5
         1,2
each stone denotes a setup of steps it takes to get there.
for example, stone1, from 0 to 1 takes 1 step, from 1 can take 0, 1, or 2 steps:
    0 stays at 1, 1 to stone2(not exist), 2 to stone3, fill stone3 set with 2
iterate through all stones, if the last stone's set is empyt, then not reachable.


Corner cases:
"""
class Solution_cleaner:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return False

        f = {}
        for s in stones:
            f[s] = set()
        f[stones[0]].add(0)

        for s in stones:
            for step in f[s]:
                for delta in range(-1, 2):
                    diff = step + delta
                    if diff > 0 and s + diff in f:
                        # only care diff > 0 move forward not backward or staying
                        f[s + diff].add(diff)
        return len(f[stones[-1]]) > 0



class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        #    [0,1,3,5,6,8,12,17]
        # f[0] = {0} (set) init as 0. It can only go forward as k + 1 = 1 steps
        # f[1] = {}
        # ...
        # f[8] = {}
        f = {} # dict
        for stone in stones:
            f[stone] = set() # init a set
        f[0].add(0)

        for stone in stones:
            for k in f[stone]:
                # k - 1
                if k - 1 > 0 and stone + k - 1 in f:
                    f[stone + k - 1].add(k - 1)
                # k
                if k > 0 and stone + k in f:
                    f[stone + k].add(k)
                # k + 1
                if stone + k + 1 in f:
                    f[stone + k + 1].add(k + 1)
        return len(f[stones[-1]]) > 0

# Test Cases
if __name__ == "__main__":
    testCases = [
        [0,1,3,5,6,8,12,17], # True
        [0,1,2,3,4,8,9,11]   # False
    ]

    solution = Solution()
    for stones in testCases:
        res = solution.canCross(stones)
        print("Res: %s" %res)
