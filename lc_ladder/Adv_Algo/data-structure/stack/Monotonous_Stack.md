#  单调栈、队列的应用

单调递增 -- 栈、队列中的元素是递增的（严格或非严格）
单调递增 -- 栈、队列中的元素是递增的（严格或非严格）

### 单调递增栈可以找到左起第一个比当前数字小的元素
#### Example
[2,1,5,6,2,3]
* 2：[2] 2左侧没有比它小
* 1: [~~2~~, 1] 1左侧没有比它小
* 5: [1, 5] 1左侧1比它小
* 6: [1, 5, 6] 6左侧5比它小
* 2: [1, ~~5~~, ~~6~~, 2] 2左侧1比它小
* 3: [1, 2, 3] 3左侧2比它小

### 单调递减栈可以找到左起第一个比当前数字大的元素
#### Example
[2,1,5,6,2,3]
* 2: [2]
* 1: [2, 1]
* 5: [~~2~~, ~~1~~, 5]
* 6: [~~5~~, 6]
* 2: [6, 2]
* 3: [6, ~~2~~, 3]

### 同理，从右往左可以找到右起第一个比当前数字大、小的元素

### 题目
* LC 84  https://leetcode.com/problems/largest-rectangle-in-histogram/
* LC 239 https://leetcode.com/problems/sliding-window-maximum/
* LC 402 https://leetcode.com/problems/remove-k-digits/submissions/
* LC 496 https://leetcode.com/problems/next-greater-element-i/
* LC 503 https://leetcode.com/problems/next-greater-element-ii/
* LC 739 https://leetcode.com/problems/daily-temperatures/
* LC 768 https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
* LC 901 https://leetcode.com/problems/online-stock-span/
* LC 862 https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
* LC 1438 https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
