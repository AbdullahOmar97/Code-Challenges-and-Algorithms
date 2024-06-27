class ListNode:
    """
    Definition for a singly linked list node.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode with a value and optional next node.

        Args:
            val (int): Value to be stored in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next ListNode. Defaults to None.
        """
        self.val = val
        self.next = next

def reverseLinkedList(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list in-place.

    Args:
        head (ListNode): Head of the linked list to be reversed.

    Returns:
        ListNode: Head of the reversed linked list.
    """
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to current
        current = next_node  # Move to the next node
    
    return prev  # prev will be the new head

def createLinkedList(arr):
    """
    Create a singly linked list from a list of values.

    Args:
        arr (list): List of values to be stored in the linked list nodes.

    Returns:
        ListNode: Head of the created linked list.
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(head):
    """
    Print values of a singly linked list.

    Args:
        head (ListNode): Head of the linked list to be printed.

    Returns:
        list: List of values in the linked list.
    """
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
