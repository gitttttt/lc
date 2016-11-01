# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root.left and not root.right:
            root.val = None
            return 'leaf'
        if root.val is data:
            if root.left and root.right:
                rightnode = root.right
                rightparent = rightnode
                while rightnode.left:
                    rightparent = rightnode
                    rightnode = rightnode.left
                root.val = rightnode.data
                if self.delNode(rightnode,rightnode.data) is 'leaf':
                    rightparent.left = None
                return 'node'
            else:
                direction = 0 if root.left else 1
                node = root[direction]
                root.val = node.data
                if self.delNode(node,node.data) is 'leaf':
                    root[direction] = None
                return 'node'
        else:
            parent = root
            direction = 0 if root.val > data else 1
            root = parent[direction]
            if self.delNode(root, data) is 'leaf':
                parent[direction] = None