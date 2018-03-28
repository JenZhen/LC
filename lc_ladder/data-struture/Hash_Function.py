#!/usr/bin/python

# http://www.lintcode.com/en/problem/hash-function/
# Example

"""
Algo:
D.S.:

Solution:
Example = 'ab'

as algo
ans = (ord('a') * 33 + ord('b')) % HASH_SIZE
    = ((ord('a') * 33) % HASH_SIZE + (ord('b')) % HASH_SIZE
      ) % HASH_SIZE

as function
a: ans = a % HASH_SIZE
b: ans = (33 * ord('a') % HASH_SIZE + ord('b')) % HASH_SIZE

Do not multiple all up then % too slow and overflow

Corner cases:
"""
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for char in key:
            ans = (33 * ans + ord(char)) % HASH_SIZE
        return ans
# Test Cases
if __name__ == "__main__":
	solution = Solution()
