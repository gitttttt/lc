# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return
        up = root
        down = root.left if root.left else root.right
        while up:
            u = up
            d = down

