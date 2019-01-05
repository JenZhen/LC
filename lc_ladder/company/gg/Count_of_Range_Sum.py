#! /usr/local/bin/python3

# https://www.lintcode.com/problem/count-of-range-sum/description?_from=ladder&&fromId=18
# Example
# 给定一个整数数组nums，返回[lower，upper]范围内的区间和。
# 区间和S(i, j)被定义为索引i和j(i ≤ j)之间（包含i和j）的nums中所有元素的和。
#
# 样例
# 给出nums = [-2, 5, -1], lower = -2, upper = 2,
# 返回3.
# 三个区间分别是: [0, 0], [2, 2], [0, 2] ，它们对应的区间和分别为: -2, -1, 2.
#
# 注意事项
# 暴力解法的时间复杂度为O(n^2)。给出的解法必须好于这个方法。

"""
Algo:
D.S.:

Solution:
TOO DIFFICULT
how to improve to n^2 to nlogn
Possible Solution
1. binary seach
2. MergeSort
3. segmentTree

Corner cases:
"""

class Solution {
public:
    /**
     * @param nums: a list of integers
     * @param lower: a integer
     * @param upper: a integer
     * @return: return a integer
     */
    int countRangeSum(vector<int> &nums, int lower, int upper) {
        if (nums.empty()) {
            return 0;
        }

        if (nums.size() == 1) {
            if (nums[0] >= lower && nums[0] <= upper) {
                return 1;
            }
            else {
                return 0;
            }
        }

        vector<int> prefixSum(nums.size() + 1, 0);

        for (int i = 1; i <= nums.size(); ++i) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
        }

        int mid = nums.size() / 2;

        return MergeSort(0, prefixSum.size() - 1, lower, upper, prefixSum);
    }

    int MergeSort(int start, int end, int lower, int upper, vector<int> &prefixSum) {

        if (start == end) {
            return 0;
        }

        int count = 0, mid = (start + end) / 2;

        count += MergeSort(start, mid, lower, upper, prefixSum);
        count += MergeSort(mid + 1, end, lower, upper, prefixSum);

        int front = start, back = start;

        //Collect the valid combinations
        for (int i = mid + 1; i <= end; ++i) {
            while (front <= mid && prefixSum[i] - prefixSum[front] > upper) {
                front++;
            }
            while (back <= mid && prefixSum[i] - prefixSum[back] >= lower) {
                back++;
            }
            count += (back - front);
        }

        //Merge sort the two parts
        int pos = 0;
        int i = start, j = mid + 1;
        vector<int> tmp (end - start + 1, 0);

        while (i <= mid || j <= end) {
            if (i > mid) {
                tmp[pos++] = prefixSum[j++];
                continue;
            }
            if (j > end ) {
                tmp[pos++] = prefixSum[i++];
                continue;
            }
            if (prefixSum[i] <= prefixSum[j]) {
                tmp[pos++] = prefixSum[i++];
                continue;
            }
            tmp[pos++] = prefixSum[j++];
        }

        for (int i = start; i <= end; ++i) {
            prefixSum[i] = tmp[i - start];
        }

        return count;
    }
};

# Test Cases
if __name__ == "__main__":
    solution = Solution()
