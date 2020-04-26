#! /usr/local/bin/python3

# https://www.lintcode.com/problem/heaters/description?_from=ladder&&fromId=18
# Example
# 冬天来啦！你的任务是设计出一个具有固定加热半径的加热器，使得所有房屋在这个冬天不至于太冷。
#
# 现在你能够获知所有房屋和加热器所处的位置，它们均分布在一条水平线中。你需要找出最小的加热半径使得所有房屋都处在至少一个加热器的加热范围内。
#
# 所以，你的输入将会是所有房屋和加热器所处的位置，期望输出为加热器最小的加热半径。
#
# 样例
# 样例1：
#
# 输入：[1,2,3],[2]
# 输出：1
# 说明：唯一的一个加热器被放在2的位置，那么只要加热半径为1，就能覆盖到所有房屋了。
# 样例2：
#
# 输入：[1,2,3,4],[1,4]
# 输出：1
# 说明：两个加热器分别位于1和4，只需要加热半径为1，就能加热所有房屋了。
# 注意事项
# 房屋和加热器的数目均为非负整数，并且它们不会超过25000。
# 房屋和加热器的位置均为非负整数，并且它们不会超过10^9。
# 只要一间房屋位于加热器的加热半径内（包括边界），它就会被加热。
# 所有加热器的加热半径相同。


"""
Algo:
D.S.:

Solution:
solution1: AC
Time: O(nlogn) for sort, core part: O(n)
solution2: exceed time limit
Time: O(n) i think so...
solution3: ERROR
not sure what corner cases not covered.
Time: O(n)


Corner cases:
"""

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        houses.sort()
        heaters.sort()
        maxidx = 0 # result radius
        index = 0 # heaters list index
        for i in range(len(houses)):
            while index + 1 < len(heaters) and \
                    # 如果后一个idx 的距离小于前一个idx的距离
                    (abs(heaters[index + 1] - houses[i]) < abs(heaters[index] - houses[i])):
                index += 1
            maxidx = max(maxidx, abs(heaters[index] - houses[i]))
        return maxidx

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        import sys
        if not houses or not heaters:
            return 0
        houses.sort()
        heaters.sort()
        startHeater, res = 0, 0
        for i in range(len(houses)):
            tempMin = sys.maxsize
            for j in range(startHeater, len(heaters)):
                if abs(houses[i] - heaters[j]) < tempMin:
                    startHeater = j
                    tempMin = abs(houses[i] - heaters[j])
            res = max(res, tempMin)
        return res


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        if not houses or not heaters:
            return 0
        houses.sort()
        heaters.sort()
        rge = [heaters[0] - 1, len(houses) - heaters[0]]
        for i in range(1, len(heaters)):
            # left range is to share with previous left heater
            leftRange = (heaters[i] - heaters[i - 1]) // 2
            rightRange = len(houses) - heaters[i]
            rge[0] = max(rge[0], leftRange)
            rge[1] = rightRange
            print(rge)
        return max(rge)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
