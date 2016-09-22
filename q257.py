# from tree.Tree import p
#
# def binaryTreePaths(root):
#     res = []
#     if not root:
#         return res
#     else:
#         a(root, "", res)
#         return res
#
# def a(node, path, res):
#     if not node.left and node.right:
#         res.append(path + node.val)
#     else:
#         a(node.left, path + "->", res)
#         a(node.right, path + "->", res)

a = {1: 2, 3: 4, 5: 6}
print(type(a))
for i in a:
    print(i)
