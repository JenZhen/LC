#! /usr/local/bin/python3

# https://leetcode.com/problems/diagonal-traverse-ii/
# Example
# Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
#
# Example 1:
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
#
# Example 2:
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
# Example 3:
# Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# Output: [1,4,2,5,3,8,6,9,7,10,11]
#
# Example 4:
# Input: nums = [[1,2,3,4,5,6]]
# Output: [1,2,3,4,5,6]
#
# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.
"""
Algo: BFS
D.S.:

Solution:
BFS
Time: O(N) -- all valid space
Space: O(N) -- visited

Old traverse way
not efficient TLE when there are a lot of empty spaces
[1]
[2]
[1,2,3]

Corner cases:
"""
class Solution_BFS:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums or not nums[0]:
            return []
        m = len(nums)
        n = max([len(nums[i]) for i in range(m)])
        q = collections.deque([(0, 0)])
        visited = set(['0.0'])
        dirs = [(1, 0), (0, 1)]
        res = []
        while q:
            x, y = q.popleft()
            res.append(nums[x][y])
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < len(nums[nx]) and str(nx) + '.' + str(ny) not in visited:
                    q.append((nx, ny))
                    visited.add(str(nx) + '.' + str(ny))
        return res

class Solution_TLE:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums or not nums[0]:
            return []
        m = len(nums)
        n = max([len(nums[i]) for i in range(m)])

        res = []
        for i in range(m):
            x, y = i, 0
            tmp = []
            while 0 <= x < m and 0 <= y < n:
                if y < len(nums[x]):
                    tmp.append(nums[x][y])
                x -= 1
                y += 1
            res.extend(tmp)

        for j in range(1, n):
            x, y = m - 1, j
            tmp = []
            while 0 <= x < m and 0 <= y < n:
                if y < len(nums[x]):
                    tmp.append(nums[x][y])
                x -= 1
                y += 1
            res.extend(tmp)
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
