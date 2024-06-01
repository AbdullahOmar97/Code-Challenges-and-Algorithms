# Write here the code challenge solution
# challenge01.py

class MyQueue:
    """
    Class to implement a queue using two stacks.
    """

    def __init__(self):
        """
        Initialize data structure.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        
        :param x: Element to be pushed into the queue
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        
        :return: The element removed from the front of the queue
        """
        self._move_stack1_to_stack2_if_needed()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        
        :return: The element at the front of the queue
        """
        self._move_stack1_to_stack2_if_needed()
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        
        :return: True if the queue is empty, False otherwise
        """
        return not self.stack1 and not self.stack2

    def _move_stack1_to_stack2_if_needed(self) -> None:
        """
        Helper function to move elements from stack1 to stack2 if stack2 is empty.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
