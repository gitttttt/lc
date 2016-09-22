class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        l, size = head, 0
        while l:
            l = l.next
            size += 1
        return self.part(head, size)

    def part(self, head, size):
        if not head:
            return
        