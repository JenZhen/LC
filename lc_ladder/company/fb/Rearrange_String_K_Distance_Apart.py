#! /usr/local/bin/python3

# https://leetcode.com/problems/rearrange-string-k-distance-apart/submissions/
# Example
# Given a non-empty string s and an integer k,
# rearrange the string such that the same characters are at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
#
# Example 1:
#
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least distance 3 from each other.
# Example 2:
#
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.
# Example 3:
#
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
"""
Algo: sort, heap
D.S.:

Solution:
- 每个字符求频率 放入map
- 根据1）频率2）字符字典序，放入max heap
- 从heap 里 每次拿出来k 个最大频率的 （因为k个数是一组）
拼成结果的字符串， 同时频率table 减少，
同时 记录当前 组里 如果还有剩余频率 最后要重新入heap

重要的判断不能拼成的条件
如果在读heap 时候 heap 空了
 - 有2个合理情况，1）这一组 k 个数 读完了 也就是 i == k - 1
                2）s 所有的数都读完了，也就是 S 的长度不是K 的倍数 即 len(s）== len(res)
 - 除以上2种情况以外 就是不合理的，直接返回”“
- 同时要注意！当heap 空的时候 一定要退出 取K 个数的for loop 因为不能再继续pop 空heap 一定要Break

Time: O(n)
Space: O(n)

Similar:
767 reorganize string
https://leetcode.com/problems/reorganize-string/
621 task scheduler
https://leetcode.com/problems/task-scheduler/solution/

Corner cases:
s = 'abb', k = 2
s = 'abb', k = 4
s = '', k = 3
s = 'abcd', k = 0
"""

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        from heapq import heappush, heappop

        if not s or not k: return s

        cnt_map = {} # key: char, val: freq
        for char in s:
            if char not in cnt_map:
                cnt_map[char] = 0
            cnt_map[char] += 1

        heap = []
        for char, freq in cnt_map.items():
            heappush(heap, (-freq, char))

        res = ""
        while heap:
            tmp_list = []
            for i in range(k):
                _, char = heappop(heap)
                res += char
                cnt_map[char] -= 1
                if cnt_map[char] > 0:
                    tmp_list.append(char)

                if len(heap) == 0:
                    # s = 'abb', k = 4
                    if i != k - 1 and len(res) != len(s):
                        return ""
                    break # break for loop
            # put char in tmp-list back to heap
            for char in tmp_list:
                heappush(heap, (-cnt_map[char], char))
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
