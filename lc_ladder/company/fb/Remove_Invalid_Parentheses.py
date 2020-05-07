#! /usr/local/bin/python3

# https://www.lintcode.com/problem/remove-invalid-parentheses/description
# Example
# https://www.youtube.com/watch?v=2k_rS_u6EBk÷
# 删除最小数目的无效括号，使得输入字符串有效，返回所有可能的结果。
#
# Example
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
# Notice
# 输入字符串可能包含除括号( 和 )之外的字符。

"""
Algo: DFS (Backtracking)
D.S.: string

Solution:
1. 如何判断是否是valid：( 可以随便有， ) 不能多于左侧的 ( ,最后必须相等
2. 找到最少要remove多少个左、右括号，
3. dfs 去找如何remove 所有多余的左右括号，当remove完，要再次检查是否valid
注意：
1. 重复的情况，dfs 如何去重
2. 结尾一定要再次查是否valid再能放入res List
3. dfs 要带着每层的startIdx

Time：O(2 ^(l + r)) recursion depth l + r ~ n
Space: O((l + r) ^ 2) ~ O(n^2)

Corner cases:
"""

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        if not s:
            return [s]
        if self._is_valid(s):
            return [s]
        # cnt of '(' and cnt of ')' to remove to make it valid
        l, r = 0, 0
        for char in s:
            if c == '(':
                l += 1
            if c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
            # option2
            # if c == '(':
            #     l += 1
            # if l == 0:
            #     r += c == ')'
            # else:
            #     l -= c == ')'
            # option3
            # l += (char == "(")
            # if l == 0:
            #     # find extra )
            #     r += (char == ")")
            # else:
            #     # offset extra (
            #     l -= (char == ")")

        res = []
        self.dfs(s, 0, l, r, res)
        return res

    def dfs(self, string, startIdx, l, r, res):
        if l == 0 and r == 0 and self._is_valid(string):
            res.append(string)
            return

        for i in range(startIdx, len(string)):
            if i != startIdx and string[i] == string[i - 1]:
                continue
            if string[i] == ")" and r > 0:
                nextString = string[:i] + string[i + 1:]
                self.dfs(nextString, i, l, r - 1, res)
            if string[i] == "(" and l > 0:
                nextString  = string[:i] + string[i + 1:]
                self.dfs(nextString, i, l - 1, r, res)



    def _is_valid(self, s):
        # l: cnt of left parentheses
        # r: cnt of right parentheses
        # traverse from left to right
        # if at any point r > l return False
        # at the end of s, valid only l == r
        l, r = 0, 0
        for char in s:
            if char == "(":
                l += 1
            if char== ")":
                r += 1
                if r > l:
                    return False
        return l == r


class Solution2:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        if not s:
            return [s]
        if self._is_valid(s):
            return [s]
        # cnt of '(' and cnt of ')' to remove to make it valid
        l, r = 0, 0
        for char in s:
            l += (char == "(")
            if l == 0:
                # find extra )
                r += (char == ")")
            else:
                # offset extra (
                l -= (char == ")")

        res = self.dfs(s, 0, l, r)
        return res
    # // return only 1 result
    # public String removeInvalid(String input) {
    #     Stack<Integer> stack = new Stack<Integer>();
    #
    #     for (int i = 0; i < input.length(); i++) {
    #         char c = input.charAt(i);
    #         if (c == '(') {
    #             stack.push(i);
    #         } else if (c == ')') {
    #             if (stack.isEmpty() || input.charAt(stack.peek()) != '(') {
    #                 stack.push(i);
    #             } else {
    #                 stack.pop();
    #             }
    #         }
    #     }
    #
    #     StringBuilder sb = new StringBuilder(input);
    #     while (!stack.isEmpty()) {
    #         sb.deleteCharAt(stack.pop());
    #     }
    #
    #     return sb.toString();
    # }

# Test Cases
if __name__ == "__main__":
    solution = Solution()
