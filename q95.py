# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.get(range(1, n+1))

    def get(self, arr):
        if not arr:
            return []
        res = []
        for i in arr:
            small = self.get(filter(lambda x: x < i, arr))
            big = self.get(filter(lambda x: x > i, arr))
            if not big and not small:
                return [TreeNode(i)]
            if not small:
                for b in big:
                    root = TreeNode(b)
                    root.right = b
                    res.append(root)
            if not big:
                for s in small:
                    root = TreeNode(s)
                    root.left = s
                    res.append(root)
            for s in small:
                for b in big:
                    root = TreeNode(i)
                    root.left = s
                    root.right = b
                    res.append(root)
        return res

for i in Solution().generateTrees(3):
    print type(i)
