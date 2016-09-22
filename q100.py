from Tree import p, q

def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) & isSameTree(p.right, q.right)
    return False

print(isSameTree(p, q))
