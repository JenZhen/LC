#! /usr/local/bin/python3

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 离散化array
# Binary Indexed tree (not related to)

"""
Solution1:
input:    [5,2,6,6,1]
reverse:  [1,6,6,2,5] 从右往左看比他小的，所以要reverse order

sorted:   [1,2,5,6] # unique numbers
rank:     [0,1,2,3]

reverse:  [1,6,6,2,5]
with rank:[0,3,3,1,2]

rank_cnt: [0,1,2,3], # iterate revese list and populate rank count at the same time
          [1,0,0,0]  # add 1 这个1的左侧没有比他更小的了
          [1,0,0,1]  # add first 6 这个6左侧有一个1比他小，sum(rank_cnt[0:rank])
最后要记得翻转结果

Time: O(nlogn) -- n 是给定序列的unique元素数量，约等于原序列长度
Space： O(n)


"""


class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        ranks = {} #key,num, val,rank starting from 0
        sorted_nums = sorted(list(set(nums)))
        for i in range(len(sorted_nums)):
            ranks[sorted_nums[i]] = i
        res = []
        cnt = [0] * len(ranks)
        for num in nums[::-1]:
            rank_num = ranks[num]
            if rank_num == 0:
                res.append(0)
            else:
                res.append(sum(cnt[0:rank_num]))
            cnt[rank_num] += 1
        return res[::-1]
