# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.part(root)

    def part(self, root):
        if not root:
            return None
        left = self.part(root.left)
        right = self.part(root.right)
        if left:
            r = root.right
            root.left = None
            root.right = root.left
            left = r
        if right:
            return right
        if left:
            return left
        return root
