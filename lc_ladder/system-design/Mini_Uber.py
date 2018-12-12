#!/usr/local/bin/python3

# https://www.lintcode.com/problem/mini-uber/description?_from=ladder&&fromId=8
# Example
# 实现一个迷你优步
# 1.司机提供他们的位置
# 2.用户请求，然后返回一个匹配的司机
#
# 实现下列函数
#
# report(driver_id, lat, lng)
#
# 如果没有找到匹配的，返回null
# 否则返回匹配trip信息
# request(rider_id, lat, lng)
#
# 简历一个trip
# 找到一个最近的司机，标记这个司机不可用了
# 将司机id填到trip里
# 返回trip
# trip的定义
#
# public class Trip {
#     public int id; // trip's id, primary key
#     public int driver_id, rider_id; // foreign key
#     public double lat, lng; // pick up location
# }
# 样例
# report(1, 36.1344, 77.5672) // return null
# report(2, 45.1344, 76.5672) // return null
# request(2, 39.1344, 76.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
# report(1, 38.1344, 75.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
# report(2, 45.1344, 76.5672) // return null

"""
Solution:
- report: 显然是根据driverid 查location
- request: 如果没有report的条件"return {trip} matched trip information if there have matched rider " 会有很多解法
根据题意直接的办法就是建立driver - trip的表， driver2Location 只用作给available 的driver，遍历来找到最近的driver
如果没有就返回None，否则完成trip信息并返回

Corner cases:
"""

'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper

class Location:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        # drivers available to pickup and his location
        # When driver match up with a rider, remove from this map
        self.driver2Location = {}
        # drivers in trip to the current trip
        self.driver2Trip = {}


    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # if driver not in trip, update his location
        # if driver in trip do not
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]
        if driver_id not in self.driver2Location:
            self.driver2Location[driver_id] = Location(lat, lng)
        else:
            self.driver2Location[driver_id].lat = lat
            self.driver2Location[driver_id].lng = lng
        return None

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # create a trip first
        # find the closest available driver from self.driver2Location
        # if no driver return none, if yes, fill in trip driver_id,
        # remove from driver2Location, add to driver2Trip
        trip = Trip(rider_id, lat, lng)
        driver_id, distance = -1, -1
        for id, loc in self.driver2Location.items():
            dis = Helper.get_distance(lat, lng, loc.lat, loc.lng)
            if distance == -1 or dis < distance:
                distance = dis
                driver_id = id
        if driver_id == -1:
            print("No available drivers")
            return None
        trip.driver_id = driver_id
        self.driver2Trip[driver_id] = trip
        del self.driver2Location[driver_id]
        return trip

# Test Cases
if __name__ == "__main__":
    solution = Solution()
