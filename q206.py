from List import h1

def reverseList(head):

    # if head is None or head.next is None:
    #     return head
    # rest = reverseList(head.next)
    # res = rest
    # while rest.next is not None:
    #     rest = rest.next
    # rest.next = head
    # head.next = None
    # return res
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        index = head
        index = index.next
        index.next = head
        head.next = None
        return index
    pre, index, after = head, head.next, head.next.next
    while after.next is not None:
        index.next = pre
        pre = index
        index = after
        after = after.next
    head.next = None
    index.next = pre
    after.next = index
    return after

a = reverseList(h1)
while a is not None:
    print(a.val)
    a = a.next
