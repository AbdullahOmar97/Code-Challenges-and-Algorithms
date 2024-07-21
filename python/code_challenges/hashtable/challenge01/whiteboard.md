# Whiteboard for Two Sum BST Problem

## Problem Domain
Given a Binary Search Tree (BST) and an integer `k`, determine if there exist two elements in the BST such that their sum is equal to `k`.

- **Input**:
  - A BST represented by its root node.
  - An integer `k`.

- **Output**:
  - A boolean value: `True` if there exist two elements in the BST whose sum is equal to `k`, otherwise `False`.

## Test Cases
1. **Test Case 1**:
   - **Input**: BST = [7, 2, 9, 1, 5, null, 14], k = 3
   - **Output**: `True`
   
2. **Test Case 2**:
   - **Input**: BST = [7, 2, 9, 1, 5, null, 14], k = 4
   - **Output**: `True`
   
3. **Test Case 3**:
   - **Input**: BST = [7, 2, 9, 1, 5, null, 14], k = 16
   - **Output**: `True`
   
4. **Test Case 4**:
   - **Input**: BST = [7, 2, 9, 1, 5, null, 14], k = 28
   - **Output**: `False`
   
5. **Test Case 5**:
   - **Input**: BST = None, k = 5
   - **Output**: `False`
   
6. **Test Case 6**:
   - **Input**: BST = [10], k = 20
   - **Output**: `False`

## Visualization

### Input
BST: [7, 2, 9, 1, 5, null, 14]
k = 3

![alt text](<لقطة شاشة 2024-07-21 064120.png>)

### Output
True

## Algorithm
1. Perform an in-order traversal of the BST to take advantage of its sorted property.
2. Use a hash table (set) to keep track of the values seen so far.
3. For each node, check if the complement (`k - node.val`) exists in the hash table.
4. If it exists, return `True`.
5. If not, add the current node's value to the hash table and continue the traversal.
6. If no such pair is found after the traversal, return `False`.

## Big O
- **Time Complexity:** O(n), where `n` is the number of nodes in the BST. Each node is visited exactly once.
- **Space Complexity:** O(n), for storing the values in the hash table and the recursion stack.

## Step Through
1. Start the in-order traversal at the root.
2. For each node, check if the complement (`k - node.val`) is in the hash table.
3. If found, return `True`.
4. If not found, add the node's value to the hash table.
5. Continue the traversal until all nodes are visited.
6. If no pair is found by the end of the traversal, return `False`.
