from List import ListNode, r1, h2

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    head = ListNode(0)
    if l1.val < l2.val:
        head.val = l1.val
        l1 = l1.next
    else:
        head.val = l2.val
        l2 = l2.next
    index = head
    while (l1 is not None) & (l2 is not None):
        if l1.val < l2.val:
            index.next = ListNode(l1.val)
            l1 = l1.next
        else:
            index.next = ListNode(l2.val)
            l2 = l2.next
        index = index.next
    if l1 is not None:
        while l1 is not None:
            index.next = ListNode(l1.val)
            l1 = l1.next
            index = index.next
    if l2 is not None:
        while l2 is not None:
            index.next = ListNode(l2.val)
            l2 = l2.next
            index = index.next
    return head

q21 = mergeTwoLists(r1, h2)
while q21 is not None:
    print(q21.val)
    q21 = q21.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        # none
        if len(lists) == 0:
            return None
        # only one list
        if len(lists) == 1:
            return lists[0]
        # merge sort each two linked list
        l1 = self.mergeKLists(lists[:len(lists)/2])
        l2 = self.mergeKLists(lists[len(lists)/2:])
        head = self.mergeTwoLists(l1,l2)
        return head

    # merge two sorted linked list
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p = ListNode(0)
        dummyhead = p
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1 is None:
            p.next = l2
        else:
            p.next = l1
        return dummyhead.next