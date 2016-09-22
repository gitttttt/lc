from List import h1

def reverseKGroup(head, k):
    length, index = 0, head
    if (head is None) or k == 1:
        return head
    while index is not None:
        length += 1
        index = index.next
    n = int(length / k)
    if n == 0:
        return head
    temp, index, p = [], head, head
    for i in range(n):
        p = index
        for j in range(k):
            temp.append(index.val)
            index = index.next
        temp.reverse()
        for j in range(k):
            p.val = temp[j]
            p = p.next
        temp = []
    return head

a = reverseKGroup(h1, 1)
while a is not None:
    print(a.val)
    a = a.next
