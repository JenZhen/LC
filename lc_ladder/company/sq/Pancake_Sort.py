#! /usr/local/bin/python3

# Requirement
# Example
# 一堆 pancakes, 根据大小排序，但是要先 implement swap(List<Pancake> pancakes, int end),
#  把从 index 0 ~ end 的pancakes的顺序全部倒过来，然后用这个方法正常排序pancakes, 最后size 从小到大。
# 比如 {3, 2, 5, 4, 6}  swap(pancakes, 3) 之后是 {4, 5, 2, 3, 6} implement 一个方法 不停地 swap 得到 {2, 3, 4, 5, 6}, 数字表示对应 pancake size

"""
Algo: Sorting
D.S.:

Solution:
Swap Sort
Time: O(N^2)

Corner cases:
"""
def findMaxIdx(arr, cnt):
    idx = 0
    max = arr[0]
    for i in range(1, cnt + 1):
        if arr[i] > max:
            max = arr[i]
            idx = i
    return idx

def reverse(arr, cnt):
    l, r = 0, cnt
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1

def pancakeSort(arr):
    if not arr:
        return arr

    cnt = len(arr) - 1
    while cnt >= 1:
        maxIdx = findMaxIdx(arr, cnt)
        # if maxIdx at last of current range, cnt -= 1 do nothing
        if maxIdx == cnt:
            cnt -= 1
            continue
        # shift maxIdx element to front
        reverse(arr, maxIdx)
        # shift the maxIdx element to cnt (last position of current range)
        reverse(arr, cnt)
        cnt -= 1
    return arr


# Test Cases
if __name__ == "__main__":
    testCases = [
        [],
        [1],
        [1, 2],
        [3, 2, 1],
        [2, 1, 5, 3, 4]
    ]
    for arr in testCases:
        res = pancakeSort(arr)
        print(res)
