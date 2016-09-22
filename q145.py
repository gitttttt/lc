# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.part(root, res)
        return res

    def part(self, node, res):
        if not node:
            return res
        self.part(node.left, res)
        self.part(node.right, res)
        res.append(node.val)