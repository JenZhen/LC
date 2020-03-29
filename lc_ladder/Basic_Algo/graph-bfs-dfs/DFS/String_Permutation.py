#! /usr/local/bin/python3

# https://www.lintcode.com/problem/string-permutation/
# Example
# abcd is a permutation of bcad, but abbe is not a permutation of abe

"""
Algo:
D.S.: Array

Solution:
Iteration
Using array for frequency of char

Corner cases:
 so need to check invalidity using A is None or B is None
"""

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        if A is None or B is None or len(A) != len(B):
            return False

        arrA = [0 for i in range(256)]
        arrB = [0 for i in range(256)]
        for char in A:
            arrA[ord(char)] += 1
        for char in B:
            arrB[ord(char)] += 1

        for i in range(256):
            if arrA[i] != arrB[i]:
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
