#! /usr/local/bin/python3

# https://www.lintcode.com/problem/course-schedule/description
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

# Test Cases
if __name__ == "__main__":
    solution = Solution()
