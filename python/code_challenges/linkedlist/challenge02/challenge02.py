# challenge02.py

class ListNode:
    """
    Definition for a singly linked list node.
    
    Attributes:
        val (int): Value stored in the node.
        next (ListNode): Pointer to the next node in the linked list.
    """
    def __init__(self, val=0, next=None):
        """
        Initializes a new instance of ListNode with the given value and next node reference.
        
        Args:
            val (int, optional): Value to store in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next node in the linked list. Defaults to None.
        """
        self.val = val
        self.next = next

def find_middle_node(head):
    """
    Given the head of a singly linked list, returns the middle node.
    If there are two middle nodes, returns the second middle node.

    Args:
        head (ListNode): Head node of the singly linked list.

    Returns:
        ListNode: The middle node of the linked list.

    Example:
        Input: head = [1,2,3,4,5]
        Output: ListNode with value 3

    Explanation:
        The middle node of the list is node 3.

        Input: head = [1,2,3,4,5,6]
        Output: ListNode with value 4

    Explanation:
        Since the list has two middle nodes with values 3 and 4, the function returns the second one.
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
