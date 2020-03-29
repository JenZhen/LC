#! /usr/local/bin/python3

# https://www.lintcode.com/problem/combination-sum-ii/description
# Example
# 给出一组候选数字(C)和目标数字(T),找出C中所有的组合，使组合中数字的和为T。C中每个数字在每个组合中只能使用一次。
#
# 样例
# 给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,
#
# 解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]
#
# 注意事项
# 所有的数字(包括目标数字)均为正整数。
# 元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
# 解集不能包含重复的组合。

"""
Algo: 顺序无关DFS Combination
D.S.:

Solution:
不明显的前序DFS
Time: O(2^n)

Corner cases:
"""

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        if not candidates or not target:
            return []

        candidates = sorted(candidates)
        findTarget = target
        subset = []
        ans = []
        self.dfs(candidates, findTarget, 0, subset, ans)
        return ans

    def dfs(self, candidates, findTarget, startIdx, subset, ans):
        # 前序在一开始判断是不是一个解
        if findTarget == 0:
            ans.append(subset[:])
            return
        for i in range(startIdx, len(candidates)):
            if findTarget < candidates[i]:
                return
            # 重要的去重条件
            if i != startIdx and candidates[i] == candidates[i - 1]:
                continue
            subset.append(candidates[i])
            # 不能重复去同一个元素，下一轮递归startIdx = i + 1
            self.dfs(candidates, findTarget - candidates[i], i + 1, subset, ans)
            subset.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
