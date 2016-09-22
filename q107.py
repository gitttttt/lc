# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [[]]
        queue = []
        res = []
        queue.append(root)
        while queue:
            tmp = []
            nextq = []
            for i in queue:
                tmp.append(i.val)
                if i.left:
                    nextq.append(i.left)
                if i.right:
                    nextq.append(i.right)
            queue = nextq
            res.append(tmp)
        return res[::-1]