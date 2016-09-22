from data import ListNode, h1, h2

def merge_sort_arr(arr1, arr2):
    i1, i2, res = 0, 0, []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        else:
            res.append(arr2[i2])
            i2 += 1
    while i1 < len(arr1):
        res.append(arr1[i1])
        i1 += 1
    while i2 < len(arr2):
        res.append(arr2[i2])
        i2 += 1
    return res

def merge_sort_arr_inplace(arr1, l, arr2):
    pass

def merge_sort_list(list1, list2):
    if not list1 and not list2:
        return None
    head = ListNode(0)
    index = head
    while list1 and list2:
        if list1.val < list2.val:
            index.next = ListNode(list1.val)
            list1 = list1.next
        else:
            index.next = ListNode(list2.val)
            list2 = list2.next
        index = index.next
    if list1:
        index.next = list1
    if list2:
        index.next = list2
    return head.next

def merge_sort_list_inplace(list1, list2):
    if not list1 and not list2:
        return None
    head = ListNode(0)
    index = head
    while list1 and list2:
        if list1.val < list2.val:
            index.next = list1
            list1 = list1.next
        else:
            index.next = list2
            list2 = list2.next
        index = index.next
    if list1:
        index.next = list1
    if list2:
        index.next = list2
    return head.next

