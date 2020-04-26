#! /usr/local/bin/python3

# https://www.lintcode.com/problem/student-attendance-record-i/description?_from=ladder&&fromId=18
# Example

"""
Algo: string iteration
D.S.: string

Solution:
Time: O(n) Space: O(1)

Corner cases:
"""
class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """
    def checkRecord(self, s):
        # Write your code here
        if not s:
            return True
        cntA = 0 # not consecutive counting
        cntL = 0 # consecutive counting
        for i in s:
            if i == 'A':
                cntA += 1
                if cntA > 1:
                    return False
                cntL = 0
            elif i == 'L':
                cntL += 1
                if cntL > 2:
                    return False
            else:
                cntL = 0
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
