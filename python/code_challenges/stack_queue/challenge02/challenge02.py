# Write here the code challenge solution
# challenge02.py

def is_valid_parentheses(s: str) -> bool:
    """
    Determine if the input string containing characters '(', ')', '{', '}', '[' and ']' is valid.
    A string is considered valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Non-bracket characters are ignored.

    Parameters:
    s (str): Input string containing brackets and other characters.

    Returns:
    bool: True if the string is valid, False otherwise.

    Examples:
    >>> is_valid_parentheses("()")
    True
    >>> is_valid_parentheses("()[]{}")
    True
    >>> is_valid_parentheses("[({})]")
    True
    >>> is_valid_parentheses("[{(())}]")
    True
    >>> is_valid_parentheses("[(hello)()]")
    True
    >>> is_valid_parentheses("[({}]")
    False
    >>> is_valid_parentheses("[(])")
    False
    >>> is_valid_parentheses("([)]")
    False
    >>> is_valid_parentheses("(((")
    False
    >>> is_valid_parentheses("())")
    False
    """
    # Dictionary to hold the mappings of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    for char in s:
        if char in bracket_map:
            # Pop the topmost element from the stack if it is non-empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the mapping for the closing bracket matches the top element of the stack
            if bracket_map[char] != top_element:
                return False
        elif char in bracket_map.values():
            # Push the current opening bracket onto the stack
            stack.append(char)
    
    # If the stack is empty, all the opening brackets had matching closing brackets
    return not stack
