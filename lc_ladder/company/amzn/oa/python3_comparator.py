#! /usr/bin/python

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
Solution1 only works for python2

Corner cases:
"""

class Solution1:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        if not logs:
            return logs


        def cmpFunction(a, b):
            idxA = a.find(" ")
            titleA = a[:idxA]
            conA = a[idxA + 1:]
            idxB = b.find(" ")
            titleB = b[:idxB]
            conB = b[idxB + 1:]
            if conA != conB:
                if conA < conB:
                    return -1
                else:
                    return 1
            if titleA < titleB:
                return -1
            else:
                return 1

        res = sorted(logs, cmp=cmpFunction)
        print("res: %s" %res)
        ans = []
        for log in res:
            idx = log.find(" ")
            if log[idx + 1].isalpha():
                ans.append(log)
        for log in logs:
            idx = log.find(" ")
            if not log[idx + 1].isalpha():
                ans.append(log)
        return ans


# Test Cases
# if __name__ == "__main__":
#     solution = Solution()


####################################
# Following test case is for python3
####################################

ppl = [
    ('john', 'E', 15),
    ('peter', 'B', 18),
    ('may', 'D', 11),
    ('ling', 'C', 11),
    ('ling', 'A', 19),
]

s0 = sorted(ppl, key=lambda x: x[2])
# print("s0: %s" %s0)

def cmp1(p1):
    return p1[2], p1[0]
s1 = sorted(ppl, key=cmp1)
print("s1: %s" %s1)


# age < 15 at front, then sort by p[1]
# age >+ 15 at back,  o more sort
def cmp1(p1):
    return p1[2] - 15, p1[1]
s2 = sorted(ppl, key=cmp1)
print("s2: %s" %s2)
