# Problem Domain
You are given a singly linked list `head` and an integer `n`. Write a function to remove the nth node from the end of the linked list and return the modified list.

- **Input**: A singly linked list `head` and an integer `n`.
- **Output**: Return the modified linked list after removing the nth node from the end.

# Test Cases
- **Test Case 1**:
  - **Input**: `head = [1,2,3,4,5], n = 2`
  - **Output**: `[1,2,3,5]`
  
- **Test Case 2**:
  - **Input**: `head = [1], n = 1`
  - **Output**: `[]`
  
- **Test Case 3**:
  - **Input**: `head = [1,2], n = 1`
  - **Output**: `[1]`

# Visualization
![alt text](<Scan_20240627 (2).jpg>)

# Algorithm
1. Initialize two pointers `first` and `second` to a dummy node.
2. Move `second` pointer `n+1` steps ahead.
3. Move both `first` and `second` pointers until `second` reaches the end.
4. Adjust `first.next` to skip the `nth` node from the end.
5. Return the modified linked list.

# Big O
- **Time Complexity**: O(sz), where `sz` is the size of the linked list. We traverse the list twice (once for size calculation and once for removal).
- **Space Complexity**: O(1), as we use constant extra space aside from input.

# Step Through
Given `head = [1,2,3,4,5]` and `n = 2`:

- Initialize `dummy -> 1 -> 2 -> 3 -> 4 -> 5`
- Move `second` pointer to `4`
- Move `first` and `second` pointers until `second` reaches end
- Adjust `first.next` to skip `4`
- Return `[1,2,3,5]`
