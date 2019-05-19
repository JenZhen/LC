#! /usr/local/bin/python3

# Requirement
# Example
# input: {ab}c{de}
# output: [acd], [bcd], [ace], [bce]
"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Solution1:
    def getCombination(self, string):
        if not string:
            return []
        input = []
        in_combo = False
        start = None
        for i in range(len(string)):
            if string[i] == '{':
                start = i
                in_combo = True
            elif string[i] == '}':
                combo = string[start+1:i]
                if len(combo) > 0:
                    input.append(combo)
                in_combo = False
            else:
                if in_combo:
                    continue
                else:
                    input.append(string[i])
        res = [""]
        for group in input:
            base_length = len(res)
            temp_res = []
            for char in group:
                for prev in res:
                    temp_res.append(prev + char)
            res = temp_res
        return res

class Solution2:
    def getCombination(self, string):
        if not string:
            return []
        input = []
        in_combo = False
        start = None
        for i in range(len(string)):
            if string[i] == '{':
                start = i
                in_combo = True
            elif string[i] == '}':
                combo = string[start+1:i]
                if len(combo) > 0:
                    input.append(combo)
                in_combo = False
            else:
                if in_combo:
                    continue
                else:
                    input.append(string[i])

        # print('test input: %s' %repr(input))

        res = []
        path = ""
        startwith = 0
        self.dfs(res, input, startwith, path)
        return res

    def dfs(self, res, input, startwith, path):
        if len(path) == len(input):
            res.append(path[:])
            return

        for char in input[startwith]:
            path += char
            self.dfs(res, input, startwith + 1, path)
            path = path[:-1]

# Test Cases
if __name__ == "__main__":
    solution1 = Solution1()
    solution2 = Solution2()
    test_cases = [
        '{}ab',
        '{ab}c{de}',
        '{a}b{}'
    ]

    for t in test_cases:
        res1 = solution1.getCombination(t)
        print(res1)
        # res2 = solution2.getCombination(t)
        # print(res2)
