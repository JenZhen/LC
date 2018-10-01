#! /usr/local/bin/python3

# https://www.lintcode.com/problem/number-of-restaurants/description?_from=ladder&&fromId=62
# Example

"""
Algo:
D.S.: Use min heap twice for sorting with secondary index

Solution:
Time: O(nlogn) * 2 (n <= number of restaurant) 相当于heap sort 2 遍
Space: O(n)
Corner cases:
"""
class Solution:
    """
    @param restaurant:
    @param n:
    @return: nothing
    """
    def nearestRestaurant(self, restaurant, n):
        # Write your code here
        if not restaurant or not n or n > len(restaurant):
            return []

        from heapq import heappush, heappop
        # use min heapq twice
        def dist(x, y):
            return x ** 2 + y ** 2
        distHeap = []
        orderHeap = []
        res = []
        for i, [x, y] in enumerate(restaurant):
            heappush(distHeap, (dist(x, y), i, [x, y]))
        for _ in range(n):
            heappush(orderHeap, (heappop(distHeap)[1:]))
        while len(orderHeap):
            res.append(heappop(orderHeap)[1])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
