#! /usr/local/bin/python3

# https://www.lintcode.com/problem/find-the-celebrity/description
# Example
# 假设你和 n 个人在一个聚会中(标记为 0 到 n - 1)，其中可能存在一个名人。名人的定义是所有其他 n - 1 人都认识他/她，但他/她不知道任何一个。
# 现在你想要找出这个名人是谁或者验证这个名人不存在。你唯一可以做的事情就是提出如下问题：“你好，A，你认识B吗？” 来获取A是否认识B。您需要通过询问尽可能少的问题(以渐近的意义)来找出名人是谁(或验证其不存在)。
# 你得到一个辅助函数 bool know(a，b)，它会告诉你A是否知道B.实现一个函数 int findCelebrity(n)，你的函数应该使 knows 的调用次数最少。
#
# 样例
# 样例1
#
# 输入：
# 2 // 接下来n*(n-1)行
# 0 knows 1
# 1 does not know 0
# 输出： 1
# 解释：
# 所有人都认识1，而且1不认识其他人。
# 样例2
#
# 输入：
# 3 // 接下来n*(n-1)行
# 0 does not know 1
# 0 does not know 2
# 1 knows 0
# 1 does not know 2
# 2 knows 0
# 2 knows 1
# 输出：0
# 解释：
# 所有人都认识0，而且0不认识其他人。
# 0不认识1，同时1认识0。
# 2认识所有人，但是1不认识2。
# 注意事项
# 如果在这个聚会中有名人， 那么有且只有一个。如果有名人在聚会中则返回名人的标签，如果没有名人，返回 -1。
"""
Algo: graph, edge search
D.S.:

Solution:
重点高频！！

如果有有向图 拓扑排序
Time: O(n ^2)

最优解如下，Time: O(n)

Corner cases:
"""


"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        if not n:
            return -1
        # 先去找到一个可能的名人
        celeb = 0
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i
        # 再去搜一遍，拿这个candidate 和其他人依次比较，如果被排除就没有candidate
        for i in range(n):
            if celeb != i and Celebrity.knows(celeb, i):
                return -1
            if celeb != i and not Celebrity.knows(i, celeb):
                return -1
        return celeb

# Test Cases
if __name__ == "__main__":
    solution = Solution()
