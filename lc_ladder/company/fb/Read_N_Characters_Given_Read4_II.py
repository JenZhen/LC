#! /usr/local/bin/python3

# https://www.lintcode.com/problem/read-n-characters-given-read4-ii-call-multiple-times/description
# Example
# 接口：int read4(char * buf)一次从文件中读取 4 个字符。
# 返回值是实际读取的字符数。 例如，如果文件中只剩下 3 个字符，则返回 3。
# 通过使用read4 接口，实现从文件读取 n 个字符的函数int read(char * buf，int n)。
#
# 样例
# Example 1
#
# Input:
# "filetestbuffer"
# read(6)
# read(5)
# read(4)
# read(3)
# read(2)
# read(1)
# read(10)
# Output:
# 6, buf = "filete"
# 5, buf = "stbuf"
# 3, buf = "fer"
# 0, buf = ""
# 0, buf = ""
# 0, buf = ""
# 0, buf = ""
# Example 2
#
# Input:
# "abcdef"
# read(1)
# read(5)
# Output:
# 1, buf = "a"
# 5, buf = "bcdef"
# 注意事项
# read 函数可能被调用多次。

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:
    # 注意global 变量的定义
    buf_ptr = 0 # 当前读到临时Buffer哪个位置
    buf_cnt = 0 # 临时buffer读出来有几位 0 - 4
    tmp_buf = [None] * 4 # 临时buffer 有4位，一定要预留好，否则会idx error
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        ttl = 0 # 当前read读了几个
        while ttl < n: # 一定是小于n
            # 如果当前buffer 读数的位置是0，说明都读完了，应该call read4 再来一波4个char
            if self.buf_ptr == 0:
                # 更新这次call api 读了几个出来
                self.buf_cnt = Reader.read4(self.tmp_buf)

            # 在总数小于n
            # buffer 指针小于当前读出来的buf_cnt (无论是刚读出来的4个还是上一轮剩下来的)
            while ttl < n and self.buf_ptr < self.buf_cnt:
                buf[ttl] = self.tmp_buf[self.buf_ptr]
                ttl += 1
                self.buf_ptr += 1

            # self.buf_ptr == self.buf_cnt 说明当前Buffer里读出来的都用完了
            # 可能还有更多的需要读，需要reset buf_ptr = 0下一轮循环读出来一个新的read4
            if self.buf_ptr == self.buf_cnt:
                self.buf_ptr = 0
            # 如果当前buffer读出来的不够4，说明read4已经没有了，直接Break, 即使没有读完n个字符
            if self.buf_cnt < 4:
                break # no more read4
        return ttl


# Test Cases
if __name__ == "__main__":
    solution = Solution()
