## Problem Domain
Determine if a given string containing the characters '(', ')', '{', '}', '[' and ']' is valid. A string is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

### Input:
- A string `s` containing characters '(', ')', '{', '}', '[' and ']'.

### Output:
- A boolean value: `True` if the string is valid, otherwise `False`.

## Test Cases
1. **Input:** `s = "()"`  
   **Output:** `True`
2. **Input:** `s = "()[]{}"`  
   **Output:** `True`
3. **Input:** `s = "[({})]"`  
   **Output:** `True`
4. **Input:** `s = "[{(())}]"`  
   **Output:** `True`
5. **Input:** `s = "[(hello)()]"`  
   **Output:** `True`
6. **Input:** `s = "[({}]`  
   **Output:** `False`
7. **Input:** `s = "[(])"`  
   **Output:** `False`
8. **Input:** `s = "([)]"`  
   **Output:** `False`
9. **Input:** `s = "((("`  
   **Output:** `False`
10. **Input:** `s = "())"`  
    **Output:** `False`

## Visualization



## Algorithm
1. Initialize a stack to keep track of opening brackets.
2. Create a dictionary to map closing brackets to their corresponding opening brackets.
3. Iterate over each character in the string:
   - If the character is a closing bracket, check if the stack is non-empty and the top of the stack is the corresponding opening bracket. If so, pop the stack. Otherwise, return `False`.
   - If the character is an opening bracket, push it onto the stack.
   - Ignore non-bracket characters.
4. After processing all characters, check if the stack is empty. If so, return `True`; otherwise, return `False`.

## Big O
- **Time Complexity:** O(n), where n is the length of the string. We iterate through the string once.
- **Space Complexity:** O(n), in the worst case, all the opening brackets are pushed onto the stack.

## Step Through
Initialize the stack and the bracket_map.
Iterate through each character in the string.
Depending on whether the character is an opening or closing bracket, perform the appropriate stack operation.
Ignore non-bracket characters.
After iteration, check if the stack is empty to determine if the string is valid.