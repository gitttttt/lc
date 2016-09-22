# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []
        if root:
            self.queue.append(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue is not []


    def next(self):
        """
        :rtype: int
        """
        if self.queue:
            first = self.queue.pop(0)
            if first.left:
                self.queue.append(first.left)
            if first.right:
                self.queue.append(first.right)
            return first.val


