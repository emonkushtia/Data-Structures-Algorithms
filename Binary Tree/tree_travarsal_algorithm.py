# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do in-order tree traversal
def print_in_order(node):
    if node:
        # First recur on left child
        print_in_order(node.left)

        # then print the data of node
        print(node.val),

        # now recur on right child
        print_in_order(node.right)


# A function to do post-order tree traversal
def print_post_order(node):
    if node:
        # First recur on left child
        print_post_order(node.left)

        # the recur on right child
        print_post_order(node.right)

        # now print the data of node
        print(node.val),


# A function to do pre-order tree traversal
def print_pre_order(node):
    if node:
        # First print the data of node
        print(node.val),

        # Then recur on left child
        print_pre_order(node.left)

        # Finally recur on right child
        print_pre_order(node.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
print_pre_order(root)

print("\nInorder traversal of binary tree is")
print_in_order(root)

print("\nPostorder traversal of binary tree is")
print_post_order(root)
