#!/usr/local/bin/python3

# https://www.lintcode.com/problem/geohash-ii/description?_from=ladder&&fromId=8
# Example

"""
Solution:

Corner cases:
"""

class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # write your code here
        # convert 32based to 10based
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        for c in geohash:
            # convert decimal to 5-digit binary
            b += self.i2b(_base32.find(c))
        print("b: " + b)
        odd = ''.join([b[i] for i in range(0, len(b), 2)]) # for latitude
        even = ''.join([b[i] for i in range(1, len(b), 2)]) # for longitude
        print("odd: " + odd)
        print("even: " + even)
        location = []
        location.append(self.get_location(-90.0, 90.0, even))
        location.append(self.get_location(-180.0, 180.0, odd))
        return location

    def i2b(self, val):
        # template from decimal to binary
        # for loop controls total digit
        b = ""
        for i in range(5):
            if val % 2:
                b = '1' + b
            else:
                b = '0' + b
            val = val // 2
        return b

    def get_location(self, start, end, string):
        for c in string:
            mid = (start + end) / 2
            print(mid)
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2

# Test Cases
if __name__ == "__main__":
    solution = GeoHash()
    print solution.decode("wx4g0s")
