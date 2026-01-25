import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail = None


def find_lowest_value(head):
    min_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value


def find_max_value(head):
    max_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data > max_value:
            max_value = current_node.data
        current_node = current_node.next
    return max_value


def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def insert_node(head, new_data, index):
    new_node = Node(new_data)

    if index == 0:
        new_node.next = head
        return new_node

    current = head
    previous_node = head
    count = 0

    while current and count < index - 1:
        previous_node = current
        current = current.next
        count += 1

    if not current:
        previous_node.next = new_node
        return head

    new_node.next = current.next
    current.next = new_node
    return head


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1 = insert_node(node1, 14, 3)
traverseAndPrint(node1)
# print(findLowestValue(node1))
# print(find_lowest_value(node1))
# print(find_max_value(node1))
# print(find_max_value(node3))
