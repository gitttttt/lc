# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        node = root
        while stack or node:
            if node:
                res.append(node.val)
                res.append(node)
                node = node.left
            else:
                up = stack.pop()
                node = up.right