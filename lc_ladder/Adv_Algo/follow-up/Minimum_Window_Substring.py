#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-window-substring/
# Example
# 给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。
#
# 样例
# 给出source = "ADOBECODEBANC"，target = "ABC" 满足要求的解  "BANC"
#
# 挑战
# 要求时间复杂度为O(n)
#
# 说明
# Should the characters in minimum window has the same order in target?
#
# Not necessary.
# 注意事项
# If there is no such window in source that covers all characters in target, return the emtpy string "".
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.
# The target string may contain *duplicate* characters, the minimum window should cover all characters including the duplicate characters in target.

"""
Algo: 双指针，快慢指针，只往前走，不回头
D.S.:

Solution:
O(N)
j starting from 0 -> n - 1
i starting from 0 -> n - 1
j 先往前移动，直至找到一个match，i再往前移动，缩小范围，直至不match，重复j往前移动过程
总共：O(2n)

Corner cases:
"""
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        if not source or not target:
            return ""
        srcmap = [0] * 256
        tgtmap = [0] * 256
        self.initTgtmap(tgtmap, target)
        minStr = ""
        minLen = len(source) + 1
        i, j = 0, 0 #slower pointer, and faster pointer
        for i in range(len(source)):
            while not self.isValid(srcmap, tgtmap) and j < len(source):
                srcmap[ord(source[j])] += 1
                j += 1
            # No matter if while breaks due to valid or j outof range,
            # j already in the next position
            if self.isValid(srcmap, tgtmap):
                if minLen > j - i:
                    minLen = j - i
                    minStr = source[i : j]
            srcmap[ord(source[i])] -= 1
        return minStr

    def initTgtmap(self, tgtmap, target):
        for i in target:
            tgtmap[ord(i)] += 1
        return tgtmap

    def isValid(self, srcmap, tgtmap):
        for i in range(256):
            if tgtmap[i] > srcmap[i]:
                return False
        return True


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        import sys
        lt, ls = len(t), len(s)
        slot_t = [0] * 256
        slot_s = [0] * 256
        self.init(slot_t, len(t), t)
        # print(slot_t)
        fast, slow = 0, 0
        slot_s[ord(s[fast])] = 1
        res = [None, None]
        length = sys.maxsize
        while fast < len(s):
            while self.canCover(slot_t, slot_s):
                print('s: %s, f: %s' %(slow, fast))
                if fast - slow < length:
                    length = fast - slow
                    res = [slow, fast]
                slot_s[ord(s[slow])] -= 1
                slow += 1
            if fast < len(s) - 1:
                slot_s[ord(s[fast + 1])] += 1
            fast += 1
        print('res: %s' %repr(res))
        # NOTE: 一定要查最后可能根本找不到的情况
        if res == [None, None]:
            return ""
        else:
            return s[res[0]: res[1] + 1]

    def init(self, slot, length, string):
        for i in range(length):
            slot[ord(string[i])] += 1

    def canCover(self, slot_t, slot_s):
        for i in range(256):
            if slot_t[i] > slot_s[i]:
                return False
        return True
# Test Cases
if __name__ == "__main__":
    s2 = Solution2()
    testcases = [
        {
            's': 'a',
            't': 'b'
        },
        {
            's': 'abc',
            't': 'b'
        },
        {
            's': 'ADOBECODEBANC',
            't': 'ABC'
        }
    ]

    for test in testcases:
        s = test['s']
        t = test['t']
        res2 = s2.minWindow(s, t)
        print(res2)
