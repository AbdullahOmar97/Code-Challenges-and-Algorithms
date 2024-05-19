
import pytest
from challenge01 import ListNode, delete_node

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Test cases
def test_delete_node():

    head1 = list_to_linked_list([4, 5, 1, 9])
    node_to_delete1 = head1.next
    print("Original Linked List:")
    print_linked_list(head1)
    delete_node(node_to_delete1)
    print("Linked List after deletion:")
    print_linked_list(head1)
    assert linked_list_to_list(head1) == [4, 1, 9]

    head2 = list_to_linked_list([4, 5, 1, 9])
    node_to_delete2 = head2.next.next
    print("\nOriginal Linked List:")
    print_linked_list(head2)
    delete_node(node_to_delete2)
    print("Linked List after deletion:")
    print_linked_list(head2)
    assert linked_list_to_list(head2) == [4, 5, 9]