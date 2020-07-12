#! /usr/local/bin/python3

# https://leetcode.com/problems/product-of-the-last-k-numbers/
# Example
# Implement the class ProductOfNumbers that supports two methods:
# 1. add(int num)
# Adds the number num to the back of the current list of numbers.
# 2. getProduct(int k)
#
# Returns the product of the last k numbers in the current list.
# You can assume that always the current list has at least k numbers.
# At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
#
# Example:
# Input
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
# [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
#
# Output
# [null,null,null,null,null,null,20,40,0,null,32]
#
# Explanation
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3);        // [3]
# productOfNumbers.add(0);        // [3,0]
# productOfNumbers.add(2);        // [3,0,2]
# productOfNumbers.add(5);        // [3,0,2,5]
# productOfNumbers.add(4);        // [3,0,2,5,4]
# productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
# productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        // [3,0,2,5,4,8]
# productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32
#
#
# Constraints:
#
# There will be at most 40000 operations considering both add and getProduct.
# 0 <= num <= 100
# 1 <= k <= 40000
"""
Algo: presum, pre-product, 细节
D.S.:

Solution:
技巧，记录最近一次0出现的idx
如果求的区间 有0出现，直接返回0
有0出现 当前累计的乘积为1， 后面在1的基础上 算乘积

Time:
add: O(1)
getProduct: O(1)
Space: O（n)

FollowUP:
sliding window product

Corner cases:
"""

class ProductOfNumbers:
    def __init__(self):
        self.q = []
        self.last_zero_pos = -1

    def add(self, num: int) -> None:
        n = len(self.q)
        if n == 0:
            # if empty, first element
            if num == 0:
                self.last_zero_pos = n
                self.q.append(1)
            else:
                self.q.append(num)
        else:
            if num == 0:
                self.last_zero_pos = n
                self.q.append(1)
            else:
                self.q.append(num * self.q[-1])

    # add can be simplified as
    def add(self, num: int) -> None:
        n = len(self.q)
        if num == 0:
            self.last_zero_pos = n
            self.q.append(1)
        else:
            if n == 0:
                self.q.append(num)
            else:
                self.q.append(num * self.q[-1])


    def getProduct(self, k: int) -> int:
        start_idx = len(self.q) - k
        if start_idx >= 0 and self.last_zero_pos >= start_idx:
            # has 0 in the range
            return 0
        if start_idx <= 0:
            return self.q[-1]
        else:
            return self.q[-1] // self.q[start_idx - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
