# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.part(nums)

    def part(self, arr):
        mid = (len(arr)-1)/2
        head = TreeNode(arr[mid])
        head.left = self.part(arr[:mid:])
        head.right = self.part(arr[mid+1::])
        return head

