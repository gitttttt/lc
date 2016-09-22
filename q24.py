from List import h1

def swapPairs(head):
    if (head is None) or (head.next is None):
        return head
    pre, index = head, head
    index = index.next
    temp = 0
    while (index is not None) and (index.next is not None):
        temp = index.val
        index.val = pre.val
        pre.val = temp
        pre = index.next
        index = index.next.next
    if index is None:
        return head
    else:
        temp = index.val
        index.val = pre.val
        pre.val = temp
        return head

a = swapPairs(h1)
while a is not None:
    print(a.val)
    a = a.next
