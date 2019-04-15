#! /usr/local/bin/python3

# https://www.lintcode.com/problem/text-justification/description
# Example
# 给定一个单词数组和一个宽度maxWidth，格式化文本，使每行具有刚好maxWidth个字符并完全（左和右）对齐。
#
# 你应该用贪心法打包你的单词; 也就是说，在每行中包含尽可能多的单词。 必要时填充额外的空格，以便每行具有正确的maxWidth字符。
#
# 单词之间的额外空格应尽可能均匀分布。 如果一行上的空格数不均匀分配，则左侧的空插槽将分配比右侧插槽更多的空格。
#
# 对于最后一行文本，它应该是左对齐的，并且在单词之间不插入额外的空格。
#
# 样例
# 样例 1:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 样例 2:
#
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 说明：请注意，最后一行是 "shall be    " 而不是 "shall     be"，
#               因为最后一行必须左对齐而不是完全对齐。
#               请注意，第二行也是左对齐的，因为它只包含一个单词。
# 样例 3:
#
# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
# 注意事项
# ·单词定义为仅由非空格字符组成的字符序列。
# ·每个单词的长度保证大于0且不超过maxWidth。
# ·输入数组words至少包含一个单词。
"""
Algo: Math
D.S.:

Solution:
思路直接，注意细节！
Time: O(n)
Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        if not words:
            return [""]

        line, length = [], 0
        results = []
        for w in words:
            if length + len(w) + len(line) <= maxWidth:
                length += len(w)
                line.append(w)
            else:
                results.append(self._format_line(line, maxWidth))
                length = len(w)
                line = [w]
        if len(line):
            results.append(self._format_last_line(line, maxWidth))
        return results

    def _format_last_line(self, line, maxWidth):
        s = " ".join(line)
        return s + " " * (maxWidth - len(s))

    def _format_line(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        # option 1
        # s, gaps = line[0], len(line) - 1
        # for index, w in enumerate(line[1:]):
        #     if index < (maxWidth - length) % gaps:
        #         s = s + " " + " " * ((maxWidth - length) // gaps) + w
        #     else:
        #         s = s + " " * ((maxWidth - length) // gaps) + w
        # option2
        space_length = maxWidth - length
        gaps_count = len(line) - 1
        base_length = space_length // gaps_count
        remaining = space_length % gaps_count
        s = ""
        for i in range(len(line) - 1):
            # add one “ ” for each space from left to right
            if i < remaining:
                s += line[i] + " " * base_length + " " #add one " "for the remaining one
            else:
                s += line[i] + " " * base_length
        # don't forget to add the last word
        s += line[-1]
        return s

# Test Cases
if __name__ == "__main__":
    solution = Solution()
