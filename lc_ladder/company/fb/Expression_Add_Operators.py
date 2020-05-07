#! /usr/local/bin/python3

# https://leetcode.com/problems/expression-add-operators/submissions/
# Example
# Given a string that contains only digits 0-9 and a target value,
# return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
# Example 1:
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# Example 3:
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# Example 5:
# Input: num = "3456237490", target = 9191
# Output: []
"""
Algo: DFS, Backtracking
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []
        res = []
        tmp = ''
        cur_sum = 0
        prev_sum = 0
        start_idx = 0
        self.dfs(target, num, res, tmp, start_idx, cur_sum, prev_sum)
        return res

    def dfs(self, target, num, res, tmp, start_idx, cur_sum, prev_sum):
        if start_idx == len(num) and cur_sum == target:
            res.append(tmp)
            return
        for i in range(start_idx, len(num)):
            s = num[start_idx:(i+1)]
            s_value = int(s)

            if start_idx == 0:
                self.dfs(target, num, res, s, i + 1, s_value, s_value)
            else:
                self.dfs(target, num, res, tmp + '+' + s, i + 1, cur_sum + s_value, s_value)
                self.dfs(target, num, res, tmp + '-' + s, i + 1, cur_sum - s_value, s_value * (-1))
                self.dfs(target, num, res, tmp + '*' + s, i + 1, cur_sum - prev_sum + prev_sum * s_value, prev_sum * s_value)
            if s_value == 0:
                break # if '0' not '01'
# Test Cases
if __name__ == "__main__":
    solution = Solution()
