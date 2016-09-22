from Tree import p
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
        if not root:
            return '#'
        else:
            return str(root.val) + ',' + self.serialize(root.left) + ','\
                   + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        origin = data.split(",")
        return self.help(origin)

    def help(self, arr):
        node = arr.pop(0)
        if node == '#':
            return None
        else:
            root = TreeNode(node)
            root.left = self.help(arr)
            root.right = self.help(arr)
            return root



print Codec().serialize(p)