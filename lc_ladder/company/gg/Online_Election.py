#! /usr/local/bin/python3

# Requirement
# https://leetcode.com/problems/online-election/submissions/
# In an election, the i-th vote was cast for persons[i] at time times[i].
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.
#
# Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.
#
# Example 1:
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation:
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
#
# Note:
#
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
"""
Algo: binary search, bisect
D.S.:

Solution:
Time: O(len(Persons) + nlog(Persons)) -- n is number of query called
Space: O(len(Persons))

Corner cases:
"""

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = {} # key: person, val: # of votes
        self.time_series = [] # list of tuple (timestamp, leader)
        leader = None
        leader_count = 0
        for i in range(len(persons)):
            p, t = persons[i], times[i]
            c = count.get(p, 0)
            c += 1
            count[p] = c
            # use c >= leader_count, 跟新最新的leader
            if c >= leader_count:
                leader_count = c
                leader = p
            self.time_series.append((t, leader))
        print(self.time_series)
    def q(self, t: int) -> int:
        pos = bisect.bisect(self.time_series, (t, sys.maxsize))
        # pos == 0 query time before anyone has voted
        if pos == 0:
            return None
        return self.time_series[pos - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
