# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = {root: None}
        queue = [root]
        while queue:
            tmp = queue.pop(0)
            if tmp.left:
                queue.append(tmp.left)
                ancestor[tmp.left] = tmp
            if tmp.right:
                queue.append(tmp.right)
                ancestor[tmp.right] = tmp
        lset = set(p)
        index = p
        while index:
            lset.add(ancestor[index])
            index = ancestor[index]
        index = q
        while index not in lset:
            index = ancestor[index]
        return index
