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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        # return False

    def remove_head(self):
        current_head = self.head
        if self.head == self.tail and self.head is not None:
            self.head = None
            self.tail = None
            return current_head.value
        elif self.head is not None:
            self.head = self.head.next
            return current_head.value

    def get_max(self):
        current = self.head
        if current is not None:
            current_max = current.value
            while current is not None:
                if current.value > current_max:
                    current_max = current.value
                else:
                    current = current.next
            return current_max
