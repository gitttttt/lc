# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [[]]
        right = True
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
            if right:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            queue = nextq
            right = ~right
        return res[::-1]