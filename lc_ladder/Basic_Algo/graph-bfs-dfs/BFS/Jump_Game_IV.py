#! /usr/local/bin/python3

# https://leetcode.com/problems/jump-game-iv/
# Example
# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#
# Example 1:
#
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:
#
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
# Example 3:
#
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
# Example 4:
#
# Input: arr = [6,1,9]
# Output: 2
# Example 5:
#
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
#
#
# Constraints:
#
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8

"""
Algo: BFS with optimization
D.S.:

Solution:
Classic BFS 数层 算法
注意优化！！ 否则超时

例子：
[7*,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7*,11]
对于连续的相同数字 只有第一个和最后一个7 是有意义的。
中间的7都会在最短路径上
所以在计算MAP的时候要忽略这些中间的7， 不要算在BFS计算过程中

Corner cases:
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0

        # build idx_map -- key: val, val: list of idx
        idx_map = {}
        for i in range(len(arr)):
            if arr[i] not in idx_map:
                idx_map[arr[i]] = [i]
            else:
                # optimization: keep only the head and tail if a number occurs continusouly.
                if i == 0 or arr[i] != arr[i - 1] or i == len(arr) - 1 or arr[i] != arr[i + 1]:
                    idx_map[arr[i]].append(i)
        print(idx_map)

        visited = set([0])
        q = collections.deque([0])

        step = -1
        while q:
            step += 1
            size = len(q)
            print(q)
            for _ in range(size):
                cur_idx = q.popleft()
                if cur_idx == len(arr) - 1:
                    return step

                # i - 1
                if cur_idx - 1 >= 0 and cur_idx - 1 not in visited:
                    q.append(cur_idx - 1)
                    visited.add(cur_idx - 1)
                # i + 1
                if cur_idx + 1 < len(arr) and cur_idx + 1 not in visited:
                    q.append(cur_idx + 1)
                    visited.add(cur_idx + 1)

                # check same value idx
                if arr[cur_idx] in idx_map:
                    for ele in idx_map[arr[cur_idx]]:
                        if ele not in visited:
                            q.append(ele)
                            visited.add(ele)
        return 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
