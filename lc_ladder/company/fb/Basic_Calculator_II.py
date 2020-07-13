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

Solution1:
Inspired by Expression Add Operators
Time: O(N)
Space: O(1)
注意注意注意：做除法时
’12 - 3 /2' => 11
in python
-3 /2 = -2
3/ 2 = 1
在这里如果prev_val < 0 要转成正数 除后加上符号 得到 tmp_val

Solution2:
计算 模板
Time: O(N)
Space: O(N)
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

class Solution2_Standard:
    def calculate(self, s: str) -> int:
        parsed_list = self.parse(s)
        st_num = []
        st_op = []
        print(parsed_list)
        priority = {
            '+': 1,
            '-': 1,
            '/': 2,
            '*': 2,
        }
        for ele in parsed_list:
            if ele.isdigit():
                st_num.append(int(ele))
            else:
                #注意这里 优先级是>=  - + 要先算 - 再算 +
                while st_op and priority[st_op[-1]] >= priority[ele]:
                    op = st_op.pop()
                    if len(st_num) < 2:
                        raise "Invalid input"
                    n2 = st_num.pop()
                    n1 = st_num.pop()
                    st_num.append(self.calc(n1, n2, op))
                st_op.append(ele)

        while st_op:
            op = st_op.pop()
            if len(st_num) < 2:
                raise "Invalid input"
            n2 = st_num.pop()
            n1 = st_num.pop()
            st_num.append(self.calc(n1, n2, op))
        return st_num[-1]

    def calc(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            sign = 1 if (n1 >= 0 and n2 > 0) or (n1 <= 0 and n2 < 0) else -1
            return n1 // n2 * (sign)

    def parse(self, s):
        n = len(s)
        i = 0
        res = []
        while i < n:
            c = s[i]
            if c.isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                res.append(s[i:j])
                i = j
            elif c == '+' or c == '-' or c == '*' or c == '/':
                res.append(c)
                i += 1
            elif c == ' ':
                i += 1
                continue
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
