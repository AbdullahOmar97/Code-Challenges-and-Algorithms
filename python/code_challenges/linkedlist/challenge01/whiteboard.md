### Work Documentation

### Problem Statement

You are given a singly-linked list. Write a function to delete a node in the linked list. However, you are not given access to the head of the list; instead, you are given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Implement the function `delete_node(node)` which takes the node to be deleted as a parameter and modifies the linked list in place.

### Example

#### Input:

Linked list: 4 -> 5 -> 1 -> 9
Node to be deleted: 5

#### Output:

Linked list after deletion: 4 -> 1 -> 9


Explanation: You are given the node with value `5`. After calling the `delete_node` function with this node, the linked list should become `4 -> 1 -> 9`.

### Constraints

- The number of nodes in the given list is in the range `[2, 1000]`.
- The value of each node in the list is in the range `[-1000, 1000]`.
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node.


#### `delete_node` Function

The `delete_node` function takes a node in a singly-linked list as input and deletes that node from the list. The function works by copying the value of the next node to the current node and then updating the next pointer of the current node to skip the next node, effectively removing it from the list.

Here's the pseudocode for the `delete_node` function:

#### Test Cases

Test cases are written using pytest to verify the correctness of the `delete_node` function. Each test case covers a specific scenario, such as deleting a node in the middle of the list or deleting a node at the beginning of the list.


