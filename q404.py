# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        if not node:
            return 0
        if not node.left and not node.right:
            return 0
        if not node.left:
            return self.sumOfLeftLeaves(node.right)
        if node.left and not node.left.left and not node.left.right:
            return 1 + self.sumOfLeftLeaves(node.right)