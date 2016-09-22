from List import ListNode, h1

def deleteDuplicates(head):
    keys = set()
    index = head
    while index is not None:
        keys.add(index.val)
        index = index.next
    keys = sorted(list(keys))
    print(keys)
    head = ListNode(keys[0])
    index = head
    for i in keys[1:]:
        index.next = ListNode(i)
        index = index.next
    return head

a = deleteDuplicates(h1)
while a is not None:
    print(a.val)
    a = a.next
