#!/usr/local/bin/python3

# https://www.lintcode.com/problem/mini-yelp/description?_from=ladder&&fromId=8
# Example
# 设计一个小的Yelp系统支持下列操作
# 1.添加一个新餐馆的名字和地址
# 2.去除一个餐馆
# 3.在给定地点找一个临近的餐馆
#
# 临近餐馆是指距离小于 k km
#
# Restaurant类已近建立好了并且有Restaurant.create() 和Helper.get_distance(location1, location2)两个函数可以使用.
#
# GeoHash类也已经提供了GeoHash.encode(location)和GeoHash.decode(string)可以帮助转换地址
#
# 样例
# addRestauraunt("Lint Cafe", 10.4999999, 11.599999) // return 1
# addRestauraunt("Code Cafe", 10.4999999, 11.512109) // return 2
# neighbors(10.5, 11.6, 6.7) // return ["Lint Cafe"]
# removeRestauraunt(1)
# neighbors(10.5, 9.6, 6.7) // return []
#
#
# //  location(10.5, 11.6) 和 "Lint Code" 的距离是 0.0001099 km
# //  location(10.5, 11.6) 和 "Code Code" 的距离是 9.6120978 km
# 注意事项
# Learn about GeoHash http://www.lintcode.com/en/help/geohash/

"""
Solution:
TODO:

Corner cases:
"""

'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper
import bisect

class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {}
        self.ids = {}
        self.geo_value  = []

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        # Write your code here
        restaurant = Restaurant.create(name, location)
        hashcode = "%s.%s" % (GeoHash.encode(location), restaurant.id)
        bisect.insort(self.geo_value, hashcode)
        self.restaurants[hashcode] = restaurant
        self.ids[restaurant.id] = hashcode
        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        hashcode = self.ids[restaurant_id]
        index = bisect.bisect_left(self.geo_value, hashcode)
        self.geo_value.pop(index)
        del self.restaurants[hashcode]
        del self.ids[restaurant_id]

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        length = self.get_length(k)
        hashcode = GeoHash.encode(location)[0:length]
        left = bisect.bisect_left(self.geo_value, hashcode)
        right = bisect.bisect_right(self.geo_value, hashcode + '{')

        results = []
        # print left, right, hashcode
        for index in range(left, right):
            hashcode = self.geo_value[index]
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if  distance <= k:
                results.append((distance, restaurant))

        results = sorted(results, key=lambda obj: obj[0])
        return [rt[1].name for rt in results]

    def get_length(self, k):
        ERROR = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]
        for i, error in enumerate(ERROR):
            if k  > error:
                return i

        return len(ERROR)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
