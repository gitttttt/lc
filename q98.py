import sys
def isValidBST(root):
    return yes(root, sys.maxsize, -sys.maxsize)

def yes(node, max_value, min_value):
    if node is None:
        return True
    elif node.val < min_value or node.val > max_value:
        return False
    else:
        return yes(node.left, node.val, min_value) and yes(node.right, max_value, node.val)