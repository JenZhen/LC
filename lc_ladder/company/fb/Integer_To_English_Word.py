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
class Solution1: # Suggested
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        # print(rest)
        res = ''
        if billion:
            res += self.three(billion) + ' Billion'
        if million:
            res += ' ' if res else ''
            res += self.three(million) + ' Million'
        if thousand:
            res += ' ' if res else ''
            res += self.three(thousand) + ' Thousand'
        if rest:
            res += ' ' if res else ''
            res += self.three(rest)
        return res

    def three(self, num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return self.one(hundred) + ' Hundred '+ self.two(rest)
        elif not hundred and rest:
            return self.two(rest)
        elif hundred and not rest:
            return self.one(hundred) + ' Hundred'
        # cannot be not hundred and not rest

    def one(self, num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher[num]

    def two(self, num):
        if not num: return ''
        if num < 10:
            return self.one(num)
        elif num < 20:
            return self.two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            if tenner and rest:
                return self.ten(tenner) + ' ' + self.one(rest)
            elif tenner and not rest:
                return self.ten(tenner)

    def ten(self, num):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher[num]

    def two_less_20(self, num):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher[num]

class Solution2:
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
