class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def remove(self, key):
        temp = self.head
        if temp.data == key:
            self.head = temp.next
            return

        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                break
            temp = temp.next

    def remove_at(self, position):
        temp = self.head
        local_position = 0
        if local_position == position:
            self.head = temp.next
            return

        while temp.next:
            local_position += 1
            if local_position == position:
                temp.next = temp.next.next
                break
            temp = temp.next

    def find_length(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def find_length_recursively(self, node):
        if node is None:
            return 0

        if node.next:
            return 1 + self.find_length_recursively(node.next)
        else:
            return 1

    @staticmethod
    def print_nodes(node):
        while node.next:
            print(node.data, end=' ')
            node = node.next
        print(node.data, end=' ')


def main():
    linked_list = LinkedList()
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    forth_node = Node(4)
    fifth_node = Node(5)
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = forth_node
    forth_node.next = fifth_node
    linked_list.head = first_node

    linked_list.insert(12)
    linked_list.push(10)

    linked_list.remove_at(4)
    linked_list.print_nodes(linked_list.head)
    print('Length of Linked List: ', linked_list.find_length())
    print('Length of Linked List by Recursive method: ', linked_list.find_length_recursively(linked_list.head))


main()