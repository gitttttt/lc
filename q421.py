class Node:
    def __init__(self):
        self.arr = [None, None]

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = map(lambda x: str(bin(x))[::-1], nums)
        root = Node()
        for n in nums:
            node = root
            for i in n:
                if not node.arr[int(i)]:
                    node.arr[int(i)] = Node()
                node = node.arr[int(i)]
        return self.help(root, 0)

    def help(self, node, n):
        if not node:
            return 0
        if node.arr[0] and node.arr[1]:
            return max(self.help(node.arr[0], n+1), self.help(node.arr[1], n+1)) + 2 ** n
        if node.arr[0]:
            return self.help(node.arr[0], n+1)
        if node.arr[1]:
            return self.help(node.arr[1], n+1)
        return 2 ** n


