from Tree import p

def hasPathSum(root, sum):
    if root is None:
        return False
    else:
        if root.left is None and root.right is None:
            return root.val == sum
        else:
            return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)

print(hasPathSum(p, 2))