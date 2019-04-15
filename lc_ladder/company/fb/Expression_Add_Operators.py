#! /usr/local/bin/python3

# https://www.lintcode.com/problem/expression-add-operators/description
# Example
# 给定一个仅包含数字 0 - 9 的字符串和一个目标值，返回在数字之间添加了 二元 运算符(不是一元)+, - 或 * 之后所有能得到目标值的情况。
#
# Example
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
"""
Algo: DFS, string
D.S.:

Solution:
https://www.youtube.com/watch?v=v05R1OIIg08

很多很多坑和技巧
- "123"， 处理前n个字符串构成的数字时 前面不需要有operator，所以直接覆盖cur_exp
- 处理* 很麻烦，需要知道前面一个节点的值，做乘积后记得更新当前值得value
- "0123" 要记得0x是invalid, 如果pre_num = 0 就不需要往后遍历更长数字的必要了

Time: O(n ^ 2 * 4 ^ (n - 1))
n ^ 2: ways of dividing numbers,
4 ^ (n - 1) ways of choosing operators
Space: O(n ^ 2)
每层递归都传入下一层一个expression string copy
因为for loop 的总时间复杂度的O(n ^ 2)，所以要存储 O(n ^ 2)个string

Corner cases:
"""

class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, num, target):
        # write your code here
        def dfs(start_idx, cur_exp, cur_val, last_node, res):
            if start_idx == len(num):
                # visited till the end of num string
                if cur_val == target:
                    res.append(cur_exp)
                return
            for i in range(start_idx, len(num)):
                # starting from start_idx to build possible integers
                # eg, 1, 12, 123, note that 012, is not a valid one, but 0 is valid

                pre_num = int(num[start_idx: i + 1])
                if start_idx == 0:
                    # note: start of the string here's no operator to connect
                    dfs(i + 1, str(pre_num), pre_num, pre_num, res)
                else:
                    dfs(i + 1, cur_exp + "+" + str(pre_num), cur_val + pre_num, pre_num, res)
                    dfs(i + 1, cur_exp + "-" + str(pre_num), cur_val - pre_num, -pre_num, res)
                    dfs(i + 1, cur_exp + "*" + str(pre_num), cur_val - last_node + last_node * pre_num, last_node * pre_num, res)
                # note: if pre_num = 0, then don't check later '01' '0X' is invalid
                if pre_num == 0:
                    break

        res = []
        start_idx = 0
        cur_exp = ""
        cur_val = 0
        last_node = 0
        dfs(start_idx, cur_exp, cur_val, last_node, res)
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
