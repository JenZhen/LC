#! /usr/local/bin/python3

# https://www.lintcode.com/problem/combination-sum/description
# Example
# 给出一个候选数字的set(C)和目标数字(T),找到C中所有的组合，使找出的数字和为T。C中的数字可以无限制重复被选取。
#
# 例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：
# [7]，
# [2,2,3]
#
# 所有的数字(包括目标数字)均为正整数。
# 元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
# 解集不能包含重复的组合。
# 样例
# 给出候选set[2,3,6,7]和目标数字7
#
# 返回 [[7],[2,2,3]]

"""
Algo: 顺序无关DFS Combination
D.S.:

Solution:
不明显的前序DFS
Time: O(2 ^ n)

Follow-Up
求解的个数

Corner cases:
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or not target:
            return []

        candidates = sorted(list(set(candidates)))
        findTarget = target
        subset = []
        ans = []
        self.dfs(candidates, findTarget, 0, subset, ans)
        return ans

    def dfs(self, candidates, findTarget, startIdx, subset, ans):
        # 上一轮递归后剩下target = 0，说明是一个解
        if findTarget == 0:
            ans.append(subset[:])
            return
        # 从startIdx依次找下个可能的数
        for i in range(startIdx, len(candidates)):
            # 如果当前这数比findTarget还大，说明肯定不能加，以后的数更大，退出这次递归
            # 上一个加入的数也要pop （在上一轮解决）
            # ** 这个for loop 是固定选取元素【startIdx - 1】，然后依次只尝试startIdx -> len(candidates) - 1
            # 如果选了startIdx + 1, 说明直选了这一个，没有选startIdx, 所以这是一个重要的去重标准
            if findTarget < candidates[i]:
                return
            subset.append(candidates[i])
            # 因为index i 的数字可重复利用，下一轮递归的startIdx 还是i
            self.dfs(candidates, findTarget - candidates[i], i, subset, ans)
            subset.pop()

class Solution_similar:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or not target:
            return []

        candidates = sorted(list(set(candidates)))
        findTarget = target
        subset = []
        ans = []
        self.dfs(candidates, target, 0, subset, ans)
        return ans

    def dfs(self, candidates, target, startIdx, subset, ans):
        if sum(subset) > target:
            return
        if sum(subset) == target:
            ans.append(subset[:])
            return
        for i in range(startIdx, len(candidates)):
            subset.append(candidates[i])
            self.dfs(candidates, target, i, subset, ans)
            subset.pop()

class Solution_FollowUp:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or not target:
            return []

        candidates = sorted(list(set(candidates)))
        findTarget = target
        subset = []
        ans = []
        cnt = [0] # pass in reference using list, if integer pass in a copy
        self.dfs(candidates, findTarget, 0, subset, ans, cnt)
        print(cnt[0])
        return ans

    def dfs(self, candidates, findTarget, startIdx, subset, ans, cnt):
        # 上一轮递归后剩下target = 0，说明是一个解
        if findTarget == 0:
            ans.append(subset[:])
            cnt[0] += 1
            return
        # 从startIdx依次找下个可能的数
        for i in range(startIdx, len(candidates)):
            # 如果当前这数比findTarget还大，说明肯定不能加，以后的数更大，退出这次递归
            # 上一个加入的数也要pop （在上一轮解决）
            if findTarget < candidates[i]:
                return
            subset.append(candidates[i])
            # 因为index i 的数字可重复利用，下一轮递归的startIdx 还是i
            self.dfs(candidates, findTarget - candidates[i], i, subset, ans, cnt)
            subset.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
