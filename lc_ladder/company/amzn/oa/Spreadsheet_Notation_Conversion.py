#! /usr/local/bin/python3

# https://www.lintcode.com/problem/spreadsheet-notation-conversion/description?_from=ladder&&fromId=156
# Example
# 你需要模拟电子表格，类似 ExcelExcel 的列命名规则，将整数的编号转换成字符串的形式。
# 给出一个数 indexindex，令 1 = A1=A, 2 = B2=B，26 = Z26=Z，27 = AA27=AA ... 最后 702 = ZZ702=ZZ，每行最多有 702702 个编号。
# 当 index > 702index>702 时，需要换一行，并重新开始编号，并重新从 AA 开始编号，如 703 = A703=A，705 = C705=C。每满 702702 个数都要换行，重新开始编号。
# 最后转换的结果为 indexindex 所在的行号加上他的编号。
# 如最终 1 = 1A, 2 = 1B, 3 = 1C, 26 = 1Z, 27 = 1AA, 702 = 1ZZ, 705 = 2C, 1404 = 2ZZ1=1A,2=1B,3=1C,26=1Z,27=1AA,702=1ZZ,705=2C,1404=2ZZ。
# 如 705705 在第 22 行，编号为 CC，所以它通过转换得到的字符串是 2C2C。
#
# 样例
# 样例输入1:
# 3
#
# 样例输出1:
# 1C
# 样例输入2:
# 28
#
# 样例输出2:
# 1AB
# 注意事项
# 1 <= index <= 10^{18}1<=index<=10
# ​18

"""
Algo:
D.S.:

Solution:
类似 excel-sheet-column-title

Corner cases:
"""

class Solution:
    """
    @param index: the index to be converted
    @return: return the string after convert.
    """
    def convert(self, index):
        # write your code here
        if not index: return ''
        index = index - 1
        res = ''
        row = (index // 702) + 1
        res += str(row)
        rest = index - (index // 702) * 702
        first_idx = rest // 26
        if first_idx:
            res += chr(ord('A') + first_idx - 1)
            rest -= first_idx * 26

        last = rest % 26
        res += chr(ord('A') + last)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
