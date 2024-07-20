# Whiteboard

## Problem Domain
- **Input**: A list of integers representing the level-order traversal of a binary tree.
  - Example: `[10, 20, 30, 40, 28, 27, 50, 29]`
- **Output**: The maximum height of the binary tree, measured in terms of edges.
  - Example: `3`

## Test Cases
1. **Example Case**
   - **Input**: `[10, 20, 30, 40, 28, 27, 50, 29]`
   - **Output**: `3`
   - **Description**: This case tests a typical binary tree with multiple levels.

2. **Empty Tree**
   - **Input**: `[]`
   - **Output**: `-1`
   - **Description**: This case tests the scenario of an empty tree. The height of an empty tree is considered `-1` for this implementation.

3. **Single Node**
   - **Input**: `[1]`
   - **Output**: `0`
   - **Description**: This case tests a tree with only one node. The height of a single node tree is `0`.

4. **Two Levels**
   - **Input**: `[1, 2, 3]`
   - **Output**: `1`
   - **Description**: This case tests a tree with two levels.

5. **Three Levels**
   - **Input**: `[1, 2, 3, 4, 5, 6, 7]`
   - **Output**: `2`
   - **Description**: This case tests a tree with three levels.

## Visualization
- **Example Tree for Input `[10, 20, 30, 40, 28, 27, 50, 29]`**:

![alt text](<لقطة شاشة 2024-07-20 233004.png>)

## Algorithm
1. **Build Tree**:
 - Initialize the root node with the first element of the list.
 - Use a queue to keep track of nodes and their children.
 - For each node, assign its left and right children based on the subsequent elements in the list.
 
2. **Calculate Height**:
 - Recursively compute the height of the left and right subtrees.
 - The height of the tree is the maximum of the heights of the left and right subtrees plus one.

## Big O
- **Time Complexity**: O(n)
- Building the tree takes O(n) time, where n is the number of nodes in the tree.
- Calculating the height also takes O(n) time as it visits each node once.
- **Space Complexity**: O(n)
- The space complexity is O(n) due to the space used by the queue during tree construction and the recursion stack for height calculation.

## Step Through
1. **Initialization**:
 - Start with an empty queue.
 - Create the root node using the first value from the input list.

2. **Tree Construction**:
 - Dequeue nodes and assign their left and right children using the next values in the list.
 - Continue this process until the entire list is processed.

3. **Height Calculation**:
 - For each node, recursively calculate the height of the left and right subtrees.
 - The height of the current node is the maximum of its children’s heights plus one.

4. **Return Result**:
 - Subtract `1` from the height returned by the recursive function to get the number of edges.
