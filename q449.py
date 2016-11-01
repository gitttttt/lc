# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        inOrder = []
        preOrder = []
        self.inOrder(root, inOrder)
        self.preOrder(root, preOrder)
        return 'a'.join(inOrder) + 'b' + 'a'.join(preOrder)

    def inOrder(self, root, res):
        if root:
            self.inOrder(root.left, res)
            res.append(root.val)
            self.inOrder(root.right, res)


    def preOrder(self, root, res):
        if root:
            res.append(root.val)
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        inorder = map(int, data.split('b')[0].split('a'))
        preorder = map(int, data.split('b')[1].split('a'))
        return self.buildTree(preorder, inorder)


    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))