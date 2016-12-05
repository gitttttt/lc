# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            tmp = RandomListNode(p.label)
            tmp.next = p.next
            p.next = tmp
            tmp.random = p.random.next
            p = tmp.next
        res = head.next
        p = res
        while p:
            p.next = p.next.next
            p = p.next
        return res

