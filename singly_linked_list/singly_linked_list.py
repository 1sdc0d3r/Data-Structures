class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = self.head.next
            current.next = new_node

    def contains(self, value):
        if self.head.value == value:
            return self.head.value
        else:
            current = self.head
            while current.next is not None:
                if current.value == value:
                    return current.value
                else:
                    current = current.next

    def remove_head(self):
        self.head = self.head.next

    def get_max(self):
        current_max = self.head.value
        current = self.head
        while current.next is not None:
            if current.value > current_max:
                current_max = current.value
            else:
                current = current.next
        return current_max
