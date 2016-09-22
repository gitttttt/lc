from List import ListNode, h1


def rotateRight(head, k):
    if (head is None) or (head.next is None):
        return head
    if k == 0:
        return head
    index = head
    pre = None
    while k > 0:
        pre = index
        index = index.next
        k -= 1
        if (index is None) and k>0:
            return None
    start = index
    pre.next = None
    if start is None:
        return head
    while index.next is not None:
        index = index.next
    index.next = head
    return start

r1 = rotateRight(h1, 6)
while r1 is not None:
    print(r1.val)
    r1 = r1.next

def len(l):
    length = 0
    while l is not None:
        length += 1
        l = l.next
    return length

print(len(ListNode(0)))

