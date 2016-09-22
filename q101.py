from Tree import p


def isSymmetric(root):
    if not root:
        return True
    return equal(root.left, root.right)

def equal(l, r):
    if not l and not r:
        return True
    if not l or not r:
        return False
    if l.val == r.val:
        return equal(l.left, r.right) and equal(l.right, r.left)
    else:
        return False

print(isSymmetric(p))
