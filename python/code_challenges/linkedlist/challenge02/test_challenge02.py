import unittest
from challenge02 import ListNode, find_middle_node

class TestFindMiddleNode(unittest.TestCase):
    
    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    
    def test_single_middle(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        middle_node = find_middle_node(head)
        self.assertEqual(middle_node.val, 3)
        print(f"Test Case 1: Middle Node Value is {middle_node.val}")
    
    def test_two_middle(self):
        head = self.create_linked_list([1, 2, 3, 4, 5, 6])
        middle_node = find_middle_node(head)
        self.assertEqual(middle_node.val, 4)
        print(f"Test Case 2: Middle Node Value is {middle_node.val}")
    
if __name__ == "__main__":
    unittest.main()
