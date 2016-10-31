class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.lp = None
        self.rp = None
        self.v = 0

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.build(0, len(nums)-1, nums)

    def build(self, l, r, arr):
        if l > r:
            return
        else:
            root = Node(l, r)
            if l != r:
                mid = (l+r)/2
                root.lp = self.build(l, mid, arr)
                root.rp = self.build(mid+1, r, arr)
            root.v = arr[l] if l == r else root.lp.v + root.rp.v
            return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.up(self.root, i, val)

    def up(self, root, pos, val):
        if root.l == root.r:
            root.v = val
        else:
            mid = (root.l + root.r)/2
            if mid < pos:
                self.up(root.rp, pos, val)
            else:
                self.up(root.lp, pos, val)
            root.v = root.lp.v + root.rp.v


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumR(self.root, i, j)

    def sumR(self, root, i, j):
        if root.l == i and root.r == j:
            return root.v
        mid = (root.l+root.r)/2
        if i >= mid+1:
            return self.sumR(root.rp, i, j)
        if j <= mid:
            return self.sumR(root.lp, i, j)
        return self.sumR(root.lp, i, mid) + self.sumR(root.rp, mid+1, j)



        # Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,2,3,4])
print numArray.sumRange(0, 1)
numArray.update(1, 10)
print numArray.sumRange(1, 2)