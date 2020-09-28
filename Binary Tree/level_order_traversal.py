class Node:

    def __init__(self, data):
        self.left = None

        self.right = None

        self.val = data


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []

    res = []
    nodes = [root]
    while nodes:
        res.append([node.val for node in nodes])
        next_nodes = []
        for node in nodes:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        nodes = next_nodes

    return res


queue = list()

root = Node(1)

queue.append(root)

root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)

res = levelOrder(root)
print(res)

# 1 2 3 4 5
