class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def prt(self):
        this = self
        while this:
            print this.val, "->",
            this = this.next
        print


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def prt(self):
        root = self
        if not root:
            return
        queue = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

p = t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
# t1.left.left = TreeNode(3)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(5)
# t1.left.right = TreeNode(2)
q = t2 = TreeNode(0)
t2.left = TreeNode(1)
t2.right = TreeNode(2)

l1 = ListNode(1)
h1 = l1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(1)
l1 = l1.next


l2 = ListNode(1)
h2 = l2
l2.next = ListNode(3)
l2 = l2.next
l2.next = ListNode(5)
l2 = l2.next
l2.next = ListNode(7)
l2 = l2.next
l2.next = ListNode(12)
l2 = l2.next
