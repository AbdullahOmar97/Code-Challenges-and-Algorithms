# challenge04.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to current
        current = next_node  # Move to the next node
    
    return prev  # prev will be the new head

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
