import unittest
from challenge03 import Stack

class TestDeleteMiddle(unittest.TestCase):
    def test_delete_middle_even(self):
        """
        Test deleting the middle element from a stack with an even number of elements.
        """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.to_list(), [4, 3, 2, 1])
        stack.delete_middle()
        self.assertEqual(stack.to_list(), [4, 3, 1])

    def test_delete_middle_odd(self):
        """
        Test deleting the middle element from a stack with an odd number of elements.
        """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.to_list(), [5, 4, 3, 2, 1])
        stack.delete_middle()
        self.assertEqual(stack.to_list(), [5, 4, 2, 1])

    def test_delete_middle_empty(self):
        """
        Test deleting the middle element from an empty stack.
        """
        stack = Stack()
        self.assertEqual(stack.to_list(), [])
        stack.delete_middle()
        self.assertEqual(stack.to_list(), [])

    def test_delete_middle_single(self):
        """
        Test deleting the middle element from a stack with only one element.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.to_list(), [1])
        stack.delete_middle()
        self.assertEqual(stack.to_list(), [1])  # Corrected assertion

if __name__ == '__main__':
    unittest.main()
