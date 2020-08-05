#! /usr/local/bin/python3

# Requirement
# 给定一个函数bool predicate(int), 一个vector, 一个int k. 把满足predicate的element聚集到index k的前后。
# 满足predicate的element需要保持原有次序，不满足的element也需要。不可以使用extra space。
#
# e.g {1, -1, 2, -2, 3, -3, 4, -4}   k = 4, predicate is the integer > 0.
#
# 需要把 k之前的elements 从{1, -1, 2, -2}变成 {-1, -2, 1, 2}      // 大于0的往后移，但是1, 2仍保有原有顺序，-1, -2也是
# k之后的elements从{3, -3, 4, -4}变成{3, 4, -3, -4}      // 大于0的往前移，但是3, 4仍保有原有顺序，-3, -4也是
#
# vector变成了{-1, -2, 1, 2, 3, 4, -3, -4}
# 相当于把满足predicate的element聚集在index k的前后。
# Example

"""
Algo:
D.S.:

Solution:
Time: ()
Space: ()


Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
