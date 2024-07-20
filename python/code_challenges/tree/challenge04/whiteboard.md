#### whiteboard.md

## Problem Domain
- **Input**: A binary tree represented by its root node.
- **Output**: The maximum value found in the binary tree.

## Test Cases
- **Test Case 1**:
  - Input: [10]
  - Output: 10
- **Test Case 2**:
  - Input: [1, 2, None, 3]
  - Output: 3
- **Test Case 3**:
  - Input: [1, None, 2, None, 3]
  - Output: 3
- **Test Case 4**:
  - Input: [2, 1, 3]
  - Output: 3
- **Test Case 5**:
  - Input: [1000, 500, 2000, 250, 600, 12000]
  - Output: 12000
- **Test Case 6**:
  - Input: [-1, -2, -3]
  - Output: -1
- **Test Case 7**:
  - Input: [0, -1, 1, -3, -2, 2, 3]
  - Output: 3

## Visualization
For the tree [1000, 500, 2000, 250, 600, 12000]:
[text](whiteboard.md)

## Algorithm
1. Define a nested helper function `inorder_traversal` that takes a node as an argument.
2. Initialize a variable `max_value` to negative infinity.
3. In the helper function:
   - If the node is not null, recursively call the function on the right child.
   - Compare the node's value with `max_value` and update `max_value` if the node's value is greater.
   - Recursively call the function on the left child.
4. Call the helper function starting from the root node.
5. Return `max_value`.

## Big O
- **Time Complexity:** O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once.
- **Space Complexity:** O(h), where h is the height of the tree. This is the space required for the recursion stack.

## Step Through
1. Start at the root node (1000).
2. Traverse to the right child (2000).
3. Traverse to the right child (12000).
4. Update `max_value` to 12000 since it is greater than the initial value of negative infinity.
5. Traverse back to node 2000 and then to the left child (None).
6. Traverse back to the root node (1000), compare and retain `max_value` as 12000.
7. Traverse to the left child (500).
8. Traverse to the right child (600).
9. Traverse back to node 500, then to the left child (250).
10. Finish traversal and return `max_value` as 12000.
