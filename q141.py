def hasCycle(head):
    if head is None:
        return False
    i1, i2 = head, head.next
    while (i1 is not None) and (i2 is not None):
        i1 = i1.next
        i2 = i2.next
        if i2 is None:
            return False
        else:
            i2 = i2.next
            if i1 == i2:
                return True
    return False
