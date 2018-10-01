#! /usr/local/bin/python3

# https://www.lintcode.com/problem/log-sorting/description?_from=ladder&&fromId=62
# Example
# 给出一个由List < String > 组成的日志，每个元素代表一行日志。 每行日志信息以第一个空格分隔成两个字符串，分割后的前面部分的字符串为日志的ID，后面部分的字符串为日志内容(日志的内容也可能包括空格字符)。
# 组成日志内容的字符串有以下两种类别：
#
# 1.全部由字母和空格组成。
# 2.全部由数字和空格组成。
#
# 现在对日志进行了排序，要求类别1日志按照内容的字典编排的顺序排序并放在顶部，类别2的日志应放在底部并按输入顺序输出。（注意，除第一以外的空格字符也属于内容，并且当类别1的词典顺序相等时，根据日志ID的字典顺序排序，并且ID一定不重复）
#
# 样例
# 给出 list =
#
# [
#     "zo4 4 7",
#     "a100 Act zoo",
#     "a1 9 2 3 1",
#     "g9 act car"
# ]
# 返回
#
# [
#     "a100 Act zoo",
#     "g9 act car",
#     "zo4 4 7",
#     "a1 9 2 3 1"
# ]
# 解释：
# "Act zoo" < "act car"，所以输出如上。
# 给出 list =
#
# [
#     "zo4 4 7",
#     "a100 Act zoo",
#     "Tac Bctzoo",
#     "Tab Bct zoo",
#     "g9 act car"
# ]
# 返回
#
# [
#     "a100 Act zoo",
#     "Tab Bct zoo",
#     "Tac Bctzoo",
#     "g9 act car",
#     "zo4 4 7"
# ]
# 解释：
# 由于 "Bctzoo" == "Bctzoo", 所以比较"Tab"与"Tac"，有 "Tab" < "Tac"，故 "Tab Bctzoo" < "Tac Bctzoo"。
# 由于' ' < 'z' ,所以 "a100 Act zoo" < "a100 Actzoo"。
#
# 注意事项
# 输入的日志总数为n，n <= 10000。
# 每行日志长度为mi, mi <= 100。


"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        if not logs:
            return logs


        def cmpFunction(self, a, b):
            idxA = a.find(" ")
            titleA = a[:idxA]
            conA = a[idxA + 1:]
            idxB = b.find(" ")
            titleB = b[:idxB]
            conB = b[idxB + 1:]
            if conA != conB:
                if conA < conB:
                    return -1
                else:
                    return 1
            if titleA < titleB:
                return -1
            else:
                return 1
        newLog = sorted(logs, cmp=cmpFunction)
        return newLog

# Test Cases
if __name__ == "__main__":
    solution = Solution()
