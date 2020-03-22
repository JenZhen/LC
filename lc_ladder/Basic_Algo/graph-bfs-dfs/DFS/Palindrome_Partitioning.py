#! /usr/local/bin/python3

# https://www.lintcode.com/problem/palindrome-partitioning/description
# Example
# Given s = 'aab'
# Return
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

"""
Algo: 经典前序顺序无关DFS
D.S.:

Solution:
Solution1: DFS
Time: O(2^n)

Corner cases:
"""

class Solution1:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if s is None:
            return []

        ans = []
        subStrings = []
        self.dfs(s, subStrings, 0, ans)
        return ans

    def dfs(self, s, subStrings, startIdx, ans):
        if startIdx == len(s):
            ans.append(subStrings[:])
        for i in range(startIdx, len(s)):
            leftString = s[startIdx:(i + 1)]
            if not self.isPalindrome(leftString):
                continue
            subStrings.append(leftString)
            self.dfs(s, subStrings, i + 1, ans)
            subStrings.pop()

    def isPalindrome(self, string):
        size = len(string)
        if size <= 1:
            return True
        l, r = 0, size - 1
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

class Solution2:

    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(stringlist)
            # results.append(list(stringlist))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                # next recursion, passed in a new copy, instead of stringlist itself
                self.dfs(s[i:], stringlist + [prefix], results)
                # stringlist.append(prefix)
                # self.dfs(s[i:], stringlist, results)
                # stringlist.pop()
    # This is very neat
    def is_palindrome(self, s):
        return s == s[::-1]

# 提速方法
# 1. precalculate isPalindrome matrix
# 2. substring list 中存放分割的节点 而不是分好的子串，在写入result的时候转化成list of sub strings

# public class Solutio3 {
#     List<List<String>> results;
#     boolean[][] isPalindrome;
#
#     /**
#      * @param s: A string
#      * @return: A list of lists of string
#      */
#     public List<List<String>> partition(String s) {
#         results = new ArrayList<>();
#         if (s == null || s.length() == 0) {
#             return results;
#         }
#
#         getIsPalindrome(s);
#
#         helper(s, 0, new ArrayList<Integer>());
#
#         return results;
#     }
#
#     private void getIsPalindrome(String s) {
#         int n = s.length();
#         isPalindrome = new boolean[n][n];
#
#         for (int i = 0; i < n; i++) {
#             isPalindrome[i][i] = true;
#         }
#         for (int i = 0; i < n - 1; i++) {
#             isPalindrome[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));
#         }
#
#         for (int i = n - 3; i >= 0; i--) {
#             for (int j = i + 2; j < n; j++) {
#                 isPalindrome[i][j] = isPalindrome[i + 1][j - 1] && s.charAt(i) == s.charAt(j);
#             }
#         }
#     }
#
#     private void helper(String s,
#                         int startIndex,
#                         List<Integer> partition) {
#         if (startIndex == s.length()) {
#             addResult(s, partition);
#             return;
#         }
#
#         for (int i = startIndex; i < s.length(); i++) {
#             if (!isPalindrome[startIndex][i]) {
#                 continue;
#             }
#             partition.add(i);
#             helper(s, i + 1, partition);
#             partition.remove(partition.size() - 1);
#         }
#     }
#
#     private void addResult(String s, List<Integer> partition) {
#         List<String> result = new ArrayList<>();
#         int startIndex = 0;
#         for (int i = 0; i < partition.size(); i++) {
#             result.add(s.substring(startIndex, partition.get(i) + 1));
#             startIndex = partition.get(i) + 1;
#         }
#         results.add(result);
#     }
# }
# Test Cases
if __name__ == "__main__":
    solution = Solution()
