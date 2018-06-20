#! /usr/local/bin/python3

# https://www.lintcode.com/problem/course-schedule-ii/description
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example
# Given n = 2, prerequisites = [[1,0]]
# Return [0,1]
# Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
# Return [0,1,2,3] or [0,2,1,3]

"""
Algo: BFS, Topological Sorting
D.S.:

Solution:
Time: O(n ^ 2) n is numCourses

Corner cases:
1, [] -- return [0]
if numCourses == 0: return []
if no prerequisites: return course list [i for i in range(numCourses)]

if cannot take all courses, ie, len(res) != numCourses, return []
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
