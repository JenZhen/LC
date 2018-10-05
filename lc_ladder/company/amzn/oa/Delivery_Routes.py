#! /usr/local/bin/python3

# Requirement
# Example
# 无人机有最大里程，然后给了两个list，分别是出发和返回的里程数，数据类型是List<List<Integer>>，list里面只有id和里程两个值，
# 要求找出所有出发和返回里程数之和最接近无人机最大里程的pair。
# 比如，
# 最大里程M = 11000，
# forwarding = [[1, 1000],[2, 7000],[3, 12000]],
# retrun = [[1, 10000],[2, 9000],[3, 3000],[4, 2000]],
# 最接近的里程和是10000，所以结果是[[1, 2],[2, 3]]..
#
# 思路：先用两个list sort一下，因为题目里没说给的list是sort好的，然后用two pointers找到最接近的里程，
# 接着把return list里的id和里程的关系放到hashmap里，用two sum的解法就弄出来了。这题test cases全过了。

"""
Algo: Two pointers
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param maxDist: Integer
    @param forw: an array
    @param ret: an array
    @return: possible longest delivery routes
    """
    def longestRoutes(self, maxDist, forw, ret):
        res = []
        if not maxDist or not forw or not ret:
            return res
        forw = sorted(forw, key=lambda x:x[1])
        ret = sorted(ret, key=lambda x:x[1])

        import sys
        canDoDist = -sys.maxsize
        i, j = len(forw) - 1, 0
        while i >= 0 and j <= len(ret) - 1:
            ttl = forw[i][1] + ret[j][1]
            if ttl < canDoDist:
                j += 1
            elif canDoDist <= ttl <= maxDist:
                canDoDist = ttl
                j += 1
            else:
                i -= 1

        i, j = len(forw) - 1, 0
        while i >= 0 and j <= len(ret) - 1:
            ttl = forw[i][1] + ret[j][1]
            if ttl < canDoDist:
                j += 1
            elif ttl > canDoDist:
                i -= 1
            else:
                res.append([forw[i][0], ret[j][0]])
                i -= 1
                j += 1
        return res

# Test Cases
if __name__ == "__main__":
    testCases = [
        {
            "maxDist": 10000,
            "forw": [[1, 1000],[2, 7000],[3, 12000]],
            "ret": [[1, 10000],[2, 9000],[3, 3000],[4, 4200]]
        },
        {
            "maxDist": 9000,
            "forw": [[1, 1000],[2, 6000],[3, 12000]],
            "ret": [[1, 10000],[2, 5000],[3, 3000],[4, 4200]]
        },
    ]
    solution = Solution()
    for t in testCases:
        res = solution.longestRoutes(t["maxDist"], t["forw"], t["ret"])
        print("Res: %s" %repr(res))
