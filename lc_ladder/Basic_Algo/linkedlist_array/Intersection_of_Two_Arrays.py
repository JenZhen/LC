#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/intersection-of-two-arrays/description/
# Intersection of two arrays, return has no duplicate element

"""
Algo:
D.S.: Array/Hashmap

Solution:
Follow Up 1:https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
Duplicate should be in the result

1. Sort then iterate thru two arrays to find out overlaps
2. Using map, in case of python using collections.Counter

Time Complexity:
Sort O(2 * nlogn)
check overlap O(n)
Corner cases:
"""
class Solution1(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		result = []
		nums1.sort()
		nums2.sort()
		p1, p2 = 0, 0
		while p1 < len(nums1) and p2 < len(nums2):
			if nums1[p1] == nums2[p2]:
				if len(result) == 0 or result[-1] != nums1[p1]:
					result.append(nums1[p1])
				# Note pointer move are outside the if
				# as long as it equal condition pointers move regardless appending or not
				p1 += 1
				p2 += 1

			elif nums1[p1] < nums2[p2]:
				p1 += 1
			else:
				p2 += 1
		return result

class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        result = []
        cnt = Counter(nums1)
        for item in nums2:
            if cnt[item] > 0:
                result.append(item)
                # Once found, cnter value goes to 0
                cnt[item] = 0
        return result

class Solution3(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Use generic dict {} to implement Counter
        # Note to check has_key whenever access map element
        result = []
        map = {}
        # save nums1 to a map, key nums element value, val repeating counter
        for ele in nums1:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        for ele in nums2:
        	# Do remember to check ele in map!!!!!!
            if ele in map and map[ele] > 0:
                result.append(ele)
                map[ele] = 0
        return result


class Solution_FollowUp1_1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1

            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return result


class Solution_FollowUp1_2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        result = []
        cnt = Counter(nums1)
        for item in nums2:
            if cnt[item] > 0:
                result.append(item)
                cnt[item] -= 1
        return result


# Test Cases
if __name__ == "__main__":
	solution = Solution()
	A = [1,2,2,1]
	B = [2,2]

	print solution.intersection(A, B)
