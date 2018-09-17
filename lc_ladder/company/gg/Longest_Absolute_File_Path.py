#! /usr/local/bin/python3

# https://lintcode.com/problem/longest-absolute-file-path/description?_from=ladder&&fromId=18
# Example
# 假设我们通过以下的方式用字符串来抽象我们的文件系统：
# 字符串"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"代表了：
#
# dir
# 	subdir1
# 	subdir2
# 		file.ext
# 目录 dir 包含一个空子目录 subdir1 和一个包含文件file.ext的子目录 subdir2。
# 字符串
#
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# 代表了：
#
# dir
# 	subdir1
# 		file1.ext
# 		subsubdir1
# 	subdir2
# 		subsubdir2
# 			file2.ext
# 目录 dir 包含两个子目录 subdir1 和 subdir2 。 subdir1 包含一个文件 file1.ext 和一个空的二级子目录 subsubdir1 。 subdir2 包含一个包含文件 file2.ext 的二级子目录 subsubdir2。
# 我们有兴趣找到文件系统中文件的最长绝对路径（字符数）。例如，在上面的第二个例子中，最长的绝对路径是“dir/subdir2/subsubdir2/file2.ext”，其长度为 32 (不包括双引号)。
# 给定一个以上述格式表示文件系统的字符串，返回抽象文件系统中文件最长绝对路径的长度。如果系统中没有文件，则返回 0 。
#
# 样例
# Give input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" return 20
#
# 注意事项
# 一个文件的名称至少包含一个 . 和扩展名。
# 目录或子目录的名称不会包含 . 。
# 时间复杂度要求： O(n) 其中 n 是输入字符串的大小。
# 请注意如果有另一条路径 aaaaaaaaaaaaaaaaaaaaa / sth.png 存在的话, a/aa/aaa/file1.txt 不是最长的文件路径。

"""
Algo:
D.S.:

Solution:
Time: O(n) -- 转化为list后，每个元素被读取一次
Space: O(n)

# dir
# 	subdir1
# 		file1.ext
# 		subsubdir1
# 	subdir2
# 		subsubdir2
# 			file2.ext

level1: r.find("\t") = -1, 没有找到    ，-1 + 2 = 1， 0个‘\t’
level2: r.find("\t") = 0,  找到位置在0  ， 0 + 2 = 2, 1个'\t'
...

stack = [0, 0, 0, 0, 0]
stack[i]表示累计到第i层的长度
stack[0] = 0 #第0层是0
stack[1] = len(f) （不用考虑分隔符）
stack[2] = stack[2 - 1] + 第2层长度，where 第二层长度 = len(f) - countOf("\t") + 1 (一个'\'分隔符在最前面)

只有在有'.'的文件时才考虑是否要update res

Corner cases:
"""

class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        # write your code here
        res = 0
        if not input:
            return res
        files = input.split("\n")
        stack = [0] * (len(files) + 1)
        for f in files:
            level = f.rfind("\t") + 2 # ith level i start from 1
            stack[level] = stack[level - 1] + len(f) - level + 1
            if level != 1:
                stack[level] += 1
            if f.find('.') != -1:
                res = max(res, stack[level])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
