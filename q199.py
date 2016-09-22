# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        nodes = []
        res = []
        nodes.append(root)
        while nodes:
            tmp = []
            for i in nodes:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            res.append(nodes[-1].val)
            nodes = tmp
        return res