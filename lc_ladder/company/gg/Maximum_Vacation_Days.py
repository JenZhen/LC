#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-vacation-days/description?_from=ladder&&fromId=18
# Example
# LintCode想让它最好的员工之一选择在N个城市间旅行来收集算法问题。但是只工作不玩耍，聪明的孩子也会变傻，你可以在某些特定的城市并且一个星期里去度假。你的工作是安排旅行，尽可能多的假期，但是有一些规则和限制你需要遵守。
# 规则和限制:
# 您只能在1个城市中旅行，由0到N-1的索引表示。一开始，你周一在城市0。
# 这些城市都是通过航班连接起来的。这些航班被表示为N*N矩阵(非必要对称)，称为代表航空公司从城市i到j城市状态的flights矩阵。如果没有从城市i到城市j的航班，flights[i][j] = 0;否则,flights[i][j]= 1。还有，flights[i][i] = 0。
# 你总共有K周(每周有7天)旅行。你只能每天最多乘坐一次航班，而且只能在每周一早上乘坐航班。由于飞行时间太短，我们不考虑飞行时间的影响。
# 对于每个城市，你只能在不同的星期里限制休假日，给定一个命名为days的N*K矩阵表示这种关系。对于days[i][j]的值，它表示你可以在j周的城市i里休假的最长天数，你得到的是flights矩阵和days矩阵，你需要输出你在K周期间可以获得的最长假期。
#
# 样例
# 给定 flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]], 返回 12.
#
# 解释：
# Ans = 6 + 3 + 3 = 12.
#
# 最好的策略之一是:
# 第一周:周一从城市0飞往城市1，休假6天，工作1天。
# (虽然你从城市0开始，但从周一开始，我们也可以飞到其他城市去。)
# 第二周:周一从城市1飞到城市2，休假3天，工作4天。
# 第三周:呆在城市2，休假3天，工作4天。
# 给定 flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]], 返回 3.
#
# 解释：
# Ans = 1 + 1 + 1 = 3.
#
# 因为没有航班可以让你飞到另一个城市，所以你必须在城市里呆3个星期。
# 每个星期，你只有一天休假的时间和六天的工作。
# 所以假期的最大天数是3
# 给定 flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]], 返回 21.
#
# 解释：
# Ans = 7 + 7 + 7 = 21.
#
# 最好的策略之一是:
# 第一周:呆在城市0，玩7天。
# 第二周:周一从城市0飞到城市1，然后休假7天。
# 第三周:周一从城市1飞到城市2，然后休假7天。
# 注意事项
# N和K是正整数，它们在[1, 100]的范围内。
# 在flights矩阵中，所有的值都是在[0, 1]范围内的整数。
# 在days矩阵中，所有的值都是范围内的整数[0, 7]。
# 你可以呆在一个超过假期天数的城市，但是你应该多工作几天，这不会算作休假日。
# 如果你从A市飞到B市，并在那天休假，那么假期的扣除将计入B城市的假期天数。
# 我们不考虑飞行时间对计算假期的影响。

"""
Algo: DP, DFS
D.S.:

Solution:
1. 2. DP
 - DP1 技巧 倒着推导
Time: O(n ^ 2 * k)
3. DFS ?

Corner cases:
注意：
- flight 是有向的
- 不能用dp[i][week - 1] 来作为之前是否可以走到的标志

"""


class Solution_DP1:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """
    def maxVacationDays(self, flights, days):
        # Write your code here
        if not flights or not days:
            return 0

        nWeeks = len(days[0]) # col
        nCities = len(days) # row

        dp = [[0 for _ in range(nWeeks)] for _ in range(nCities)]

        # init last col same as days last col
        for i in range(nCities):
            dp[i][nWeeks - 1] = days[i][nWeeks - 1]

        # dp process, col by col backwards
        for j in range(nWeeks - 2, -1, -1):
            for i in range(nCities):
                dp[i][j] = days[i][j] + self.getMaxDays(flights, dp, i, j + 1)
        # make sure to get it again instead of using
        self.print(dp)
        return self.getMaxDays(flights, dp, 0, 0)

    def getMaxDays(self, flights, dp, city, week):
        maxDay = dp[city][week] # start with the fromWeek, meaning no travel
        for i in range(len(flights)):
            if flights[city][i] == 1: # if city i can fly to desCity, fromWeek of city i to desCity
                maxDay = max(maxDay, dp[i][week])
        return maxDay

    def print(self, dp):
        for i in range(len(dp)):
            print(dp[i])

class Solution_DP2:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """
    def maxVacationDays(self, flights, days):
        # Write your code here
        if not flights or not days:
            return 0

        nWeeks = len(days[0]) # col
        nCities = len(days) # row

        dp = [[0 for _ in range(nWeeks)] for _ in range(nCities)]
        visited = [[False for _ in range(nWeeks)] for _ in range(nCities)]
        # init first city, first week as it is in days
        dp[0][0] = days[0][0]
        visited[0][0] = True
        # init other rows of first col as if accessible from city 0
        for i in range(1, nCities):
            # from city 0 to city 0
            if flights[0][i] == 1:
                dp[i][0] = days[i][0]
                visited[i][0] = True

        # dp process, col by col forwards
        for j in range(1, nWeeks):
            for i in range(nCities):
                dp[i][j] = self.getMaxDays(flights, days, visited, dp, i, j)

        self.print(dp)
        self.print(visited)
        return max([dp[i][nWeeks - 1] for i in range(nCities)])

    def getMaxDays(self, flights, days, visited, dp, city, week):
        maxDay = 0
        for i in range(len(days)):
            if i == city: # if coming staying same city of pre week
                # maxDay = max(maxDay, days[i][week] + dp[i][week - 1] if dp[i][week - 1] != 0 else 0)
                if visited[i][week - 1] == False:
                    maxDay = max(maxDay, 0)
                else:
                    maxDay = max(maxDay, days[city][week] + dp[i][week - 1])
                    visited[city][week] = True
                    # print("*[%s, %s]: %s" %(city, week, maxDay))
            # from city i to destination city
            if flights[i][city] == 1:
                maxDay = max(maxDay, days[city][week] + dp[i][week - 1])
                visited[city][week] = True
                # print("**[%s, %s]: %s" %(city, week, maxDay))
        # print("[%s, %s]: %s" %(city, week, maxDay))
        return maxDay

    def print(self, dp):
        for i in range(len(dp)):
            print(dp[i])

class Solution_DFS:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """
    def maxVacationDays(self, flights, days):
        # Write your code here
        if not flights or not days:
            return 0

        NCities = len(flights)
        KWeeks = len(days[0])
        memo = {} # key: (city, week) pair, val: maxDay of it

        # start from city 0 and week 0
        return self.dfs(0, 0, flights, days, NCities, KWeeks, memo)

    def dfs(self, city, week, flights, days, NCities, KWeeks, memo):
        if (city, week) in memo:
            return memo[(city, week)]

        if week == KWeeks:
            return 0
        # Calculate the maxDay for (city, week)
        maxDay = 0
        for i in range(NCities):
            # we could either stay in current city or fly to other city at current week
                            # from city to city_i
            if i == city or flights[city][i] == 1:
                # update maxDay using the result for next week
                maxDay = max(maxDay, days[i][week] + self.dfs(i, week + 1, flights, days, NCities, KWeeks, memo))

        memo[(city, week)] = maxDay
        return maxDay
# Test Cases
if __name__ == "__main__":
    solution = Solution()
