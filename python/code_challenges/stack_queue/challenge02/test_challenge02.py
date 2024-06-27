# Write your test here
# test_challenge02.py

from challenge02 import is_valid_parentheses

def test_valid_parentheses():
    assert is_valid_parentheses("()") == True
    print("Test 1 passed")
    assert is_valid_parentheses("()[]{}") == True
    print("Test 2 passed")
    assert is_valid_parentheses("[({})]") == True
    print("Test 3 passed")
    assert is_valid_parentheses("[{(())}]") == True
    print("Test 4 passed")
    assert is_valid_parentheses("[(hello)()]") == True
    print("Test 5 passed")

def test_invalid_parentheses():
    assert is_valid_parentheses("[({}]") == False
    print("Test 6 passed")
    assert is_valid_parentheses("[(])") == False
    print("Test 7 passed")
    assert is_valid_parentheses("([)]") == False
    print("Test 8 passed")
    assert is_valid_parentheses("(((") == False
    print("Test 9 passed")
    assert is_valid_parentheses("())") == False
    print("Test 10 passed")

# Run the tests
test_valid_parentheses()
test_invalid_parentheses()
