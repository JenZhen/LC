#! /usr/local/bin/python3

# https://leetcode.com/problems/validate-stack-sequences/submissions/
# Example
# Given two sequences pushed and popped with distinct values,
# return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack
#
# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
# Note:
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
"""
Algo: stack
D.S.:

Solution1:
Time: O(n)
Space: O(n)

Solution2:
Time: O(n ^ 2)
Space: O(1)
以时间换空间
重要常考的follow up
pushed: 1, 2, 3, 4, 5
popped: 4, 5, 3, 2, 1
用stack的好处：[1,2,3,4] - 4 pop 之后，是5，5pop之后 直接暴露3 快速知道4已经pop了
如果不用stack，需要遍历 之前poped 的数 来看 4是否已经pop 过


Corner cases:
"""

class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        st = []
        for ele in pushed:
            st.append(ele)
            while st and j < len(popped) and st[-1] == popped[j]:
                st.pop()
                j += 1
        return j == len(popped)

class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        for i in range(len(pushed)):
            push_idx = i
            while push_idx >= 0 and pop_idx < len(popped) and pushed[push_idx] == popped[pop_idx]:
                push_idx -= 1
                pop_idx += 1

                # hasPopped 看前一个push 进去的元素是否已经pop 过
                while push_idx >= 0 and self.hasPopped(pushed[push_idx], popped, pop_idx - 1):
                    # 如果pop 过，push_idx 往前挪一位，然后继续看这一位有没有 pop
                    push_idx -= 1
        return pop_idx == len(popped)

    def hasPopped(self, pushed_value, popped, pop_idx):
        # 固定一个pushed_value，popped 数组往前找，
        while pop_idx >= 0:
            if pushed_value == popped[pop_idx]:
                return True
            pop_idx -= 1
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
