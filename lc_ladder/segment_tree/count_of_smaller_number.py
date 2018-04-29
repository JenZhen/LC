#! /usr/local/bin/python3

"""
Solution1: use cnt array
A length n, queries m (ignore)
Time Complexit: O(n + max(A))
Space Complexity: O(max(A)) upto 10000
"""
class Solution1:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    note if A = [] or A is None return [0, 0, 0, ... ]
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        maxNumber = max(A) if len(A) != 0 else 0
        cnt = [0] * (maxNumber + 1)
        for ele in A:
            cnt[ele] += 1
        ans = []
        for q in queries:
            if q > len(cnt) - 1:
                res = sum(cnt[:])
            else:
                res = sum(cnt[:q])
            ans.append(res)
        return ans

"""
Solution2: Sort A + Binary search
A length n, queries m (ignore)
Time Complexit: O(nlogn + logn)
Space Complexity: O(m)
"""
class Solution2:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if not A and queries:
            return [0] * len(queries)

        A.sort()
        ans = []
        # find the first occurance of target, it's index is how many element
        # smaller than it
        def findFirstQ(A, q):
            l, r = 0, len(A) - 1
            while l + 1 < r:
                mid = (l + r) // 2
                if A[mid] >= q:
                    r = mid
                else:
                    l = mid
            if q <= A[l]:
                return l
            else:
                return r
        for q in queries:
            ans.append(findFirstQ(A, q))
        return ans

###################################################################
# SegmentTree Solution

class SegmentTreeNodeCnt(object):
    def __init__(self, start, end, cnt=0):
        self.start, self.end, self.cnt = start, end, cnt
        self.left, self.right = None, None

    def __repr__(self):
        repr = "start: " + str(self.start)  \
             + ", end: " + str(self.end) \
             + ", cnt: " + str(self.cnt)
        return repr

class SegmentTreeCnt(object):
    def __init__(self):
        self.root = None

    def build(self, start, end):
        self.root = self._build(start, end)

    def _build(self, start, end):
        # This is to build an empty tree
        if start >= end:
            return SegmentTreeNodeCnt(start, end)
        else:
            mid = (start + end) // 2
            root = SegmentTreeNodeCnt(start, end)
            root.left = self._build(start, mid)
            root.right = self._build(mid + 1, end)
            return root

    def modify(self, root, index, value):
        print("tree info :%s" %repr(root))
        if root.start == root.end and root.start != index:
            return
        if root.start == index and root.end == index:
            root.cnt += value
            return
        mid = (root.start + root.end) // 2
        if index <= mid: # go to left sub tree
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        root.cnt = root.left.cnt + root.right.cnt
        return

    def query(self, root, start, end):
        if root is None:
            return None
        if start <= root.start and root.end <= end:
            return root.cnt
        mid = (root.start + root.end) // 2
        ans = 0
        if mid >= start: # overlap with left sub tree
            ans += self.query(root.left, start, end)
        if mid + 1 <= end: # overlap with right sub tree
            ans += self.query(root.right, start, end)
        return ans

class Solution3:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        # build segment tree
        segTree = SegmentTreeCnt()
        segTree.build(0, 10000)
        # print("tree root: %s" %repr(segTree.root))
        result = []

        # modify count value for each
        for num in A:
            print("now modify %s" %num)
            segTree.modify(segTree.root, num, 1)

        for i in queries:
            count = 0
            if i > 0:
                count = segTree.query(segTree.root, 0, i - 1)
            result.append(count)

        return result

if __name__ == "__main__":
    testCases = [
        {
            "A": [1,2,3,4,5,6],
            "queries": [1,2,3,4]
        }
    ]
    s3 = Solution3()
    for t in testCases:
        A = t["A"]
        queries = t["queries"]
        res3 = s3.countOfSmallerNumber(A, queries)
        print("res3: %s" %repr(res3))
