class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if not head or n < 1:
        return None
    
    # Constraint: The number of nodes in the list is sz.
    sz = 0
    current = head
    while current:
        sz += 1
        current = current.next
    
    if n > sz:
        return None
    
    # Constraint: 1 <= sz <= 30
    if sz == 1:
        return None
    
    # Constraint: 1 <= n <= sz
    if n == sz:
        return head.next
    
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move second pointer to the n+1th node from the beginning
    for i in range(n + 1):
        second = second.next
    
    # Move both pointers until the second pointer reaches the end
    while second is not None:
        first = first.next
        second = second.next
    
    # Remove the nth node
    first.next = first.next.next
    
    return dummy.next
