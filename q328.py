# Definition for singly-linked list.
from List import ListNode, head1

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1 = head
        h2 = head.next
        head2 = h2
        while h2 and h2.next:
            h1.next = h2.next
            h1 = h1.next
            if h1:
                h2.next = h1.next
                h2 = h2.next
        print 'aaa'
        h1.next = head2

head1.prt()
Solution().oddEvenList(head1)
head1.prt()
