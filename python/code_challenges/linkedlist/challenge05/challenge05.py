# Write here the code challenge solution
class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        return current

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def insert_after(before, new_node):
    if not before:
        raise ValueError("The given 'before' node cannot be None")
    new_node.next = before.next
    before.next = new_node
