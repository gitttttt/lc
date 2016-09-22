from Tree import p, prt_tree

def invertTree(root):
    if not root:
        return None
    else:
        right, left = invertTree(root.left), invertTree(root.right)
        root.right, root.left = right, left
        return root

a = invertTree(p)
prt_tree(a)