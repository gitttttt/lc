from List import ListNode
def addTwoNumbers(l1, l2):
    temp, add, res = 0, 0, ListNode(0)
    ret = res
    pre = None
    while (l1 is not None) & (l2 is not None):
        temp = l1.val + l2.val + add
        l1, l2 = l1.next, l2.next
        add = int(temp / 10)
        res.val = temp % 10
        res.next = ListNode(0)
        pre = res
        res = res.next
    if l1 is not None:
        while l1 is not None:
            temp = l1.val + add
            l1 = l1.next
            add = int(temp / 10)
            res.val = temp % 10
            res.next = ListNode(0)
            pre = res
            res = res.next
    if l2 is not None:
        while l2 is not None:
            temp = l2.val + add
            l2 = l2.next
            add = int(temp / 10)
            res.val = temp % 10
            res.next = ListNode(0)
            pre = res
            res = res.next
    res.val = add
    if add == 0:
        res = pre
    res.next = None
    return ret
