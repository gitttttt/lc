# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        up = root
        down = up.left
        while down:
            pos = up
            while pos:
                pos.left.next = pos.right
                if pos.next:
                    pos.right.next = pos.next.left
                pos = pos.next
            up = up.left
            down = down.left
