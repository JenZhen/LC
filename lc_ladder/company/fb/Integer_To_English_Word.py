#! /usr/local/bin/python3

# https://www.lintcode.com/problem/integer-to-english-words/description
# Example

"""
Algo: math, string
D.S.:

Solution:
高频！

Corner cases:
很多很多细节
1. 40，48： 表达式fourty后面有没有空格

"""


class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        if num is None:
            return None
        if num == 0:
            return "Zero"

        scale = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion"
        }

        # 123,456,789 -> [789, 456, 123]
        arr = self._split_integer(num)
        print(arr)
        res = ""

        for i in range(len(arr)):
            hundred_expression = self._convert_to_hundred(arr[i])
            if scale[i] == "":
                res = hundred_expression + res
            else:
                res = hundred_expression + " " + scale[i] + " " + res
        return res

    def _split_integer(self, num):
        res = []
        while num > 1000:
            res.append(num % 1000)
            num = num // 1000
        res.append(num)
        return res

    def _convert_to_hundred(self, num):
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        if num == 0:
            return ""
        elif num < 20:
            return lessThan20[num]
        elif num < 100:
            temp = self._convert_to_hundred(num % 10)
            ten = tens[num // 10]
            return ten + " " + temp if temp != "" else ten
        else:
            return lessThan20[num // 100] + " Hundred " + self._convert_to_hundred(num % 100)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
