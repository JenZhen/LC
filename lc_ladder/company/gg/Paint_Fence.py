#! /usr/local/bin/python3

# https://www.lintcode.com/problem/paint-fence/description
# Example
# 我们有一个栅栏，它有n个柱子，现在要给柱子染色，有k种颜色可以染。
# 必须保证不存在超过2个相邻的柱子颜色相同，求有多少种染色方案。
#
# 样例
# n = 3, k = 2, return 6
#
#       post 1,   post 2, post 3
# way1    0         0       1
# way2    0         1       0
# way3    0         1       1
# way4    1         0       0
# way5    1         0       1
# way6    1         1       0
# 注意事项
# n和k都是非负整数

"""
Algo:
D.S.: DP 滚动数组

Solution:
Time: O(n), Space: O(1)
dp 分析
n = 1:
same = 0 # 和没有篱笆的涂法一样，是没有的
diff = k
ttl = k
n = 2:
same = prev_diff
diff = prev_ttl * (k - 1) # 之前共有k种方法，和之前不同的有k * (k - 1)
ttl = same + diff
n = 3:
...

要注意赋值顺序，same, diff, ttl

Corner cases:
100000 根篱笆， 1个颜色
当遍历到n = 3的时候 有same == 0, diff == 0, 意味着，以后也不会找到涂法了，所以可以直接返回0

"""

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if not n or not k:
            return 0
        diff = k
        same = 0
        ttl = k
        if n == 1:
            return ttl
        for i in range(2, n + 1):
            same = diff
            diff = ttl * (k - 1)
            ttl = same + diff
            if same == 0 and diff == 0:
                return 0
        return ttl

# Test Cases
if __name__ == "__main__":
    solution = Solution()
