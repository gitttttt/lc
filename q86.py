from List import ListNode, h1

def partition(head, x):
    if head is None:
        return None
    index, less, more = head, ListNode(0), ListNode(0)
    less_start, more_start = less, more
    while index is not None:
        if index.val < x:
            less.next = ListNode(index.val)
            less = less.next
        else:
            more.next = ListNode(index.val)
            more = more.next
        index = index.next
    less.next = more_start.next
    return less_start.next

a = partition(h1, 3)
while a is not None:
    print(a.val)
    a = a.next