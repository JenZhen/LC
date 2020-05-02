#! /usr/local/bin/python3

# https://www.lintcode.com/problem/simplify-path/description
# Example
# 给定一个文件的绝对路径(Unix-style)，请进行路径简化。
#
# Unix中, . 表示当前目录, .. 表示父目录。
#
# 结果必须以 / 开头，并且两个目录名之间有且只有一个 /。最后一个目录名(如果存在)后不能出现 / 。你需要保证结果是正确表示路径的最短的字符串。
#
# 样例
# 样例 1:
#
# 输入: "/home/"
# 输出: "/home"
# 样例 2:
#
# 输入: "/a/./../../c/"
# 输出: "/c"
# 解释: "/" 没有上级目录, "/../" 的结果就是 "/".
# 注意事项
# 你是否考虑了 路径为 "/../" 的情况？
#
# 在这种情况下，你需返回"/"。
#
# 此外，路径中也可能包含双斜杠'/'，如 "/home//foo/"。
#
# 在这种情况下，应该忽略多余的斜杠，返回 "/home/foo"。

"""
Algo: string manipulation
D.S.:

Solution:
Time: O(n)

Corner cases:
要和面试官讨论各种可能的corner cases
input:
'/...'
'///'
'/home'
'home/'
"""

class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        if not path: return path
        st = []
        parts = path.split('/')
        print(parts)
        for p in parts:
            if p == '..':
                if st: st.pop()
            elif p == '.' or not p:
                continue
            else:
                st.append(p)
        return '/' + '/'.join(st)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
