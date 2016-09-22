def reverse(self, head):
    pre = None
    now = head
    while now:
        next = now.next
        now.next = pre
        pre = now
        now = next
    return pre
