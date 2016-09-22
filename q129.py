# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return sum(map(lambda x: int(x), self.get_num(root)))

    def get_num(self, head):
        if not head:
            return []
        if not head.left and not head.right:
            return [str(head.val)]
        left = self.get_num(head.left)
        right = self.get_num(head.right)
        return [str(head.val)+x for x in left] + [str(head.val)+x for x in right]

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)

print Solution().sumNumbers(root)