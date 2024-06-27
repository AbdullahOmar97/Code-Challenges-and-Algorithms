class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, value=0, next_node=None):
        """
        Initializes a new instance of Node.

        Args:
            value: The value to be stored in the node.
            next_node: Reference to the next node in the linked list.
        """
        self.value = value
        self.next = next_node


class LinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty linked list with a head node."""
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be appended to the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, value):
        """
        Searches for a node with the given value in the linked list.

        Args:
            value: The value to search for.

        Returns:
            The node containing the value if found, otherwise None.
        """
        current = self.head
        while current and current.value != value:
            current = current.next
        return current

    def to_list(self):
        """
        Converts the linked list into a Python list.

        Returns:
            A Python list representation of the linked list values.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


def insert_after(before, new_node):
    """
    Inserts a new node after a specified node in the linked list.

    Args:
        before: The node after which the new_node should be inserted.
        new_node: The new node to be inserted.

    Raises:
        ValueError: If the 'before' node is None.
    """
    if not before:
        raise ValueError("The given 'before' node cannot be None")
    new_node.next = before.next
    before.next = new_node
