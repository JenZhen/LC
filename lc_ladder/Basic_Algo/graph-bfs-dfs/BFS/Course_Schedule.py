#! /usr/local/bin/python3

# https://www.lintcode.com/problem/course-schedule/description
# https://leetcode.com/problems/course-schedule/submissions/c
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# Example
# Given n = 2, prerequisites = [[1,0]]
# Return true
# Given n = 2, prerequisites = [[1,0],[0,1]]
# Return false

"""
Algo: BFS, Topological Sorting
D.S.:

Solution:
Time: O(n ^ 2)
- Go over prerequisites: n courses, any two courses could have a relation, n ^ 2
- Other iteration is just O(numCourses) ie O(n)

Corner cases:
10
[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
IMPORTANT: Use list in stead of set() in outMap, in case of duplicate as [1, 9] [1, 9]
1's inDegree would count twice, 9's outMap list would contain two 1

Solution2:
DFS (not recommended)
"""

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        from collections import deque
        if not numCourses or not prerequisites:
            return True

        # step1: re-org data
        # outMap: [[]], outMap[i] courses that have i as prerequisite
        # inDegree: [], inDegree[i] course i has how many prerequisite
        outMap = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        for req in prerequisites:
            inDegree[req[0]] += 1
            outMap[req[1]].append(req[0])

        cnt = 0
        # step2: if inDegree[i] == 0, meaning i has no inDegree, ie, no prerequisite
        # i could be a startin course, put in queue
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        # step3: BFS
        while len(q):
            cur = q.popleft()
            cnt += 1
            for node in outMap[cur]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    q.append(node)
        return cnt == numCourses


class Solution_DFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        outMap = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            outMap[v].append(u)

        visited = [False for _ in range(numCourses)]
        checkCycle = [False for _ in range(numCourses)] # starting for node i if has cycle
        for i in range(numCourses):
            if visited[i] == True or self.hasCycle(outMap, visited, i, checkCycle):
                return False
        return True

    def hasCycle(self, outMap, visited, curCourse, checkCycle):
        if checkCycle[curCourse]: return False
        visited[curCourse] = True
        for next_course in outMap[curCourse]:
            if visited[next_course] or self.hasCycle(outMap, visited, next_course, checkCycle):
                return False
        visited[curCourse] = False
        checkCycle[curCourse] = False
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
