# Write here the code challenge solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    """
    Deletes a node from a singly linked list given only access to that node.

    Args:
        node (ListNode): The node to be deleted. It is guaranteed to be a valid node and not the tail node.

    Returns:
        None

    """
    node.val = node.next.val
    node.next = node.next.next
