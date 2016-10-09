class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.left = [nums[0]]
        self.right = [nums[-1]]
        for i in range(1, len(nums)/2+1):
            self.left.append(self.left[-1] + nums[i])
            self.right.insert(0, self.right[0] + nums[-i-1])
        print self.left
        print self.right

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """



        # Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4,5]
numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)