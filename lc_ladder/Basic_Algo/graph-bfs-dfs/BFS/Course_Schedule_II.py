#! /usr/local/bin/python3

# https://www.lintcode.com/problem/course-schedule-ii/description
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

"""
Algo: BFS, Topological Sorting
D.S.:

Solution:
Time: O(n ^ 2) n is numCourses

Corner cases:
1, [] -- return [0] --> VERY IMPORTANT
if numCourses == 0: return []
if no prerequisites: return course list [i for i in range(numCourses)]

if cannot take all courses, ie, len(res) != numCourses, return [] --> VERY IMPORTANT
"""

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        from collections import deque
        if not numCourses:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]

        outMap = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        for req in prerequisites:
            outMap[req[1]].append(req[0])
            inDegree[req[0]] += 1

        res = []
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        while len(q):
            cur = q.popleft()
            res.append(cur)
            for node in outMap[cur]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    q.append(node)
        if len(res) != numCourses:
            return []
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
