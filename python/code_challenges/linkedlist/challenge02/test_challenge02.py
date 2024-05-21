import unittest
from challenge02 import ListNode, middleNode

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_array(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array

class TestMiddleNode(unittest.TestCase):
    def test_odd_length_list(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        middle = middleNode(head)
        result = linked_list_to_array(middle)
        self.assertEqual(result, [3, 4, 5])

    def test_even_length_list(self):
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        middle = middleNode(head)
        result = linked_list_to_array(middle)
        self.assertEqual(result, [4, 5, 6])

    def test_single_element_list(self):
        head = create_linked_list([1])
        middle = middleNode(head)
        result = linked_list_to_array(middle)
        self.assertEqual(result, [1])

    def test_two_element_list(self):
        head = create_linked_list([1, 2])
        middle = middleNode(head)
        result = linked_list_to_array(middle)
        self.assertEqual(result, [2])

if __name__ == '__main__':
    unittest.main()

