# Write your test here
# test_challenge02.py

import pytest
from challenge02 import is_valid_parentheses

def test_valid_parentheses():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("[({})]") == True
    assert is_valid_parentheses("[{(())}]") == True
    assert is_valid_parentheses("[(hello)()]") == True

def test_invalid_parentheses():
    assert is_valid_parentheses("[({}]") == False
    assert is_valid_parentheses("[(])") == False
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("(((") == False
    assert is_valid_parentheses("())") == False
