class Node:
    """
    Node class represents a single element in the stack.
    """
    def __init__(self, value):
        """
        Initialize a new Node with the given value.

        Args:
            value: The value to store in the Node.
        """
        self.value = value
        self.next = None

class Stack:
    """
    Stack class represents a Last-In-First-Out (LIFO) data structure.
    """
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.head = None

    def push(self, value):
        """
        Push a new element onto the stack.

        Args:
            value: The value to push onto the stack.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The value of the top element, or None if the stack is empty.
        """
        if self.head is None:
            return None
        popped = self.head.value
        self.head = self.head.next
        return popped

    def delete_middle(self):
        """
        Delete the middle element from the stack.
        If the stack has an even number of elements, delete the second middle element.
        """
        if self.head is None or self.head.next is None:
            # If the stack is empty or has only one element, return
            return
        if self.head.next.next is None:
            # If the stack has exactly two elements, delete the first one
            self.head = self.head.next
            return
        slow_ptr = self.head
        fast_ptr = self.head
        prev_ptr = None
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if prev_ptr:
            prev_ptr.next = slow_ptr.next
        else:
            self.head = slow_ptr.next

    def to_list(self):
        """
        Convert the stack to a list.

        Returns:
            A list containing the elements of the stack.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Test the implementation
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("Input:", stack.to_list())
    stack.delete_middle()
    print("Output:", stack.to_list())
