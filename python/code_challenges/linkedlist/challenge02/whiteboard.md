# Find Middle Node - Challenge 02

## 1. Problem Domain
Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

## 2. Test Cases
### Input and Output
- **Input**: A singly linked list.
- **Output**: The middle node of the linked list.

### Test Case 1: Odd Length List
- **Input**: `[1, 2, 3, 4, 5]`
- **Expected Output**: `[3, 4, 5]`

### Test Case 2: Even Length List
- **Input**: `[1, 2, 3, 4, 5, 6]`
- **Expected Output**: `[4, 5, 6]`

### Test Case 3: Single Element List
- **Input**: `[1]`
- **Expected Output**: `[1]`

### Test Case 4: Two Element List
- **Input**: `[1, 2]`
- **Expected Output**: `[2]`

## 3. Visualization
![Visualization](<لقطة شاشة 2024-05-19 191848.png>)

## Solution
To solve the problem of finding the middle node in a singly linked list, we can use the two-pointer technique. Specifically, we use a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

## 4. Algorithm
1. Initialize two pointers, `slow` and `fast`, both pointing to the head of the list.
2. Traverse the list with the `slow` pointer moving one step and the `fast` pointer moving two steps at a time.
3. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle node.
4. Return the node at the `slow` pointer.

### Code Implementation
#### challenge02.py

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
```

## Test Cases
We wrote the tests to verify the functionality of our middleNode function. The tests cover cases with an odd number of nodes, an even number of nodes, a single node, and two nodes.

## 5. Big O
- **Time Complexity:** O(n) - where n is the number of nodes in the list. We traverse the list with the fast pointer which ensures we cover all nodes.
- **Space Complexity:** O(1) - only a constant amount of extra space is used for the pointers.

## 6. Step Through

### Example: `[1, 2, 3, 4, 5]`
**Initialization:**
- `slow` at 1
- `fast` at 1

**First Iteration:**
- `slow` moves to 2
- `fast` moves to 3

**Second Iteration:**
- `slow` moves to 3
- `fast` moves to 5

**End of Loop:**
- `fast` can no longer move two steps, so `slow` is now at the middle node (3).

### Example: `[1, 2, 3, 4, 5, 6]`
**Initialization:**
- `slow` at 1
- `fast` at 1

**First Iteration:**
- `slow` moves to 2
- `fast` moves to 3

**Second Iteration:**
- `slow` moves to 3
- `fast` moves to 5

**Third Iteration:**
- `slow` moves to 4
- `fast` moves to the end of the list

**End of Loop:**
- `slow` is now at the second middle node (4).
