import unittest
from challenge03 import removeNthFromEnd, ListNode

class TestRemoveNthFromEnd(unittest.TestCase):
    def test_remove_nth_from_end(self):
        # Example 1
        # Input: head = [1,2,3,4,5], n = 2
        # Output: [1,2,3,5]
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        n = 2
        result = removeNthFromEnd(head, n)

        expected_output = [1, 2, 3, 5]
        self.assertEqual(self.get_linked_list_values(result), expected_output)

        # Example 2
        # Input: head = [1], n = 1
        # Output: []
        head = ListNode(1)
        n = 1
        result = removeNthFromEnd(head, n)
        self.assertIsNone(result)

        # Example 3
        # Input: head = [1,2], n = 1
        # Output: [1]
        head = ListNode(1)
        head.next = ListNode(2)
        n = 1
        result = removeNthFromEnd(head, n)
        expected_output = [1]
        self.assertEqual(self.get_linked_list_values(result), expected_output)

    def get_linked_list_values(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

if __name__ == "__main__":
    unittest.main()
