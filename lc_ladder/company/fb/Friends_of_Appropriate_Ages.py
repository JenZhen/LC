#! /usr/local/bin/python3

# https://www.lintcode.com/problem/friends-of-appropriate-ages/description
# Example
# 有些人会提出好友请求。 给定他们的年龄列表，其中age[i]是第i个人的年龄。
#
# 如果满足以下任一条件，则A不会向B（B！= A）提出好友请求：
#
# age[B] <= 0.5 * age[A] +7
# age[B]>age[A]
# age[B]> 100 && age[A] <100
# 否则，A会向B发起好友请求.
# 请注意，如果A请求B，B不一定请求A。此外，人们不会向自己发出好友请求。
#
# 总共有多少好友请求被发出？
#
# Example
# 样例 1：
#
# 输入: [16,16]
# 输出: 2
# 解释: 两个人互相发出好友请求.
# 样例2：
#
# 输入: [16,17,18]
# 输出: 2
# 解释: 以下好友请求被发出 17 -> 16, 18 -> 17.
# 样例3：
#
# 输入: [20,30,100,110,120]
# 输出: 3
# 解释: 以下好友请求被发出 110 -> 100, 120 -> 110, 120 -> 100.
# Notice
# 1 <= ages.length <= 20000.
# 1 <= ages[i] <= 120.

"""
Algo: Map, 组合数
D.S.:

Solution:
这个题要注意数据规模 -- 年龄区间远小于人数，说明同一个年龄有很多重复
暴力解法：遍历每个人，看他可以向多少个人发出请求，O(n ^ 2) exceeding time limit

优化解法：
分组，每个年龄多少人
10： 10 ren
11： 20 ren
10岁向11岁发的请求有10 * 20 个
10岁向10岁发的请求有10 * （10 - 1）个，排除想自己发

Corner cases:
"""

class Solution:
    """
    @param ages:
    @return: nothing
    """
    def numFriendRequests(self, ages):
        if not ages:
            return 0

        age_cnt = {}
        for age in ages:
            age_cnt[age] = age_cnt.get(age, 0) + 1

        cnt = 0
        for a in age_cnt:
            for b in age_cnt:
                if self.request(a, b):
                    if a == b:
                        cnt += (age_cnt[a] * (age_cnt[b] - 1))
                    else:
                        cnt += age_cnt[a] * age_cnt[b]
        return cnt
    def request(self, a, b):
        return not (b <= 0.5 * a + 7 or b > a)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
