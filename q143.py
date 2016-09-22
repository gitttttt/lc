from List import ListNode, head1
#
#
# def reorderList(head):
#     # if head is None or head.next is None:
#     #     return head
#     # length = 0
#     # index = head
#     # while index is not None:
#     #     index = index.next
#     #     length += 1
#     # left, right, index = [], [], head
#     # left_length = int((length+1) / 2)
#     # for i in range(left_length):
#     #     left.append(index.val)
#     #     index = index.next
#     # while index is not None:
#     #     right.append(index.val)
#     #     index = index.next
#     # right.reverse()
#     # res = ListNode(0)
#     # index = res
#     # i = 0
#     # while length > 1:
#     #     index.next = ListNode(left[i])
#     #     index = index.next
#     #     index.next = ListNode(right[i])
#     #     index = index.next
#     #     length -= 2
#     #     i += 1
#     # if length == 1:
#     #     index.next = ListNode(left[i])
#     # return res.next
#     slow, fast = head, head
#     while fast.next is not None and fast.next.next is not None:
#         slow = slow.next
#         fast = fast.next.next
#     i = slow
#     slow = slow.next
#     i.next = None
#     slow = reverseList(slow)
#
#     p1=head                                             # rejoin 2 parts together
#     p2=slow
#     while p2:
#         t1=p1.next
#         p1.next=p2
#         t2=p2.next
#         p2.next=t1
#         p1=t1
#         p2=t2
#
# def reverseList(head):
#
#     # if head is None or head.next is None:
#     #     return head
#     # rest = reverseList(head.next)
#     # res = rest
#     # while rest.next is not None:
#     #     rest = rest.next
#     # rest.next = head
#     # head.next = None
#     # return res
#     if head is None or head.next is None:
#         return head
#     if head.next.next is None:
#         index = head
#         index = index.next
#         index.next = head
#         head.next = None
#         return index
#     pre, index, after = head, head.next, head.next.next
#     while after.next is not None:
#         index.next = pre
#         pre = index
#         index = after
#         after = after.next
#     head.next = None
#     index.next = pre
#     after.next = index
#     return after
#
#
# reorderList(h1)
# while h1 is not None:
#     print(h1.val)
#     h1 = h1.next
#
#
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: void Do not return anything, modify head in-place instead.
#         """
#         if head is None or head.next is None or head.next.next is None:
#             head=head
#         else:
#
#             slow=fast=head                                      # two parts
#             while fast.next and fast.next.next:
#                 slow=slow.next
#                 fast=fast.next.next
#
#             head2=slow.next
#             slow.next=None
#
#             dummy=ListNode(0)                                   # reverse 2nd part
#             dummy.next=head2
#             p=head2.next
#             head2.next=None
#             while p:
#                 tmp=p
#                 p=p.next
#                 tmp.next=dummy.next
#                 dummy.next=tmp
#             head2=dummy.next
#
#             p1=head                                             # rejoin 2 parts together
#             p2=head2
#             while p2:
#                 t1=p1.next
#                 p1.next=p2
#                 t2=p2.next
#                 p2.next=t1
#                 p1=t1
#                 p2=t2

# Definition for singly-linked list.


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        else:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            h1 = slow.next
            slow.next = None
            pre = None
            now = h1
            while now:
                nx = now.next
                now.next = pre
                pre = now
                now = nx
            h1 = pre
            h2 = head
            # h2.prt()
            # print
            # h1.prt()
            nx2 = None
            nx1 = None
            while h1:
                nx2 = h2.next
                h2.next = h1
                nx1 = h1.next
                h1.next = nx2
                h2 = nx2
                h1 = nx1


Solution().reorderList(head1)
head1.prt()



