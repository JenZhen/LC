#! /usr/local/bin/python3

# https://leetcode.com/problems/trapping-rain-water/
# Example

"""
Algo: Two-side， monotonous stack
D.S.:

Solution1:
两边夹算法
Time: O(n)
Space: O(1)

Solution2:
monotonous stack 单调栈 （栈内递减）
严格递减 或是 不严格递减 都可以
Time: O(n)
Space: O(n)
Corner cases:
"""
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        lHeight = heights[l]
        rHeight = heights[r]
        res = 0
        while l < r:
            if lHeight < rHeight:
                # search left side
                l += 1
                if lHeight > heights[l]:
                    res += (lHeight - heights[l])
                else:
                    lHeight = heights[l]
            else:
                # search right side
                r -= 1
                if rHeight > heights[r]:
                    res += (rHeight - heights[r])
                else:
                    rHeight = heights[r]
        return res

class Solution2:
    def trap(self, height: List[int]) -> int:
        res = 0
        i = 0
        st = []
        while i < len(height):
            # height[i] >= height[st[-1]] or height[i] > height[st[-1]]
            while (st and height[i] >= height[st[-1]]):
                lowest_idx = st.pop()
                if len(st) == 0:
                    break # break inner while try next i
                width = i - st[-1] - 1
                depth = min(height[i], height[st[-1]]) - height[lowest_idx]
                res += (width * depth)
            st.append(i)
            i += 1
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
