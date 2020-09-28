class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, traversal_type):
        if traversal_type == 'in_order':
            print(self._in_order_print(self.root, ''))
        if traversal_type == 'pre_order':
            print(self._pre_order_print(self.root, ''))
        if traversal_type == 'post_order':
            print(self._post_order_print(self.root, ''))

    def _post_order_print(self, node, traversal_msg):
        if node:
            traversal_msg = self._post_order_print(node.left, traversal_msg)
            traversal_msg = self._post_order_print(node.right, traversal_msg)
            traversal_msg += (str(node.data) + ' > ')
        return traversal_msg

    def _pre_order_print(self, node, traversal_msg):
        if node:
            traversal_msg += (str(node.data) + ' > ')
            traversal_msg = self._pre_order_print(node.left, traversal_msg)
            traversal_msg = self._pre_order_print(node.right, traversal_msg)
        return traversal_msg

    def _in_order_print(self, node, traversal_msg):
        if node:
            traversal_msg = self._in_order_print(node.left, traversal_msg)
            traversal_msg += (str(node.data) + ' > ')
            traversal_msg = self._in_order_print(node.right, traversal_msg)
        return traversal_msg


#                   1
#                /      \
#               2         5
#            /   \       /  \
#           3     4     6    7
#
# in_order = 3 > 2 > 4 > 1 > 6 > 5 > 7
# pre_order = 1 > 2 > 3 > 4 > 5 > 6 > 7
# post_order = 3 > 4 > 2 > 6 > 7 > 5 > 1
# level_order = 1 > 2 > 5 > 3 > 4 > 6 > 7

def main():
    tree = BinaryTree()
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree.root = root
    tree.print_tree('in_order')
    tree.print_tree('pre_order')
    tree.print_tree('post_order')


main()
