
def maxDepth(root):
    return depth(root)


def depth(p):
    if p is None:
        return 0
    else:
        return 1 + max(depth(p.left), depth(p.right))