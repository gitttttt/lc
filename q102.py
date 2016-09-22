import time

from Tree import p


def levelOrder(root):
    if root is None:
        return []
    else:
        res, node_list = [], [root]
        while len(node_list) > 0:
            time.sleep(1)
            tmp_node, tmp = [], []
            for i in node_list:
                if i.left is not None:
                    tmp_node.append(i.left)
                if i.right is not None:
                    tmp_node.append(i.right)
                tmp.append(i.val)

            res.append(tmp)
            print(res)
            node_list = tmp_node
            for i in node_list:
                print(i.val)
        return res

levelOrder(p)
