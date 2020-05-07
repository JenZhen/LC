#! /usr/local/bin/python3

# https://leetcode.com/problems/basic-calculator-ii/submissions/
# Example
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
# Input: "3+2*2"
# Output: 7
# Example 2:
# Input: " 3/2 "
# Output: 1
# Example 3:
# Input: " 3+5 / 2 "
# Output: 5
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
"""
Algo:
D.S.:

Solution:
Inspired by Expression Add Operators
Time: O(N)
Space: O(1)
注意注意注意：做除法时
’12 - 3 /2' => 11
in python
-3 /2 = -2
3/ 2 = 1
在这里如果prev_val < 0 要转成正数 除后加上符号 得到 tmp_val
Corner cases:
"""


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        prev_val = 0
        prev_op = '+'
        val = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                cur_val = int(s[i:j])
                # print('prev_val: ', prev_val)
                # 注意要将 i 挪到 j
                i = j
                if prev_op == '+':
                    prev_val = cur_val
                    val = val + cur_val
                elif prev_op == '-':
                    prev_val = -cur_val
                    val = val - cur_val
                elif prev_op == '*':
                    tmp_val = prev_val * cur_val
                    val = val - prev_val + tmp_val
                    prev_val = tmp_val
                elif prev_op == '/':
                    sign = 1 if prev_val > 0 else -1
                    tmp_val = abs(prev_val) // cur_val * (sign)
                    val = val - prev_val + tmp_val
                    prev_val = tmp_val
            elif s[i] in ['+', '-', '*', '/']:
                prev_op = s[i]
                i += 1
        return val
# Test Cases
if __name__ == "__main__":
    solution = Solution()
