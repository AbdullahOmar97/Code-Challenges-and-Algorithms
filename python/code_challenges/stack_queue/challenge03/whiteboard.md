## Problem Domain
Write a function that takes a head of a Stack (represented as a list), deletes the middle element in the stack, and returns the new stack.

- **Input**: A stack represented as a list of integers.
  - Example 1: [1, 2, 3, 4, 5]
  - Example 2: [1, 2, 3, 4]
- **Output**: The stack after deleting the middle element.
  - Example 1 Output: [1, 2, 4, 5]
  - Example 2 Output: [1, 2, 4]

## Test Cases
1. **Odd number of elements**
   - Input: [1, 2, 3, 4, 5]
   - Output: [1, 2, 4, 5]
2. **Even number of elements**
   - Input: [1, 2, 3, 4]
   - Output: [1, 2, 4]
3. **Single element**
   - Input: [1]
   - Output: []
4. **Two elements**
   - Input: [1, 2]
   - Output: [2]
5. **Empty stack**
   - Input: []
   - Output: []

## Visualization
![alt text](<Screenshot 2024-06-06 055455.png>)
![alt text](<Scan_20240627 (4).jpg>)

### Example 1
Input: [1, 2, 3, 4, 5]
1. Calculate the middle index: len(stack) // 2 = 5 // 2 = 2
2. Remove the element at index 2: [1, 2, 4, 5]
Output: [1, 2, 4, 5]

### Example 2
Input: [1, 2, 3, 4]
1. Calculate the middle index: len(stack) // 2 = 4 // 2 = 2
2. Remove the element at index 2: [1, 2, 4]
Output: [1, 2, 4]

## Algorithm
1. Calculate the length of the stack.
2. Determine the middle index using integer division (len(stack) // 2).
3. Remove the element at the middle index.
4. Return the modified stack.

## Big O
- **Time Complexity:** O(n), where n is the number of elements in the stack. This is because removing an element from a list takes O(n) time in the worst case.
- **Space Complexity:** O(1), since we are modifying the stack in place and not using any extra space proportional to the input size.

## Step Through
- Create a stack instance and push elements [1, 2, 3, 4, 5] onto the stack.
- Call `delete_middle()` to delete the middle element.
- Print the resulting stack after deletion.
