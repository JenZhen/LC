#! /usr/local/bin/python3

# https://www.lintcode.com/problem/copy-books-ii/description?_from=ladder&&fromId=4
# Example
# 给出 n 本书(每本书页数一样)以及一个大小为 k 的数组，指有 k 个人来复印书本，数组中第 i 个整数表示第 i 个人复印一本书需要花费的时间，
# 且一个人只能复印连续一段编号的书 (比如第一个人可以复印第一本第二本，但是不能复印第一本第三本，因为第一本跟第三本不是连续的）返回复印所有书需要花费的最短时间。
#
# 样例
# 给出 n = 4 数组 A = [3,2,4]
# 返回4
# 第一个人用 3 分钟复印第一本书，第二个人用 4 分钟复印第二三两本书，第三个人用 4 分钟复印第四本书。

"""
Algo: rolling DP, Binary search,
D.S.: heap

Solution:
1. DP解法
1. 状态
f[i][j]：表示前i个人copy 前J本书的最短时间
2. 方程
f[i][j] = for l in range(j + 1), 遍历第i个人和第i-1个人如何分配这个，因为连续，这个过程和第i-2个人没有关系

考虑滚动数组 Space O(size_of_backpack)

[
    [0, 3, 6, 9, 12],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 4, 4]
]
可以用滚动数组优化空间，只需要2行
Time: O(k * n ^ 2)
Space: O(k * (n + 1)) -> O(2 * (n + 1))


2. 解法二：
## TODO:

Corner cases:
"""
class Solution_DP:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """

    def copyBooksII(self, n, times):
        # write your code here
        import sys
        k = len(times)
        # create f matrix k * (n + 1)
        f = [[0 for _ in range(n + 1)] for _ in range(k)]
        # init first row
        # first col are all 0s
        for j in range(n + 1):
            f[0][j] = j * times[0]

        for i in range(1, k):
            for j in range(1, n + 1):
                f[i][j] = sys.maxsize
                for l in range(j + 1):
                    # 要把下面分批的逻辑想明白
                    if f[i - 1][j - l] > times[i] * l:
                        f[i][j] = min(f[i][j], f[i - 1][j - l])
                    else:
                        f[i][j] = min(f[i][j], times[i] * l)
                        break
        print(f)
        return f[k - 1][n]


class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """

    def copyBooksII(self, n, times):
        # write your code here
        k = len(times)
        ans = 0
        eachTime = []
        totalTime = []
        for i in range(k): self.heapAdd(eachTime, totalTime, times[i], 0)
        for i in range(n):
            ans = totalTime[0]
            x = eachTime[0]
            self.heapDelete(eachTime, totalTime)
            self.heapAdd(eachTime, totalTime, x, ans+x)
        ans = 0
        for i in range(len(totalTime)): ans = max(ans, totalTime[i])
        return ans

    def heapAdd(self, eachTime, totalTime, et, tt):
        eachTime.append(et)
        totalTime.append(tt)
        n = len(eachTime)-1
        while n>0 and eachTime[n]+totalTime[n]<eachTime[(n-1)//2]+totalTime[(n-1)//2]:
            eachTime[n], eachTime[(n-1)//2] = eachTime[(n-1)//2], eachTime[n]
            totalTime[n], totalTime[(n-1)//2] = totalTime[(n-1)//2], totalTime[n]
            n = (n-1)//2

    def heapDelete(self, eachTime, totalTime):
        n = len(eachTime)-1
        if n>=0: eachTime[0] = eachTime[n]
        if n>=0: totalTime[0] = totalTime[n]
        if len(eachTime)>0: eachTime.pop()
        if len(totalTime)>0: totalTime.pop()
        n = 0
        while n*2+1<len(eachTime):
            t = n*2+1
            if t+1<len(eachTime) and eachTime[t+1]+totalTime[t+1]<eachTime[t]+totalTime[t]: t += 1
            if eachTime[n]+totalTime[n]<=eachTime[t]+totalTime[t]: break
            eachTime[n], eachTime[t] = eachTime[t], eachTime[n]
            totalTime[n], totalTime[t] = totalTime[t], totalTime[n]
            n = t


# Test Cases
if __name__ == "__main__":
    s = Solution()
