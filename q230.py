# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        now = None
        while root:
            stack.append(root)
            root = root.left
        while stack and k > 0:
            now = stack.pop()
            right = now.right
            while right:
                stack.append(right)
                right = right.left
            k -= 1
        return now
