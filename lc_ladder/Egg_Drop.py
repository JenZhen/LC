#!/usr/bin/python

# 2 eggs, building of n floor. Say floor N is threshold that N or above
# dropping the egg, it will be broken; otherwise below N.
# How to find the N with minimum tests
# If drop below Nth floor, egg not broken and can be reused.

"""
Algo: Binary + Analysis of worst case
D.S.: Array/Math

Solution:
- Similar to binary search idea, need to find start with some level, test
if not broken, raise the level; if broken do narrow down.
- Since there are only 2 eggs, the first one can be usesd for rough estimation;
the second egg is for precision search, which has to be linear.
Ex1. Say building of 100 floors, expand every 20 floors, try worst cases
1 ---- 20 ---- 40 ---- 60 ---- 80 ---- 100
if N = 19, try 1 + 19 = 20
if N = 99, try 1 + 1 + 1 + 1 + 1 + 19 = 24 (worst case)
try fl20, fl40, fl60, fl80, fl100(broken), try from 81 till 99
Ex2. Say building of 100 floors, expand every 10 floors,
1 -- 10 -- 20 -- 30 -- 40 -- 50 -- 60 -- 70 -- 80 -- 90 -- 100
if N = 19, try 1 + 1 + 9 = 11
if N = 29, try 1 + 1 + 1 + 9 = 12
if N = 99, try 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 9 = 19

Sense that the cost is debating of how big the step(S) is (here is 20)
The bigger step, quick spotting first round esitmation O(1/S);
slower second round precison searching O(S)
Goal: find a way to seperate total floor s.t. worst case in each section 
the same. Since in section x(10-20) will have 1 more test in round 1 than
in section x - 1(1-10), then we can shorten section x by 1 to make worst
cases of x and x - 1 the same.
Hence s + (s - 1) + (s - 2) + (s - 3) + ... + 2 + 1 = n (take ceiling of s)
In worst case scenarios, try 1 + (s - 1) = s times

"""
class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    def dropEggs(self, n):
    	import math
    	'''
    	Need to find the first s that makes s(s + 1) / 2 > n (ceiling)
    	s + (s - 1) + ... + 2 + 1 = s(s + 1) / 2 = n
    	s(s + 1) = 2n --> s * s < s(s + 1) = 2n
    	start to try s from s = sqrt(2n)
    	'''
    	s = int(math.sqrt(2 * n))
    	while s * (s + 1) < n:
    		s += 1;
    	return s
    	

# Test Cases
if __name__ == "__main__":
	inputs = [0, 1, 30, 50, 100]
	# res = [0,  1, 7, 10, 14]
	solution = Solution()
	for testcase in inputs:
		print solution.dropEggs(testcase)




