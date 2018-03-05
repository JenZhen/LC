# strStr
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""
Algo: Brutal Force
D.S.: String manipulation

Solution:
- Use the most straight forward method
- Time Complexity: O(len(haystack) * len(needle))

Corner cases:
- Invalidity check, return -1
	1. haystack is None
	2. needle is None
	3. len(haystack) < len(needle)
- Quick answer
	1. len(needle) == 0 -> return 0
"""

class Solution(object):

	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if haystack is None or needle is None:
			return -1
		lenH = len(haystack)
		lenN = len(needle)
		if lenN == 0:
			return 0
		if lenH < lenN:
			return -1
		for i in range (lenH - lenN + 1):
			for j in range (lenN):
				if haystack[i + j] != needle[j]:
					break
				if j == lenN - 1:
					return i
		return -1

# Test Cases
if __name__ == "__main__":
	solution = Solution()

	# 1. At least one of the input is None -> -1
	haystack = None
	needle = None
	print solution.strStr(haystack, needle)

	# 2. needle is longer than haystack -> -1
	haystack = ''
	needle = '1'
	print solution.strStr(haystack, needle)

	# 3. needle is 0 of length -> 0
	haystack = '' # or any other length
	needle = ''
	print solution.strStr(haystack, needle)

	# 4. needle not found in haystack -> -1
	haystack = '123'
	needle = 'a'
	print solution.strStr(haystack, needle)

	# 5. needle found in haystack -> n
	haystack = '1234'
	needle = '3'
	print solution.strStr(haystack, needle)


