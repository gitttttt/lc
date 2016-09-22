from List import ListNode, h1

def deleteDuplicates(head):
    if head is None:
        return None
    index = head
    nums = {}
    while index is not None:
        if index.val in nums:
            nums[index.val] += 1
        else:
            nums[index.val] = 1
        index = index.next
    print(nums)
    num_copy = nums.copy()
    for k in num_copy.keys():
        if num_copy[k] > 1:
            del nums[k]
    keys = list(nums.keys())
    keys = sorted(keys)
    print(keys)
    if len(keys)==0:
        return None
    else:
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
print({} is None)