def isBalanced(root):
    if root is None:
        return True
    else:
        return abs(depth(root.left) - depth(root.right)) <= 1


def depth(p):
    if p is None:
        return 0
    else:
        return 1 + max(depth(p.left), depth(p.right))
