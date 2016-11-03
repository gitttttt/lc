from math import *

class Segment:
    def __init__(self, arr):
        h = int(ceil(log(len(arr), 2))) + 1
        self.arr = arr
        self.tree = [0 for _ in range(2**h)]
        self.build(arr, 0, 0, len(arr)-1)

    def build(self, arr, ti, l, h):
        if l == h:
            self.tree[ti] = arr[l]
            return
        mid = (l+h) / 2
        self.build(arr, 2*ti+1, l, mid)
        self.build(arr, 2*ti+2, mid+1, h)
        self.tree[ti] = self.tree[2*ti+1] + self.tree[2*ti+2]

    def rangeSum(self, i, j):
        return self.range(0, 0, len(self.arr)-1, i, j)

    def range(self, ti, l, h, i, j):
        if i > j:
            return self.range(ti, l, h, j, i)
        if i > h or j < l:
            return 0
        if i <= l and j >= h:
            return self.tree[ti]
        mid = (l+h) / 2
        if i > mid:
            return self.range(2*ti+2, mid+1, h, mid+1, j)
        if j <= mid:
            return self.range(2*ti+1, l, mid, i, mid)
        return self.range(2*ti+1, l, mid, i, mid) + self.range(2*ti+2, mid+1, h, mid+1, j)

    def updateVal(self, pos, val):
        self.update(0, 0, len(self.arr)-1, pos, val)

    def update(self, ti, l, h, pos, val):
        if l == h:
            self.tree[ti] = val
            return
        mid = (l+h) / 2
        if pos <= mid:
            self.update(2*ti+1, l, mid, pos, val)
        else:
            self.update(2*ti+2, mid+1, h, pos, val)
        self.tree[ti] = self.tree[2*ti+1] + self.tree[2*ti+2]

a = Segment([18, 17, 13, 19, 15, 11, 20, 12, 33, 25])
print a.rangeSum(1,4)
a.updateVal(1,0)
print a.rangeSum(1,4)

