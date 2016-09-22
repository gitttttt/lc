from List import ListNode, h1

def reverseBetween(head, m, n):
    # if head is None:
    #     return None
    # if m == n:
    #     return head
    # l, i, j, index, mid, right = [], m, n-m, head, [], []
    # while i > 1:
    #     l.append(index.val)
    #     i -= 1
    #     index = index.next
    # for i in range(j):
    #     mid.append(index.val)
    #     index = index.next
    # while index is not None:
    #     right.append(index.val)
    #     index = index.next
    # mid.reverse()
    # print(right)
    # l.extend(mid)
    # l.extend(right)
    # res = ListNode(l[0])
    # result = res
    # for i in l[1:]:
    #     res.next = ListNode(i)
    #     res = res.next
    # return result
    left, mid, right = [], [], []
    index = head
    for i in range(1, m):
        left.append(index.val)
        index = index.next
    for i in range(m, n+1):
        mid.append(index.val)
        index = index.next
    while index is not None:
        right.append(index.val)
        index = index.next
    l = []
    l.extend(left)
    mid.reverse()
    l.extend(mid)
    l.extend(right)
    result = ListNode(l[0])
    r = result
    ll = l[1:]
    for i, v in enumerate(ll):
        result.next = ListNode(l[i+1])
        result = result.next
    return r

a = reverseBetween(h1, 1, 5)
# a = reverseBetween(h1, 1,4)
while a is not None:
    print('a', a.val)
    a = a.next