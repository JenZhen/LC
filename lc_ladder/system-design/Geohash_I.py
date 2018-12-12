#!/usr/local/bin/python3

# https://www.lintcode.com/problem/geohash/description?_from=ladder&&fromId=8
# Example
# Geo哈希是一个著名的哈希算法，用于将坐标哈希成一个32位字符串
# Geohash： https://en.wikipedia.org/wiki/Geohash
# http://geohash.co/
#
# 样例
# 给出 lat = 39.92816697, lng = 116.38954991 precision = 12 返回 wx4g0s8q3jf9.
#
# precision 范围为 1 ~ 12.

"""
Solution:

因为precision是upto 12
如果12位，每一位对应一个32based的数，每一位转化为2进制需要5位，所以一共最多12 * 5 = 60 位2进制
经纬混合就是各30digit，所以经纬查找每个bin需要30个Loop

Corner cases:
"""

class GeoHash:
    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        # write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat_bin = self.get_bin(latitude, -90, 90)
        lng_bin = self.get_bin(longitude, -180, 180)
        print("lat_bin: %s" % lat_bin)
        print("lng_bin: %s" % lng_bin)
        hash_code, b = '', ''
        for i in range(30):
            b += lng_bin[i] + lat_bin[i]
        print("b: " + b)
        for i in range(0, 60, 5):
            # every 5 digit is a group: 2 ^ 5 = 32 (binary 32 based)
            # subStr is binary 5 digit string number
            subStr = b[i : i + 5]
            print("subStr: " + subStr)
            # convert a binary into a decimal integer,
            # which is the index of the _base32 map
            biNum = int(subStr, 2)
            print("biNum: " + str(biNum))
            hash_code += _base32[biNum]
            print("hash_code: " + str(hash_code))

        # take only first precision digit of the final hashcode
        return hash_code[:precision]


    def get_bin(self, value, left, right):
        b = ''
        # why 30 iteration
        for i in range(30):
            mid = (left + right) / 2
            if value > mid:
                left = mid
                b += '1'
            else:
                right = mid
                b += '0'
        return b


# Test Cases
if __name__ == "__main__":
    solution = Solution()
