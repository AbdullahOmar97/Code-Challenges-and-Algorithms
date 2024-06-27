# Whiteboard Documentation

## Problem Domain
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

### Input
- `push(x)`: An integer `x` to be added to the queue.
- `pop()`: Removes and returns the front element of the queue.
- `peek()`: Returns the front element of the queue without removing it.
- `empty()`: Returns `true` if the queue is empty, otherwise `false`.

### Output
- For `push(x)`: No output.
- For `pop()`: The front element of the queue.
- For `peek()`: The front element of the queue.
- For `empty()`: A boolean value indicating if the queue is empty.

## Test Cases
1. **Initial state**:
    - `empty()` should return `true`.
2. **Push elements and check state**:
    - `push(1)`, `push(2)`, `push(3)`
    - `empty()` should return `false`.
3. **Peek and Pop operations**:
    - `peek()` should return `1`.
    - `pop()` should return `1`.
    - `pop()` should return `2`.
    - `peek()` should return `3`.
    - `pop()` should return `3`.
4. **Final state**:
    - `empty()` should return `true`.

## Visualization
![alt text](<Scan_20240627 (3).jpg>)

1. **Initialization**:
    - Two stacks `stack1` and `stack2` are empty.

2. **Push Operation**:
    - `push(1)`: `stack1` = [1], `stack2` = []
    - `push(2)`: `stack1` = [1, 2], `stack2` = []
    - `push(3)`: `stack1` = [1, 2, 3], `stack2` = []

3. **Pop Operation**:
    - Transfer `stack1` to `stack2`: `stack1` = [], `stack2` = [3, 2, 1]
    - `pop()`: Return `1`, `stack1` = [], `stack2` = [3, 2]

4. **Peek Operation**:
    - `peek()`: Return `2`, `stack1` = [], `stack2` = [3, 2]


## Algorithm
1. **Push(x)**:
    - Append `x` to `stack1`.

2. **Pop()**:
    - If `stack2` is empty, transfer all elements from `stack1` to `stack2`.
    - Pop the top element from `stack2`.

3. **Peek()**:
    - If `stack2` is empty, transfer all elements from `stack1` to `stack2`.
    - Return the top element from `stack2`.

4. **Empty()**:
    - Return `true` if both `stack1` and `stack2` are empty, otherwise `false`.

## Big O
### Time Complexity:
- **Push**: O(1) - Each element is pushed directly onto `stack1`.
- **Pop**: Amortized O(1) - Each element is moved between stacks at most once.
- **Peek**: Amortized O(1) - Similar reasoning as `pop`.
- **Empty**: O(1) - Simple check if both stacks are empty.

### Space Complexity:
- **Overall**: O(n) - We use space for two stacks, each holding up to `n` elements.


## Step Through

### Initialization
Create an instance of `MyQueue`, resulting in two empty stacks.

### Push Operations
Add elements to the queue using `push(x)`:
- Each push operation appends an element to `stack1`.

### Pop Operation
- If `stack2` is empty, transfer all elements from `stack1` to `stack2` and then pop from `stack2`.

### Peek Operation
- Similar to pop, but only returns the top element from `stack2` without removing it.

### Empty Check
- Simply check if both `stack1` and `stack2` are empty.
