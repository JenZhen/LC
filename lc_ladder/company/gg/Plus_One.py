#! /usr/local/bin/python3

# https://lintcode.com/problem/plus-one/description
# Example

"""
Algo:
D.S.:

Solution:
Time: O(n), Space: O(1)

Corner cases:
加1进位，只能是9
最后要做加一位也只能是 99999, 999类型，可以保证后面全是0
"""

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        if not digits:
            return [1]
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9: #it's adding one, could be simpler just compare with 9
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1 # make the first digit 1, append extra 0 at the end
        digits.append(0)
        return digits

# Test Cases
if __name__ == "__main__":
    solution = Solution()
