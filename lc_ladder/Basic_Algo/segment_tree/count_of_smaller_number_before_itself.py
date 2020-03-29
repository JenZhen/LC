#! /usr/local/bin/python3

"""
Solution1: Nested loop
Time: O(n ^ 2)
Space: O(n)
OJ has timeout issue
"""
class Solution1:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return []
        ans = [0] * len(A)
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                if A[j] < A[i]:
                    ans[i] += 1
        return ans


###################################################################
# SegmentTree Solution

class SegmentTreeNodeCnt(object):
    def __init__(self, start, end, cnt=0):
        self.start, self.end, self.cnt = start, end, cnt
        self.left, self.right = None, None

class SegmentTreeCnt(object):
    def __init__(self, start, end): # init a tree with range
        self.root = self._build(start, end) # init cnt/sum = 0
    def _build(self, start, end):
        if start > end:
            return None
        elif start == end:
            return SegmentTreeNodeCnt(start, end)
        else:
            root = SegmentTreeNodeCnt(start, end)
            mid = (start + end) // 2
            root.left = self._build(start, mid)
            root.right = self._build(mid + 1, end)
            return root
    def query(self, start, end):
        # Invalid cases return None
        return self._query(self.root, start, end)

    def _query(self, root, start, end):
        if root is None:
            return None
        if start > end: # query cnt before 0; ie (0, -1) -> cnt: 0
            return 0
        if start <= root.start and root.end <= end:
            return root.cnt
        ans = 0
        mid = (root.start + root.end) // 2
        if mid >= start:
            ans += self._query(root.left, start, end)
        if mid + 1 <= end:
            ans += self._query(root.right, start, end)
        return ans

    def modify(self, index, increValue=1):
        self._modify(self.root, index, increValue)

    def _modify(self, root, index, increValue=1):
        if root.start == root.end and root.start != index:
            return
        if root.start == index and root.end == index:
            root.cnt += increValue
            return
        mid = (root.start + root.end) // 2
        if mid >= index:
            self._modify(root.left, index, increValue)
        else:
            self._modify(root.right, index, increValue)
        root.cnt = root.left.cnt + root.right.cnt
        return

class Solution2:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        segTree = SegmentTreeCnt(0, 10000) # init an empty tree of certain length
        res = []
        for ele in A:
            # First query range (0, ele - 1), then modify node ele in tree
            cnt = segTree.query(0, ele - 1)
            res.append(cnt)
            segTree.modify(ele) # default modification value increment is 1
        return res


if __name__ == "__main__":
    testCases = [
        {
            "A": [1,2,7,8,5], # returns [0,1,2,3,2]
        }
    ]
    s1 = Solution1()
    s2 = Solution2()
    for t in testCases:
        A = t["A"]
        res1 = s1.countOfSmallerNumberII(A)
        res2 = s1.countOfSmallerNumberII(A)
        print("res1: %s" %repr(res1))
        print("res2: %s" %repr(res2))
