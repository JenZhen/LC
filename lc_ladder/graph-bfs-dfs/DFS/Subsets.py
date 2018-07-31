#! /usr/local/bin/python3

# https://www.lintcode.com/problem/subsets/description
# Example

"""
Algo: DFS, BFS
D.S.: DFS: array; BFS: queue

Solution:
1. DFS
Tree: [1, 2, 3]
            []
    [1],    [2],    [3]
[1,2] [1,3] [2,3]
[1,2,3]
Complexity:
Time: 经典的计算复杂度的公式 O(构造解的复杂度 * 解的个数)
O(n * 2 ^ n) --
Space: O(2 ^ n)

result 里面subsets的order靠dfs/bfs的搜索顺序
每个subsets里面的顺序靠nums.sort()

Solution1:
print order: 中序遍历顺序
get temp: []
get temp: [1]
get temp: [1, 2]
get temp: [1, 2, 3]
get temp: [1, 3]
get temp: [2]
get temp: [2, 3]
get temp: [3]  

Solution2:
print order: 前序遍历顺序
get temp: [1, 2, 3]
get temp: [1, 2]
get temp: [1, 3]
get temp: [1]
get temp: [2, 3]
get temp: [2]
get temp: [3]
get temp: []

2. BFS:

Solution3:
print order: level order
add []
add [1]
add [2]
add [3]
add [1, 2]
add [1, 3]
add [2, 3]
add [1, 2, 3]

Solution4:
Same BFS level order not using queue
Similar to # # TODO:
print order:
add []
add [1]
add [2]
add [1, 2]
add [3]
add [1, 3]
add [2, 3]
add [1, 2, 3]

Corner cases:
"""

class Solution1:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res
        nums.sort()
        self.dfs(nums, [], 0, res)
        return res

    def dfs(self, nums, temp, idx, res):
        res.append(temp[:])
        print("get temp: %s" %repr(temp))
        # this loop defines the exit of dfs
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, temp, i + 1, res)
            temp.pop()


class Solution2:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res
        nums.sort()
        self.dfs(nums, [], 0, res)
        return res

    def dfs(self, nums, temp, idx, res):
        # exit: this branch has search till the end
        # ie. idx == len(nums)
        if idx == len(nums):
            res.append(temp[:])
            print("get temp: %s" %repr(temp))
            return
        # select nums[idx]
        temp.append(nums[idx])
        # to next level
        self.dfs(nums, temp, idx + 1, res)
        # select nums[idx]
        temp.pop()
        # to next level
        self.dfs(nums, temp, idx + 1, res)

class Solution3:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        from collections import deque
        res = []
        if nums is None:
            return res
        nums.sort()
        q = deque([])
        q.append([])
        while len(q):
            cur = q.popleft()
            res.append(cur)
            print("add %s" %repr(cur))
            for i in range(len(nums)):
                if len(cur) == 0 or cur[-1] < nums[i]:
                    temp = cur[:]
                    temp.append(nums[i])
                    q.append(temp)
        return res

class Solution4:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        if nums is None:
            return res
        nums.sort()
        res.append([])
        for i in range(len(nums)):
            size = len(res)
            for j in range(size):
                newEle = res[j][:]
                newEle.append(nums[i])
                res.append(newEle)
                print("add %s" %repr(newEle))
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
