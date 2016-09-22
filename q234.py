# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data import h1, h2
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print fast.val, slow.val
        tmp = slow.next if fast else slow
        tmp = self.reverse(tmp)
        tmp.prt()
        print
        head.prt()
        while tmp:
            if tmp.val != head.val:
                return False
            head = head.next
            tmp = tmp.next
        return True

    def reverse(self, head):
        pre = None
        now = head
        while now:
            next = now.next
            now.next = pre
            pre = now
            now = next
        return pre

print Solution().isPalindrome(h1)


