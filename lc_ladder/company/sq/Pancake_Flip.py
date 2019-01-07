#! /usr/local/bin/python3

# Requirement
# Example
# 也是一堆 pancakes, 现在有两面，有的是正面朝下，有的是反面朝下，
# 也是implement swap(List<Pancake> pancakes, int end),
# 把从 index 0 ~ end 的pancakes的顺序全部倒过来，同时对应的面也要反过来， 最后要得到的结果是全部正面朝上。

"""
Algo: Sorting
D.S.:

Solution:
Time: O(n ^ 2)

Corner cases:
"""

def reverse(arr, cur):
    l, r = 0, cur
    while l < r:
        temp = arr[l]
        arr[l] = not arr[r]
        arr[r] = not temp
        l += 1
        r -= 1
    if l == r:
        arr[l] = not arr[l]

def flipPancake(arr):
    if not arr:
        return arr
    cur = len(arr) - 1
    while cur >= 0:
        while cur >= 0 and arr[cur] == True:
            cur -= 1
        if cur == -1:
            return arr
        if cur == 0:
            arr[0] = True
            return arr
        # flip arr[0] to be False if needed
        arr[0] = False
        reverse(arr, cur)
        cur -= 1
    return arr

# Test Cases
if __name__ == "__main__":
    testCases = [
        [],
        [False],
        [True],
        [True, True],
        [False, False],
        [True, False],
        [False, True],
        [True, False, True],
        [False, True, False]
    ]
    for arr in testCases:
        res = flipPancake(arr)
        print(res)
