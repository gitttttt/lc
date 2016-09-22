from Tree import p

def pathSum(root, sum):
    tmp = hi(root)
    pass


def hi(root):
    if root is None:
        return [[]]
    else:
        if root.left is None and root.right is None:
            return [[root.val]]
        else:
            if root.right is None:
                left = hi(root.left)
                for i in left:
                    i.insert(0, root.val)
                return left
            elif root.left is None:
                right = hi(root.right)
                for i in right:
                    i.insert(0, root.val)
                return right
            else:
                left = hi(root.left)
                right = hi(root.right)
                print('1', right)
                for i in right:
                    print('2', i)
                    i.insert(0,  root.val)
                    print('3', i)
                for i in left:
                    i.insert(0,  root.val)
                return left + right

print(hi(p))