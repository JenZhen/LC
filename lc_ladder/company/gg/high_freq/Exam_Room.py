#! /usr/local/bin/python3

# https://leetcode.com/problems/exam-room/
# Example
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
#
# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.
#
#
#
# Example 1:
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# ​​​​​​​
#
# Note:
#
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""
Algo:
D.S.:

Solution:
seat: O(log n)
leave: O(n)

1.用优先队列：
用优先队列存slot，slot包含左右端点和长度。exclusive好算。注意如果是最左或最右时长度为right - left，若非则为(right - left) / 2，因为如果选择坐边上可以不管端点。seat时候去pq最大slot，中间切开offer两段。leave时候遍历找到左右两段整合
坐下时间复杂度 O(logn)
离开时间复杂度 O(n)

heap operation O(logn)
heapify O(n)
Corner cases:
"""


from heapq import heapify, heappush, heappop
class ExamRoom:

    def __init__(self, N: int):
        self.hp = []
        self.N = N
        heappush(self.hp, (self._get_dist(-1, N), -1, N))

    def _get_dist(self, l, r):
        if l == -1:
            return -r
        if r == self.N:
            return -(self.N - 1 - l)
        return -(abs(l - r) // 2)

    def seat(self) -> int:
        max_range = heappop(self.hp)
        left, right = max_range[1], max_range[2]
        new_seat = None
        if left == -1:
            new_seat = 0
        elif right == self.N:
            new_seat = self.N - 1
        else:
            new_seat = (left + right) // 2
        heappush(self.hp, (self._get_dist(left, new_seat), left, new_seat))
        heappush(self.hp, (self._get_dist(new_seat, right), new_seat, right))
        return new_seat

    def leave(self, p: int) -> None:
        head = tail = None
        for i in range(len(self.hp)):
            if p == self.hp[i][1]:
                tail = self.hp[i]
            if p == self.hp[i][2]:
                head = self.hp[i]
            if head and tail:
                break
        new_left = head[1]
        new_right = tail[2]
        self.hp.remove(head)
        self.hp.remove(tail)
        heapify(self.hp)
        heappush(self.hp, (self._get_dist(new_left, new_right), new_left, new_right))
        return None

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
