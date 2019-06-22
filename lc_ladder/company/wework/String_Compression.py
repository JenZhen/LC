#! /usr/local/bin/python3

class Solution:
    def compress(self, chars) -> int:
        if not chars:
            return []
        s, f = 0, 0
        res = []
        while f < len(chars):
            while f < len(chars) and chars[f] == chars[s]:
                f += 1
            dist = f - s
            if dist > 1:
                res.append(chars[s])
                res.append(str(dist))
            else:
                res.append(chars[s])
            if f < len(chars):
                s = f
        return res


if __name__ == "__main__":
    testCases = [
        ["a","a","b","b","c","c","c"],
        []
    ]
    s = Solution()
    for t in testCases:
        res = s.compress(t)
        print(res)
