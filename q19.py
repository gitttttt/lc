from List import ListNode


def removeNthFromEnd(head, n):
    length = 1
    index = head
    while index.next is not None:
        index = index.next
        length += 1
    if length == 1:
        return None
    else:
        index = head
        nst = length + 1 - n
        if nst == 1:
            return head.next
        elif nst == 2:
            head.next = head.next.next
            return head
        while nst - 1 > 1:
            index = index.next
            nst -= 1
        if index.next.next is None:
            index.next = None
        else:
            pre, index, after = index, index.next, index.next.next
            pre.next = after
        return head

lis = ListNode(1)
head = lis
lis.next = ListNode(2)
lis = lis.next
lis.next = ListNode(3)

af = removeNthFromEnd(head, 3)
while af is not None:
    print(af.val)
    af = af.next


