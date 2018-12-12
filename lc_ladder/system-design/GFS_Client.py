#!/usr/local/bin/python3

# https://www.lintcode.com/problem/gfs-client/description?_from=ladder&&fromId=8
# Example

# 为GFS(Google文件系统)实现一个简单的客户端，提供一下功能：
# 1.read(文件名)，通过文件名从GFS中读取文件。
# 2.write(文件名，内容)，通过文件名和内容写入GFS中。
# 现在有两种已经在基础类中实现的方法：
# 1.readChunk(文件名，块索引)，从GFS中读取一个块。
# 2.writeChunk(文件名，块索引，块数据)，向GFS中写入一个块。
# 为了简化这个问题，我们可以假设块大小为 chunkSize 位的(在真实的文件系统中，是64M)，GFS客户端的任务是将一个文件分为若干块(如果需要的话)并且保存在远端的GFS服务器上，chunkSize会在构造函数中给出，你需要的是实现读和写这两个private方法。
#
# 样例
# GFSClient(5)
# read("a.txt")
# >> null
# write("a.txt", "World")
# >> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
# read("a.txt")
# >> "World"
# write("b.txt", "111112222233")
# >> You need to save "11111" at chink 0, "22222" at chunk 1, "33" at chunk 2.
# write("b.txt", "aaaaabbbbb") # 注意，根据题意，这里的第二次写操作是覆盖，具体实现在父类中隐去
# read("b.txt")
# >> "aaaaabbbbb"

"""
Solution:

Corner cases:
注意 继承是父类方法的调用

"""
'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        self.chunkSize = chunkSize
        self.chunkNum = {} # filename: how many chunks have been written

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.chunkNum:
            return
        res = ""
        for i in range(self.chunkNum[filename]):
            subcontent = BaseGFSClient.readChunk(self, filename, i)
            if subcontent:
                res += subcontent
        return res

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        chunkNum = len(content) // self.chunkSize
        if (len(content) % self.chunkSize) != 0:
            chunkNum += 1
        for i in range(chunkNum):
            subcontent = content[i * self.chunkSize : (i + 1) * self.chunkSize]
            print(subcontent)
            BaseGFSClient.writeChunk(self, filename, i, subcontent)
        self.chunkNum[filename] = chunkNum

# Test Cases
if __name__ == "__main__":
    solution = Solution()
