import time
from List import head1, ListNode

# Definition for singly-linked list.

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        index = head
        while index.next != slow:
            index = index.next
        index.next = None
        right = slow
        left = self.sortList(left)
        right = self.sortList(right)
        return self.help(left, right)

    def help(self, left, right):
        head = None
        left.prt()
        right.prt()
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        if right:
            head.next = right
        head.prt()
        return head

l1 = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(4)
Solution().help(l1, l2).prt()

